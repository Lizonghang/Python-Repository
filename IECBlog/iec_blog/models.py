# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class BlogUser(User):
    quoto = models.CharField(blank=True, max_length=50, verbose_name=u'引言', default="")
    work = models.CharField(max_length=20, verbose_name=u'方向', default="")
    blog_site = models.URLField(blank=True, default="", verbose_name=u'个人主页')

    def __unicode__(self):
        return self.username


class BlogMessage(models.Model):
    title = models.CharField(max_length=80, verbose_name=u'博文题目')
    article = models.TextField(verbose_name=u'博文内容')
    author = models.ForeignKey(BlogUser, verbose_name=u'作者', related_name='blog_set')
    publish_date = models.DateTimeField(verbose_name=u'发布日期')
    desc = models.TextField(blank=True, default="", verbose_name=u'引文')
    blog_id = models.IntegerField(verbose_name=u'博文编号')

    def __unicode__(self):
        return self.title


class BlogCollectLog(models.Model):
    title = models.CharField(max_length=80, verbose_name=u'已收集的问卷')
    author = models.ForeignKey(BlogUser, verbose_name=u'作者', related_name='collect_log')

    def __unicode__(self):
        return self.title
