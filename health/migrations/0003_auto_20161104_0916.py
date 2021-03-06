# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-04 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20161104_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='current_hospital',
        ),
        migrations.AddField(
            model_name='patient',
            name='current_hospital_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_check_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 14, 16, 31, 527365, tzinfo=utc), verbose_name='End Time'),
        ),
    ]
