# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0004_auto_20160302_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmessage',
            name='author',
        ),
        migrations.AddField(
            model_name='bloguser',
            name='blog',
            field=models.ManyToManyField(to='iec_blog.BlogMessage', verbose_name='\u535a\u6587'),
        ),
    ]
