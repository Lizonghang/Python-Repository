# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iec_blog', '0016_auto_20160308_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCollectLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=False, max_length=40, verbose_name='\u5df2\u6536\u96c6\u7684\u95ee\u5377')),
                ('author', models.ForeignKey(related_name='collect_log', default=False, verbose_name='\u4f5c\u8005', to='iec_blog.BlogUser')),
            ],
        ),
        migrations.RenameField(
            model_name='blogmessage',
            old_name='ps',
            new_name='desc',
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='article',
            field=models.TextField(default=False, verbose_name='\u535a\u6587\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='author',
            field=models.ForeignKey(related_name='blog_set', default=False, verbose_name='\u4f5c\u8005', to='iec_blog.BlogUser'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='blog_id',
            field=models.IntegerField(default=515, verbose_name='\u535a\u6587\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 10, 48, 42, 907184), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='blogmessage',
            name='title',
            field=models.CharField(default=False, max_length=40, verbose_name='\u535a\u6587\u9898\u76ee'),
        ),
    ]
