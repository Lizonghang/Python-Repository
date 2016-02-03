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
        for j in range(0, len(arr[i])):
            if arr[i][j] == '1' or arr[i][j] == '0':
                arr[i][j] = int(arr[i][j])
    return HttpResponse(arr[2][0]+arr[5][0])
