# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0021_auto_20160312_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='desc',
            field=models.TextField(default=b'', verbose_name='\u5f15\u6587', blank=True),
        ),
    ]
