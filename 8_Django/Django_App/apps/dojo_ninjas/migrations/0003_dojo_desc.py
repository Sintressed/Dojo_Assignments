# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20180319_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='Helllojoiehfoiehfoiewhf', max_length=255),
            preserve_default=False,
        ),
    ]
