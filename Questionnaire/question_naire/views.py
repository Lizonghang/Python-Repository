from django.shortcuts import render_to_response


def home_page(request):
    return render_to_response("questionnaire.html")


def register(request):
    return render_to_response("register.html")


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
