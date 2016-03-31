# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0007_auto_20160302_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmessage',
            name='blog_id',
            field=models.IntegerField(default=1, verbose_name='\u535a\u6587\u7f16\u53f7'),
        ),
        migrations.AddField(
            model_name='bloguser',
            name='user_id',
            field=models.IntegerField(default=1, verbose_name='\u4f5c\u8005\u7f16\u53f7'),
        ),
    ]
