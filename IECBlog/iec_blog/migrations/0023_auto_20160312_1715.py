# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0022_auto_20160312_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcollectlog',
            name='title',
            field=models.CharField(max_length=80, verbose_name='\u5df2\u6536\u96c6\u7684\u95ee\u5377'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='title',
            field=models.CharField(max_length=80, verbose_name='\u535a\u6587\u9898\u76ee'),
        ),
    ]
