from django.shortcuts import render_to_response
from iec_blog.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


def blog(request, author_name, blog_id):
    blog_id = int(blog_id)
    if not len(BlogUser.objects.filter(username=author_name)) == 1:
        return HttpResponse("UserList Error Occur")
    else:
        author = BlogUser.objects.get(username=author_name)
    if len(author.blog_set.filter(blog_id=blog_id)) == 1:
        blog = author.blog_set.get(blog_id=blog_id)
        return render_to_response('blog_template.html', {'title': blog.title, 'article': blog.article, 'author': blog.author, 'ps': blog.ps, 'quoto': author.quoto, 'work': author.work})
    else:
        return HttpResponse("AuthorList Error Occur")


def test(request):
    return render_to_response('blog.html')
