from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
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
    respnse = "" + ans + "\n" + ans[0][0]+ans[0][1]+ans[0][2]+ans[0][3]+ans[0][4]+"\n"+ans[1][0]+ans[1][1]+ans[1][2]+"\n"+ans[2][0]+"\n"+ans[3][0]+ans[3][1]+"\n"+ans[4][0]+ans[4][1]+ans[4][2]+"\n"+ans[5][0]
    return HttpResponse(respnse)
