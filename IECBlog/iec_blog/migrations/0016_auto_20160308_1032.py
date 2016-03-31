# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0015_auto_20160308_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmessage',
            name='publish_date',
            field=models.DateTimeField(verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
