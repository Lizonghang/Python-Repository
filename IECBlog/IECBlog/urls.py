from django.conf.urls import include, url
from django.contrib import admin
from iec_blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/([a-zA-Z]*)/(\d{1,2})/$', blog),
    url(r'^test/$', test),
]
