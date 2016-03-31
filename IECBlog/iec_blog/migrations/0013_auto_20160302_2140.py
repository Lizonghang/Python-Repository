# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0012_auto_20160302_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='ps',
            field=models.TextField(default=b'', verbose_name='\u6ce8\u91ca'),
        ),
    ]
