# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-04 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20161104_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='is_check_in',
            new_name='is_checked_in',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 14, 19, 25, 22367, tzinfo=utc), verbose_name='End Time'),
        ),
    ]
