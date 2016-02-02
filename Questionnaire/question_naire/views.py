from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson
from django.template import Template, Context, loader
from question_naire.models import *


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
    if request.method == 'POST':
        data = simplejson.loads(request.POST.get('data'))
        with open('question_naire/testdata.py', 'ab') as f:
            f.write(''+data[0][0]+data[0][1]+data[0][2]+data[0][3]+data[0][4]+'\n'+data[1][0]+data[1][1]+data[1][2]+'\n'+ data[2][0]+'\n'+data[3][0]+data[3][1]+'\n'+data[4][0]+data[4][1]+data[4][2]+'\n'+data[5][0]+'\n'+'end')
