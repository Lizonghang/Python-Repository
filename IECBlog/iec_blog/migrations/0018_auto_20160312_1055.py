# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0017_auto_20160312_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='blog_id',
            field=models.IntegerField(default=False, verbose_name='\u535a\u6587\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 55, 8, 604213), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
