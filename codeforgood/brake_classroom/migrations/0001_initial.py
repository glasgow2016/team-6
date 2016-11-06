# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('co2_saved', models.FloatField(null=True)),
                ('milage', models.FloatField()),
                ('money_saved', models.FloatField(null=True)),
                ('created', models.DateTimeField(null=True)),
                ('complete_in', models.IntegerField(default=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('question_title', models.TextField(max_length=500)),
                ('right_answer', models.CharField(max_length=128)),
                ('wrong_answer1', models.CharField(max_length=128)),
                ('wrong_answer2', models.CharField(max_length=128)),
                ('wrong_answer3', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.OneToOneField(null=True, to='brake_classroom.Project')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
