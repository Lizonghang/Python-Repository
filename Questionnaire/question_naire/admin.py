from django.contrib import admin
from question_naire.models import *


class UserDefineAdmin(admin.ModelAdmin):
    list_display = ('username', 'QCount', 'headImgSrc')
    search_fields = 'username'


admin.site.register(Question)
admin.site.register(UserDefine, UserDefineAdmin)
