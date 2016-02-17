# coding=utf-8
from django.shortcuts import render_to_response
import json
from question_naire.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext


def home_page(request):
    if request.user.is_authenticated():
        user = request.session['username']
        logged = 'logged'
        return render_to_response("questionnaire.html", {'user': user, 'logged': logged})
    else:
        logged = 'unlogged'
        return render_to_response("questionnaire.html", {'logged': logged})


def login(request):
    if request.method == 'POST':
        if not request.user.is_authenticated():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['username'] = username
                return HttpResponse(username)
            else:
                return HttpResponse(u'该用户不存在或账户密码错误')
        else:
            return HttpResponse(u'您已登录')


def logout(request):
    auth.logout(request)
    return HttpResponse(u"您的账户已注销")


def clear_all_user(request):
    auth.logout(request)
    User.objects.all().delete()
    UserDefine.objects.all().delete()
    Statics.objects.all().delete()
    AnsCount.objects.all().delete()
    return HttpResponse("注册用户信息全部删除")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            return HttpResponse(u"该用户已注册")
        else:
            User.objects.create_user(username=username, password=password)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['username'] = username
            return HttpResponse(u"注册成功")
    else:
        return render_to_response("register.html")


def choose_template(request):
    if request.user.is_authenticated():
        return render_to_response("temp_choose.html")
    else:
        return HttpResponse("请先登录")


def agreement(request):
    return render_to_response("agreement.html")


def template_1(request):
    return render_to_response("template.html")


def submit_success(request):
    user = request.session['username']
    return render_to_response("Success.html", {'user': user})


def edit_template_1(request):
    user = request.session['username']
    return render_to_response("edit_template_1.html", {'user': user})


def view(request):
    user = request.GET.get('user')
    if request.method == 'POST':
        pageForm = request.POST.get('pageForm').encode('utf-8')
        QContent = request.POST.get('QContent').encode('utf-8')
        if UserDefine.objects.filter(username=user):
            s = Statics.objects.filter(user=UserDefine.objects.get(username=user))
            for i in range(0, len(s)):
                s[i].anscount_set.all().delete()
            UserDefine.objects.get(username=user).statics_set.all().delete()
            UserDefine.objects.get(username=user).delete()
        UserDefine.objects.create(username=user, pageForm=pageForm)
        s = Statics.objects.create(key='head', user=UserDefine.objects.get(username=user))
        s.QContent = QContent
        s.save()
        return HttpResponse('Method:Post')
    else:
        return render_to_response('user_def_temp1.html', {'pageForm': UserDefine.objects.get(username=user).pageForm, 'user': user})


def welcome(request):
    user = request.GET.get('user')
    return render_to_response('welcome.html', {'user': user})


