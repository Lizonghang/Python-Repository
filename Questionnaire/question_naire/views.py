from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
import json
from django.template import Template, Context, loader
from question_naire.models import *
from django.http import HttpResponse


def home_page(request):
    return render_to_response("questionnaire.html")


def register(request):
    if request.method == 'GET':
        return render_to_response("register.html")
    else:
        pass


def choose_template(request):
    return render_to_response("temp_choose.html")


def agreement(request):
    return render_to_response("agreement.html")


def template_1(request):
    return render_to_response("template.html")


def submit_success(request):
    return render_to_response("Success.html")


def edit_template_1(request):
    return render_to_response("edit_template_1.html")


def view(request):
    if request.method == 'POST':
        pageForm = request.POST.get('pageForm').encode('utf-8')
        QContent = request.POST.get('QContent').encode('utf-8')
        UserDefine.objects.all().delete()
        Statics.objects.all().delete()
        AnsCount.objects.all().delete()
        UserDefine.objects.create(username="Hang", pageForm=pageForm)
        s = Statics.objects.create(key='head', user=UserDefine.objects.get(username="Hang"))
        s.QContent = QContent
        s.save()
    else:
        return render_to_response('user_def_temp1.html', {'pageForm': UserDefine.objects.get(username="Hang").pageForm})


def welcome(request):
    return render_to_response('welcome.html')


def analysis(request):
    ans = request.POST.get('data')
    ans = ans[2:len(ans) - 2].split("],[")
    arr = []
    type = request.POST.get('type')
    type = type[1:len(type) - 2].replace("\"", "")
    type_arr = type.split(",")
    for k in range(0, len(ans)):
        arr.append([])
        arr[k] = ans[k].split(",")
    for i in range(0, len(ans)):
        if len(arr[i]) == 1:
            arr[i][0] = arr[i][0].replace("\"", "")
            continue
        for j in range(0, len(arr[i])):
            if arr[i][j] == '1' or arr[i][j] == '0':
                arr[i][j] = int(arr[i][j])
    if UserDefine.objects.get(username="Hang").statics_set.exclude(key='head'):
        for m in range(0, len(ans)):
            if len(arr[m]) == 1:
                foreign_key = 'arr[' + str(m) + '][0]'
                s = UserDefine.objects.get(username="Hang").statics_set.get(key=foreign_key)
                s.strValue = s.strValue + '\n' + arr[m][0]
                s.save()
                continue
            for l in range(0, len(arr[m])):
                foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                s = UserDefine.objects.get(username="Hang").statics_set.get(key=foreign_key)
                s.intValue = s.intValue + arr[m][l]
                s.save()
            if type_arr[m] == 'checkbox':
                valid = False
                for r in range(0, len(arr[m])):
                    if arr[m][r] == 1:
                        valid = True
                if valid == True:
                    a = UserDefine.objects.get(username='Hang').statics_set.get(key='arr[' + str(m) + '][0]').anscount_set.all()
                    a.multi_count += 1
                    a.save()
    else:
        for m in range(0, len(ans)):
            if len(arr[m]) == 1:
                foreign_key = 'arr[' + str(m) + '][0]'
                Statics.objects.create(key=foreign_key, strValue=arr[m][0].replace("\"", ""),
                                       user=UserDefine.objects.get(username="Hang"))
                continue
            for l in range(0, len(arr[m])):
                foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
                Statics.objects.create(key=foreign_key, intValue=arr[m][l],
                                       user=UserDefine.objects.get(username="Hang"))
            if type_arr[m] == 'checkbox':
                valid = False
                for r in range(0, len(arr[m])):
                    if arr[m][r] == 1:
                        valid = True
                if valid == True:
                    AnsCount.objects.create(multi_count=1,
                                            question=Statics.objects.get(key='arr[' + str(m) + '][0]'))
                else:
                    AnsCount.objects.create(multi_count=0,
                                            question=Statics.objects.get(key='arr[' + str(m) + '][0]'))
        s = UserDefine.objects.get(username="Hang").statics_set.get(key="head")
        s.QType = type
        s.save()
        for k in range(0, len(ans)):
            s.dim += (str(len(arr[k])) + ',')
        s.dim = s.dim[0: len(s.dim)-1]
        s.save()
    return HttpResponse()


def real_handler(request):
    s = UserDefine.objects.get(username="Hang").statics_set.get(key='head')
    d = UserDefine.objects.get(username="Hang").statics_set
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
            data_arr[i][0] = d.get(key=foreign_key).strValue
            continue
        for j in range(0, dim_arr[i]):
            foreign_key = 'arr[' + str(i) + '][' + str(j) + ']'
            data_arr[i][j] = d.get(key=foreign_key).intValue
    data_json = json.dumps(data_arr)
    valid_count = []
    for k in range(0, len(type_arr)):
        if type_arr[k] == 'fitb':
            a = d.get(key='arr['+str(k) + '][0]').strValue
            lenstr = len(a.split('\n'))
            valid_count[k] = lenstr
        elif type_arr[k] == 'radio':
            lenradio = 0
            for l in range(0, len(data_arr[k])):
                lenradio += data_arr[k][l]
            valid_count[k] = lenradio
        elif type_arr[k] == 'checkbox':
            lencheck = d.get(key='arr[' + str(k) + '][0]').anscount_set.all().multi_count
            valid_count[k] = lencheck
    valid_json = json.dumps(valid_count)
    QContent = s.QContent
    return render_to_response("realTimeStatics.html", {'type': type, 'dim': dim, 'data': data_json, 'valid': valid_json, 'QContent': QContent})
    # return render_to_response("realTimeStatics.html", {'type': type, 'dim': dim, 'QContent': QContent})
