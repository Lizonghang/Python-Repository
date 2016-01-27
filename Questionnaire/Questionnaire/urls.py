from django.conf.urls import include, url
from django.contrib import admin
from question_naire.views import *

urlpatterns = [
    url(r'^regist/$', register),
    url(r'^select/$', choose_template),
    url(r'^select/agreement/$', agreement),
    url(r'^select/template_1/$', template_1),
    url(r'^select/success/$', submit_success),
    url(r'^select/template_1/edit/$', edit_template_1),
    url(r'^select/template_1/view/$', view),
    url(r'^$', home_page),
]
