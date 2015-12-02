from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'home/$', home_page),
    url(r'login/$', login),
    url(r'regist/$', register),
    url(r'select/$', choose_template),
]
