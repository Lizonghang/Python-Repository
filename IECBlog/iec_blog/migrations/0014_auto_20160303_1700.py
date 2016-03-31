# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0013_auto_20160302_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='title',
            field=models.CharField(max_length=40, verbose_name='\u535a\u6587\u9898\u76ee'),
        ),
    ]
