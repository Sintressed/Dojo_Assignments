# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='LoginRegistration',
        ),
    ]
