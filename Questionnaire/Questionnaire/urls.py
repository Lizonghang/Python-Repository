from django.conf.urls import include, url
from django.contrib import admin
from question_naire.views import *

urlpatterns = [
    url(r'^regist/$', register),
    url(r'^select/$', choose_template),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^clear_all_user', clear_all_user),
    url(r'^select/agreement/$', agreement),
    url(r'^select/template_1/$', template_1),
    url(r'^select/success/$', submit_success),
    url(r'^select/template_1/edit/$', edit_template_1),
    url(r'^select/template_1/view/$', view),
    url(r'^select/template_1/analysis/$', analysis),
    url(r'^submit/welcome/$', welcome),
    url(r'^submit/welcome/realHandler/$', real_handler),
    url(r'^$', home_page),
]
