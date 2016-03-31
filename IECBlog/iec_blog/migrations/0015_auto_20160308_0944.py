# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0014_auto_20160303_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='ps',
            field=models.TextField(default=b'', verbose_name='\u5f15\u6587'),
        ),
    ]
