# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0011_remove_bloguser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='author',
            field=models.ForeignKey(related_name='blog_set', default=b'', verbose_name='\u4f5c\u8005', to='iec_blog.BlogUser'),
        ),
    ]
