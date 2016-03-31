# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0003_auto_20160302_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmessage',
            name='article',
            field=models.TextField(default=b'', verbose_name='\u535a\u6587\u5185\u5bb9'),
        ),
        migrations.AddField(
            model_name='bloguser',
            name='blog_site',
            field=models.URLField(default=b'', verbose_name='\u4e2a\u4eba\u4e3b\u9875'),
        ),
        migrations.RemoveField(
            model_name='blogmessage',
            name='author',
        ),
        migrations.AddField(
            model_name='blogmessage',
            name='author',
            field=models.ManyToManyField(to='iec_blog.BlogUser', verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='publish_date',
            field=models.DateField(verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u535a\u6587\u9898\u76ee'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='quoto',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u5f15\u8a00'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='work',
            field=models.CharField(default=b'', max_length=20, verbose_name='\u65b9\u5411'),
        ),
    ]
