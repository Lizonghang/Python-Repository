# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('iec_blog', '0002_auto_20160302_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('quoto', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='blogmessage',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='blogmessage',
            name='work',
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='author',
            field=models.ForeignKey(to='iec_blog.BlogUser'),
        ),
    ]
