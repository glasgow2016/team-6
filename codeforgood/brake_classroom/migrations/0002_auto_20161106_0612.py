# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brake_classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='co2_saved',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='money_saved',
            field=models.FloatField(default=0),
        ),
    ]
