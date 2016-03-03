from django.contrib import admin
from iec_blog.models import *


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'work')


class BlogMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author', 'blog_id')


admin.site.register(BlogMessage, BlogMessageAdmin)
admin.site.register(BlogUser, BlogUserAdmin)
