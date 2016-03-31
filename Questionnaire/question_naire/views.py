# coding=utf-8
from django.shortcuts import render_to_response
import json
from question_naire.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth


def home_page(request):
    if request.user.is_authenticated():
        user = request.session['username']
        logged = 'logged'
        return render_to_response("questionnaire.html", {'user': user, 'logged': logged})
    else:
        logged = 'unlogged'
        return render_to_response("questionnaire.html", {'logged': logged})


def head_sculpture(request):
    if request.user.is_authenticated():
        user = request.session['username']
        head_img_src = UserDefine.objects.get(username=user).headImgSrc
        return render_to_response("head_sculpture.html", {'user': user, 'head_img_src': head_img_src})
    else:
        return HttpResponse("请先登录")


def set_head_img(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.session['username']
            img_src = request.POST.get('img_src')
            u = UserDefine.objects.get(username=user)
            u.headImgSrc = img_src
            u.save()
            return HttpResponse('头像设置成功')
        else:
            return HttpResponse('请先登录')
    else:
        return HttpResponse('ERROR METHOD GET')


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
    Question.objects.all().delete()
    Statics.objects.all().delete()
    AnsCount.objects.all().delete()
    Collect.objects.all().delete()
    return HttpResponse("注册用户信息全部删除")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            return HttpResponse(u"该用户已注册")
        else:
            User.objects.create_user(username=username, password=password)
            UserDefine.objects.create(username=username, QCount=0)
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
    user = request.GET.get('user')
    title = request.GET.get('title')
    head_img_src = UserDefine.objects.get(username=user).headImgSrc
    return render_to_response("Success.html", {'user': user, 'title': title, 'head_img_src': head_img_src})


def edit_template_1(request):
    user = request.session['username']
    return render_to_response("edit_template_1.html", {'user': user})


def re_edit(request):
    if request.user.is_authenticated():
        user = request.session['username']
        username = request.GET.get('user')
        title = request.GET.get('title')
        if user == username:
            question = UserDefine.objects.get(username=user).question_set.get(title=title)
            pageForm = question.pageForm
            return render_to_response('re_edit.html', {'pageForm': pageForm, 'user': user})
        else:
            return HttpResponse('您没有修改权限')
    else:
        return HttpResponse('请先登录')


def delete(request):
    if request.method == 'GET':
        user = request.GET.get('user')
        title = request.GET.get('title')
        q = UserDefine.objects.get(username=user).question_set.get(title=title)
        s = q.statics_set.all()
        for i in range(0, len(s)):
            s[i].anscount_set.all().delete()
        s.delete()
        q.delete()
        UserDefine.objects.get(username=user).collect_set.filter(username=user, title=title).delete()
        return HttpResponse('delete success')
    else:
        return HttpResponse('ERROR METHOD POST')


def delete_question(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            username = request.POST.get('username')
            title = request.POST.get('title')
            u = UserDefine.objects.get(username=username)
            q = u.question_set.get(title=title)
            s = q.statics_set.all()
            for i in range(0, len(s)):
                s[i].anscount_set.all().delete()
            s.delete()
            q.delete()
            u.collect_set.filter(username=username, title=title).delete()
            return HttpResponse('Success')
        else:
            return HttpResponse('请先登录')
    else:
        return HttpResponse('ERROR METHOD GET')


def view(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    if request.method == 'POST':
        pageForm = request.POST.get('pageForm').encode('utf-8')
        QContent = request.POST.get('QContent').encode('utf-8')
        if UserDefine.objects.get(username=user).question_set.filter(title=title):
            return HttpResponse("您已创建该问卷")
        Question.objects.create(title=title, pageForm=pageForm, isEnd=False, user=UserDefine.objects.get(username=user))
        u = UserDefine.objects.get(username=user)
        u.QCount += 1
        u.save()
        s = Statics.objects.create(key='head', question=Question.objects.get(title=title))
        s.QContent = QContent
        s.save()
        return HttpResponse('Saved')
    else:
        if UserDefine.objects.get(username=user).question_set.filter(title=title):
            isEnd = UserDefine.objects.get(username=user).question_set.get(title=title).isEnd
            return render_to_response('user_def_temp1.html', {'pageForm': UserDefine.objects.get(username=user).question_set.get(title=title).pageForm, 'user': user, 'title': title, 'isEnd': isEnd})
        else:
            return HttpResponse('该问卷不存在')


def welcome(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    return render_to_response('welcome.html', {'user': user, 'title': title})


def analysis(request):
    if request.method == 'POST':
        user = request.GET.get('user')
        title = request.GET.get('title')
        if UserDefine.objects.get(username=user).question_set.get(title=title).isEnd:
            return HttpResponse('该问卷已停止发布')
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
        if UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.exclude(key='head'):
            for m in range(0, len(ans)):
                if type_arr[m] == 'fitb':
                    foreign_key = 'arr[' + str(m) + '][0]'
                    s = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key=foreign_key)
                    s.strValue = s.strValue + '\n' + arr[m][0]
                    s.save()
                    continue
                for l in range(0, len(arr[m])):
                    foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                    s = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key=foreign_key)
                    s.intValue = s.intValue + arr[m][l]
                    s.save()
                if type_arr[m] == 'checkbox':
                    valid = False
                    for r in range(0, len(arr[m])):
                        if arr[m][r] == 1:
                            valid = True
                    if valid == True:
                        a = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key='arr[' + str(m) + '][0]').anscount_set.get(key="multi_count")
                        a.multi_count += 1
                        a.save()
        else:
            for m in range(0, len(ans)):
                if type_arr[m] == 'fitb':
                    foreign_key = 'arr[' + str(m) + '][0]'
                    Statics.objects.create(key=foreign_key, strValue=arr[m][0],
                                           question=UserDefine.objects.get(username=user).question_set.get(title=title))
                    continue
                for l in range(0, len(arr[m])):
                    foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                    Statics.objects.create(key=foreign_key, intValue=arr[m][l],
                                           question=UserDefine.objects.get(username=user).question_set.get(title=title))
                if type_arr[m] == 'checkbox':
                    valid = False
                    for r in range(0, len(arr[m])):
                        if arr[m][r] == 1:
                            valid = True
                    if valid == True:
                        AnsCount.objects.create(multi_count=1, key="multi_count",
                                                statics=UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key='arr[' + str(m) + '][0]'))
                    else:
                        AnsCount.objects.create(multi_count=0, key="multi_count",
                                                statics=UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key='arr[' + str(m) + '][0]'))
            s = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key="head")
            s.QType = type
            s.save()
            for k in range(0, len(ans)):
                s.dim += (str(len(arr[k])) + ',')
            s.dim = s.dim[0: len(s.dim)-1]
            dim = s.dim
            s.save()
        return HttpResponse()


