# coding=utf-8
from django.db import models


class UserDefine(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    QCount = models.IntegerField(default=0, verbose_name='问卷数目')
    headImgSrc = models.CharField(max_length=100, default="https://cdn.jinshuju.net/assets/columbus/avatar_default-5e358f2433179a760ee1ed1f7524eb66.png", verbose_name='头像链接')

    def __unicode__(self):
        return self.username


class Question(models.Model):
    title = models.CharField(max_length=30, verbose_name='问卷题目')
    pageForm = models.TextField(blank=True, null=True, verbose_name='问卷内容页')
    isEnd = models.BooleanField(default=False, verbose_name='停止发布')
    user = models.ForeignKey(UserDefine, verbose_name="问卷创建人")

    def __unicode__(self):
        return self.title


class Statics(models.Model):
    key = models.CharField(max_length=10)
    intValue = models.IntegerField(default=0)
    strValue = models.TextField(default="")
    QContent = models.TextField(default="")
    QType = models.TextField(default="")
    dim = models.CharField(default="", max_length=10)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.key + ':' + str(self.intValue) + ',' + self.strValue


class AnsCount(models.Model):
    statics = models.ForeignKey(Statics)
    key = models.CharField(max_length=20, default="")
    multi_count = models.IntegerField(default=0)

    def __unicode__(self):
        return u'多选题' + str(self.multi_count) + u'道'


class Collect(models.Model):
    user = models.ForeignKey(UserDefine)
    username = models.CharField(max_length=16, default="")
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title + ':' + self.link
