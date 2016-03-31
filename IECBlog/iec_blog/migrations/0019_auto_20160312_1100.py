# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0018_auto_20160312_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 11, 0, 30, 770528), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
