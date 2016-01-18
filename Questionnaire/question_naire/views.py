from django.shortcuts import render_to_response


def home_page(request):
    return render_to_response("questionnaire.html")


def login(request):
    return render_to_response("login.html")


def register(request):
    return render_to_response("register.html")


def choose_template(request):
    return render_to_response("temp_choose.html")


def agreement(request):
    return render_to_response("agreement.html")
