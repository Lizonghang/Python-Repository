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
        UserDefine.objects.filter(username="Hang").delete()
        UserDefine.objects.create(username="Hang", pageForm=pageForm)
    else:
        return render_to_response('user_def_temp1.html', {'pageForm': UserDefine.objects.get(username="Hang").pageForm})


def welcome(request):
    return render_to_response('welcome.html')


def analysis(request):
    ans = request.POST.get('data')
    ans = ans[2:len(ans)-3].split("],[")
    arr = []
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

    # for m in range(0, len(ans)):
    #     if len(arr[m]) == 1:
    #         foreign_key = 'arr[' + str(m) + '][0]'
    #         Statics.objects.filter(key=foreign_key).delete()
    #         Statics.objects.create(key=foreign_key, strValue=arr[m][0].replace("\"", ""), user=UserDefine.objects.get(username="Hang"))
    #         continue
    #     for l in range(0, len(arr[m])):
    #         foreign_key = 'arr[' + str(m) + '][' + str(l) + ']'
    #         Statics.objects.filter(key=foreign_key).delete()
    #         Statics.objects.create(key=foreign_key, intValue=arr[m][l], user=UserDefine.objects.get(username="Hang"))
    # t = UserDefine.objects.get(username="Hang").statics_set.get(key='arr[2][0]').strValue
    return HttpResponse(Statics.objects.all())
