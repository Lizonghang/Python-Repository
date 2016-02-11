# coding=utf-8
from django.db import models


class UserDefine(models.Model):
    username = models.CharField(max_length=20)
    pageForm = models.TextField(blank=True, null=True)
    user_account = models.CharField(max_length=20)
    passkey = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


class Statics(models.Model):
    key = models.CharField(max_length=10)
    intValue = models.IntegerField(default=0)
    strValue = models.TextField(default="")
    user = models.ForeignKey(UserDefine)
    QContent = models.CharField(default="")
    QType = models.CharField(default="")
    dim = models.CharField(default="")

    def __unicode__(self):
        return self.key


class AnsCount(models.Model):
    question = models.ForeignKey(Statics)
    multi_count = models.IntegerField(default=0)

    def __unicode__(self):
        return u'多选题' + str(self.multi_count) + u'道'
