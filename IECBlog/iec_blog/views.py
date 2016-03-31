# coding=utf-8
from django.shortcuts import render_to_response
from iec_blog.models import *
from django.http import HttpResponse
from datetime import datetime


def blog(request, author_name, blog_id):
    blog_id = int(blog_id)
    if not len(BlogUser.objects.filter(username=author_name)) == 1:
        return HttpResponse(u"没有这个作者")
    else:
        author = BlogUser.objects.get(username=author_name)
    if len(author.blog_set.filter(blog_id=blog_id)) == 1:
        blog_set = list(author.blog_set.order_by('publish_date'))
        blog_set_length = len(blog_set)
        blog = author.blog_set.get(blog_id=blog_id)
        blog_index = blog_set.index(blog)
        if blog_index == 0:
            newer_blog_index = blog_index + 1
            pre_link = '/blog/' + author_name + '/' + str(blog_set[newer_blog_index].blog_id) + '/'
            next_link = 'javascript:alert("已经是最后一篇")'
        elif blog_index == blog_set_length - 1:
            older_blog_index = blog_index - 1
            pre_link = 'javascript:alert("已经是最新文章")'
            next_link = '/blog/' + author_name + '/' + str(blog_set[older_blog_index].blog_id) + '/'
        else:
            newer_blog_index = blog_index + 1
            older_blog_index = blog_index - 1
            pre_link = '/blog/' + author_name + '/' + str(blog_set[newer_blog_index].blog_id) + '/'
            next_link = '/blog/' + author_name + '/' + str(blog_set[older_blog_index].blog_id) + '/'
        render_data = {
            'title': blog.title,
            'article': blog.article,
            'author': blog.author,
            'desc': blog.desc,
            'blog_id': blog.blog_id,
            'date': blog.publish_date,
            'pre': pre_link,
            'next': next_link,
        }
        return render_to_response('article.html', render_data)
    else:
        return HttpResponse(u"错误的ID")


def publish(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').replace('[', ' ').replace(']', ' ')
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
                return HttpResponse()
            else:
                if blog_user.blog_set.filter(title=title):
                    return HttpResponse(u'日志与文章列表不同步')
                blogid = len(blog_user.blog_set.all()) + 1
                BlogMessage.objects.create(title=title, article=article, author=BlogUser.objects.get(username=author),
                                           publish_date=date, blog_id=blogid, desc=desc)
                BlogCollectLog.objects.create(title=title, author=BlogUser.objects.get(username=author))
                return HttpResponse(u'收集: ' + title)
        else:
            return HttpResponse(u'不存在的用户')
    else:
        return HttpResponse(u'非法的请求')


def delete(request, author_name):
    blog_list = BlogUser.objects.get(username=author_name).blog_set.all()
    if len(blog_list):
        for each_blog in blog_list:
            blog_title = each_blog.title
            if BlogCollectLog.objects.filter(title=blog_title):
                BlogCollectLog.objects.get(title=blog_title).delete()
                each_blog.delete()
        return HttpResponse(u'删除作者:' + author_name + u' 的信息')
    else:
        return HttpResponse(u'作者:' + author_name + u'没有博客')
