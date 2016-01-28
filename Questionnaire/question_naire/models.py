from django.db import models


class UserDefine(models.Model):
    username = models.CharField(max_length=20)
    pageForm = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.username
