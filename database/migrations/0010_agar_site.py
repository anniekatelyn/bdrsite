# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20171030_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agar',
            fields=[
                ('agar_id', models.IntegerField(primary_key=True, serialize=False)),
                ('media', models.CharField(max_length=100)),
                ('temp', models.CharField(max_length=20)),
                ('ctx', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
