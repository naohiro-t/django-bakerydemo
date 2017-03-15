# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0014_auto_20170303_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationoperatinghours',
            name='day',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUES', 'Tuesday'), ('WED', 'Wednesday'), ('THUR', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='MONDAY', max_length=4),
        ),
    ]
