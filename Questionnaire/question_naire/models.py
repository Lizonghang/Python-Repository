# coding=utf-8
from django.db import models


class UserDefine(models.Model):
    username = models.CharField(max_length=20)
    QCount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


class Question(models.Model):
    title = models.CharField(max_length=30)
    pageForm = models.TextField(blank=True, null=True)
    isEnd = models.BooleanField(default=False)
    user = models.ForeignKey(UserDefine)

    def __unicode__(self):
        return self.title + ',isEnd=' + str(self.isEnd) + ',user=' + self.user.username


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
