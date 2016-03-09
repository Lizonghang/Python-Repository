# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    quoto = models.CharField(max_length=50, verbose_name=u'引言', default="", blank=True)
    work = models.CharField(max_length=20, verbose_name=u'方向', default="")
    blog_site = models.URLField(default="", verbose_name=u'个人主页', blank=True)

    def __unicode__(self):
        return self.username


class BlogMessage(models.Model):
    title = models.CharField(max_length=40, verbose_name=u'博文题目')
    article = models.TextField(default="", verbose_name=u'博文内容')
    author = models.ForeignKey(BlogUser, default="", verbose_name=u'作者', related_name='blog_set')
    publish_date = models.DateTimeField(verbose_name=u'发布日期')
    ps = models.TextField(default="", verbose_name=u'引文')
    blog_id = models.IntegerField(default=1, verbose_name=u'博文编号')

    def __unicode__(self):
        return self.title
