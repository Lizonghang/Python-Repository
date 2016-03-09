# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0009_auto_20160302_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='blog_site',
            field=models.URLField(default=b'', verbose_name='\u4e2a\u4eba\u4e3b\u9875', blank=True),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='quoto',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u5f15\u8a00', blank=True),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='user_id',
            field=models.CharField(default=b'', max_length=2, verbose_name='\u4f5c\u8005\u7f16\u53f7'),
        ),
    ]
