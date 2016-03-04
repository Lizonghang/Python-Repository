from django.shortcuts import render_to_response
from iec_blog.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
import json


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
        author_blog = author.blog_set.all()
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
            'ps': blog.ps,
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


def test(request):
    return render_to_response('blog.html')
