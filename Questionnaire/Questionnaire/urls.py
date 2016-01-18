from django.conf.urls import include, url
from django.contrib import admin
from question_naire.views import *

urlpatterns = [
    url(r'login/$', login),
    url(r'regist/$', register),
    url(r'select/$', choose_template),
    url(r'select/agreement/$', agreement),
    url(r'', home_page),
]
