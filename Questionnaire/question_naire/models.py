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

    def __unicode__(self):
        return self.key
