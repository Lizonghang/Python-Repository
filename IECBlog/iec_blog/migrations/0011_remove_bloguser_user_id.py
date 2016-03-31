# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0010_auto_20160302_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='user_id',
        ),
    ]
