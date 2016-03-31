# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0006_blogmessage_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='ps',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u6ce8\u91ca'),
        ),
    ]
