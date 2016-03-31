# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('publish_date', models.DateTimeField()),
                ('author', models.CharField(max_length=10)),
                ('quote', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=20)),
            ],
        ),
    ]
