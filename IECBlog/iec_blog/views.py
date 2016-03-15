# coding=utf-8
from django.shortcuts import render_to_response
from iec_blog.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
import json
from datetime import datetime
import random


def blog(request, author_name, blog_id):
    blog_id = int(blog_id)
    if not len(BlogUser.objects.filter(username=author_name)) == 1:
        return HttpResponse("UserList Error Occur")
    else:
        author = BlogUser.objects.get(username=author_name)
    if len(author.blog_set.filter(blog_id=blog_id)) == 1:
        blog = author.blog_set.get(blog_id=blog_id)
        recommend_bloguser = BlogUser.objects.exclude(username=author_name).order_by('?')[0: 5]
        recommend_bloguser_username = []
        recommend_bloguser_blogid = []
        recommend_bloguser_blogtitle = []
        for each_bloguser in recommend_bloguser:
            recommend_bloguser_username.append(each_bloguser.username)
            each_blog = each_bloguser.blog_set.order_by('?')[0]
            recommend_bloguser_blogid.append(str(each_blog.blog_id))
            recommend_bloguser_blogtitle.append(each_blog.title)
        author_blog = author.blog_set.exclude(title=blog.title)
        if len(author_blog) > 5:
            author_blog = author_blog.order_by('?')[0:5]
        author_blogid = []
        author_blogtitle = []
        for each_blog in author_blog:
            author_blogtitle.append(each_blog.title)
            author_blogid.append(str(each_blog.blog_id))
        render_data = {
            'title': blog.title,
            'article': blog.article,
            'author': blog.author,
            'quoto': author.quoto,
            'work': author.work,
            'recommend_user': json.dumps(recommend_bloguser_username),
            'recommend_blogid': json.dumps(recommend_bloguser_blogid),
            'recommend_blogtitle': json.dumps(recommend_bloguser_blogtitle),
            'author_blogtitle': json.dumps(author_blogtitle),
            'author_blogid': json.dumps(author_blogid),
        }
        return render_to_response('blog_template.html', render_data)
    else:
        return HttpResponse("AuthorList Error Occur")


def publish(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        date = request.POST.get('date', '')
        desc = request.POST.get('desc', '')
        if title == '' or author == '':
            return HttpResponse(u'错误的数据')
        if date:
            date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')
        else:
            date = datetime.now()
        article = request.POST.get('article')
        if BlogUser.objects.filter(username=author):
            blog_user = BlogUser.objects.get(username=author)
            if blog_user.collect_log.filter(title=title):
                return HttpResponse(u'已存在: ' + title)
            else:
                if blog_user.blog_set.filter(title=title):
                    return HttpResponse(u'日志与文章列表不同步')
                blogid = len(blog_user.blog_set.all()) + 1
                # blogid = random.randint(0, 999)
                # while blog_user.blog_set.filter(blog_id=blogid):
                #     blogid = random.randint(0, 999)
                BlogMessage.objects.create(title=title, article=article, author=BlogUser.objects.get(username=author),
                                           publish_date=date, blog_id=blogid, desc=desc)
                BlogCollectLog.objects.create(title=title, author=BlogUser.objects.get(username=author))
                return HttpResponse(u'收集: ' + title)
        else:
            return HttpResponse(u'不存在的用户')
    else:
        return HttpResponse(u'非法的请求')