def real_handler(request):
    user = request.GET.get('user')
    title = request.GET.get('title')
    if UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.exclude(key='head'):
        s = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set.get(key='head')
        d = UserDefine.objects.get(username=user).question_set.get(title=title).statics_set
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
        isEnd = UserDefine.objects.get(username=user).question_set.get(title=title).isEnd
        return render_to_response("realTimeStatics.html", {'type': type, 'data': data_json, 'valid': valid_json, 'QContent': QContent, 'user': user, 'isEnd': isEnd})
    else:
        return render_to_response("no_ans_collect.html")


def end_publish(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.session['username']
            title = request.POST.get('title')
            username = request.POST.get('username')
            if user == username:
                q = UserDefine.objects.get(username=user).question_set.get(title=title)
                q.isEnd = True
                q.save()
                return HttpResponse('该问卷停止发布')
            else:
                return HttpResponse('您没有权限停止发布')
        else:
            return HttpResponse('您没有登录')
    else:
        return HttpResponse('ERROR OPERATION GET')


def user_list(request):
    if request.user.is_authenticated():
        user = request.session['username']
        head_img_src = UserDefine.objects.get(username=user).headImgSrc
        titles = ''
        collect = ''
        qs = UserDefine.objects.get(username=user).question_set.all()
        if qs:
            for i in range(0, len(qs)):
                titles += (qs[i].title + ',')
                if UserDefine.objects.get(username=user).collect_set.filter(title=qs[i].title):
                    collect += '1,'
                else:
                    collect += '0,'
            titles = titles[0: len(titles)-1]
            collect = collect[0: len(collect)-1]
        return render_to_response("userQList.html", {'user': user, 'titles': titles, 'collect': collect, 'head_img_src': head_img_src})
    else:
        return HttpResponse("请先登录")


def collect_log(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.session['username']
            method = request.POST.get('method')
            username = request.POST.get('username')
            title = request.POST.get('title')
            if method == 'collect':
                Collect.objects.create(user=UserDefine.objects.get(username=user), username=username, title=title)
                return HttpResponse('收藏成功')
            elif method == 'uncollect':
                UserDefine.objects.get(username=user).collect_set.get(username=username, title=title).delete()
                return HttpResponse('取消收藏')
        else:
            return HttpResponse('请先登录')
    else:
        return HttpResponse('Method: GET Error')


def is_collected(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.session['username']
            username = request.POST.get('username')
            title = request.POST.get('title')
            if UserDefine.objects.get(username=user).collect_set.filter(username=username, title=title):
                return HttpResponse('collected')
            else:
                return HttpResponse('uncollected')
        else:
            return HttpResponse('uncollected')
    else:
        return HttpResponse('Method GET Error')


def collect(request):
    if request.user.is_authenticated():
        user = request.session['username']
        head_img_src = UserDefine.objects.get(username=user).headImgSrc
        c = UserDefine.objects.get(username=user).collect_set.all()
        username = ''
        titles = ''
        if c:
            for i in range(0, len(c)):
                titles += (c[i].title + ',')
                username += (c[i].username + ',')
            titles = titles[0: len(titles)-1]
            username = username[0: len(username)-1]
        return render_to_response("collect.html", {'user': user, 'titles': titles, 'username': username, 'head_img_src': head_img_src})
    else:
        return HttpResponse("请先登录")


def search(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            title_include = request.GET.get('keyword')
            sq = Question.objects.filter(title__contains=title_include)
            titles = ''
            if sq:
                for i in range(0, len(sq)):
                    titles += (sq[i].title + ',')
                titles = titles[0: len(titles)-1]
            return HttpResponse(titles)
        else:
            return HttpResponse('ERROR METHOD POST')
    else:
        return HttpResponse('请先登录')


def search_result(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            user = request.session['username']
            title_include = request.GET.get('title_include')
            head_img_src = UserDefine.objects.get(username=user).headImgSrc
            sq = Question.objects.filter(title__contains=title_include)
            username = ''
            titles = ''
            collects = ''
            if sq:
                for i in range(0, len(sq)):
                    username += (sq[i].user.username + ',')
                    titles += (sq[i].title + ',')
                    if UserDefine.objects.get(username=user).collect_set.filter(username=sq[i].user.username, title=sq[i].title):
                        collects += '1,'
                    else:
                        collects += '0,'
                username = username[0: len(username)-1]
                titles = titles[0: len(titles)-1]
                collects = collects[0: len(collects)-1]
            return render_to_response("search_result.html", {'user': user, 'head_img_src': head_img_src, 'username': username, 'titles': titles, 'collect': collects})
        else:
            return HttpResponse('ERROR METHOD POST')
    else:
        return HttpResponse('请先登录')


def bad_request(request):
    return render_to_response("404.html", status=404)


def server_error(request):
    return render_to_response("50x.html", status=500)


def code(request):
    return render_to_response('code.html')


def interact(request):
    return render_to_response('interact.html')
