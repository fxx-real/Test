# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 10:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170324_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(choices=[(1, '\u8bfe\u7a0b'), (2, '\u673a\u6784'), (3, '\u6559\u5e08')])),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6536\u85cf\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237id')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
    ]
