# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('pageForm', models.TextField(null=True, blank=True)),
                ('user_account', models.CharField(max_length=20)),
                ('passkey', models.CharField(max_length=20)),
            ],
        ),
    ]