def analysis(request):
    if request.method == 'POST':
        user = request.GET.get('user')
        ans = request.POST.get('data')
        ans = ans[2:len(ans) - 2].split("],[")
        arr = []
        type = request.POST.get('type')
        type = type[1:len(type) - 2].replace("\"", "")
        type_arr = type.split(",")
        for k in range(0, len(ans)):
            arr.append([])
            if type_arr[k] == 'fitb':
                arr[k].append(ans[k].replace("\"", ""))
                continue
            arr[k] = ans[k].split(",")
        for i in range(0, len(ans)):
            if type_arr[i] == 'fitb':
                continue
            for j in range(0, len(arr[i])):
                if arr[i][j] == '1' or arr[i][j] == '0':
                    arr[i][j] = int(arr[i][j])
        if UserDefine.objects.get(username=user).statics_set.exclude(key='head'):
            for m in range(0, len(ans)):
                if type_arr[m] == 'fitb':
                    foreign_key = 'arr[' + str(m) + '][0]'
                    s = UserDefine.objects.get(username=user).statics_set.get(key=foreign_key)
                    s.strValue = s.strValue + '\n' + arr[m][0]
                    s.save()
                    continue
                for l in range(0, len(arr[m])):
                    foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                    s = UserDefine.objects.get(username=user).statics_set.get(key=foreign_key)
                    s.intValue = s.intValue + arr[m][l]
                    s.save()
                if type_arr[m] == 'checkbox':
                    valid = False
                    for r in range(0, len(arr[m])):
                        if arr[m][r] == 1:
                            valid = True
                    if valid == True:
                        a = UserDefine.objects.get(username=user).statics_set.get(key='arr[' + str(m) + '][0]').anscount_set.get(key="multi_count")
                        a.multi_count += 1
                        a.save()
        else:
            for m in range(0, len(ans)):
                if type_arr[m] == 'fitb':
                    foreign_key = 'arr[' + str(m) + '][0]'
                    Statics.objects.create(key=foreign_key, strValue=arr[m][0],
                                           user=UserDefine.objects.get(username=user))
                    continue
                for l in range(0, len(arr[m])):
                    foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                    Statics.objects.create(key=foreign_key, intValue=arr[m][l],
                                           user=UserDefine.objects.get(username=user))
                if type_arr[m] == 'checkbox':
                    valid = False
                    for r in range(0, len(arr[m])):
                        if arr[m][r] == 1:
                            valid = True
                    if valid == True:
                        AnsCount.objects.create(multi_count=1, key="multi_count",
                                                question=UserDefine.objects.get(username=user).statics_set.get(key='arr[' + str(m) + '][0]'))
                    else:
                        AnsCount.objects.create(multi_count=0, key="multi_count",
                                                question=UserDefine.objects.get(username=user).statics_set.get(key='arr[' + str(m) + '][0]'))
            s = UserDefine.objects.get(username=user).statics_set.get(key="head")
            s.QType = type
            s.save()
            for k in range(0, len(ans)):
                s.dim += (str(len(arr[k])) + ',')
            s.dim = s.dim[0: len(s.dim)-1]
            dim = s.dim
            s.save()
        return HttpResponse(dim)


def real_handler(request):
    user = request.GET.get('user')
    s = UserDefine.objects.get(username=user).statics_set.get(key='head')
    d = UserDefine.objects.get(username=user).statics_set
    type = s.QType
    type_arr = type.split(",")
    dim = s.dim
    dim_arr = dim.split(",")
    for h in range(0, len(dim_arr)):
        dim_arr[h] = int(dim_arr[h])
    data_arr = []
    for i in range(0, len(dim_arr)):
        data_arr.append([])
        if dim_arr[i] == 1:
            foreign_key = 'arr[' + str(i) + '][0]'
            data_arr[i].append(d.get(key=foreign_key).strValue)
            continue
        for j in range(0, dim_arr[i]):
            foreign_key = 'arr[' + str(i) + '][' + str(j) + ']'
            data_arr[i].append(d.get(key=foreign_key).intValue)
    data_json = json.dumps(data_arr)
    valid_count = []
    for k in range(0, len(type_arr)):
        if type_arr[k] == 'fitb':
            a = d.get(key='arr['+str(k) + '][0]').strValue
            lenstr = len(a.split('\n'))
            valid_count.append(lenstr)
        elif type_arr[k] == 'radio':
            lenradio = 0
            for l in range(0, len(data_arr[k])):
                lenradio += data_arr[k][l]
            valid_count.append(lenradio)
        elif type_arr[k] == 'checkbox':
            lencheck = d.get(key='arr[' + str(k) + '][0]').anscount_set.get(key="multi_count").multi_count
            valid_count.append(lencheck)
    valid_json = json.dumps(valid_count)
    QContent = s.QContent
    return render_to_response("realTimeStatics.html", {'type': type, 'data': data_json, 'valid': valid_json, 'QContent': QContent, 'user': user})


def bad_request(request):
    return render_to_response("404.html", status=404)


def server_error(request):
    return render_to_response("50x.html", status=500)
