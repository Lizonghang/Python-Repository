# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0008_auto_20160302_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='blog',
        ),
        migrations.AddField(
            model_name='blogmessage',
            name='author',
            field=models.ForeignKey(default=b'', verbose_name='\u4f5c\u8005', to='iec_blog.BlogUser'),
        ),
    ]
