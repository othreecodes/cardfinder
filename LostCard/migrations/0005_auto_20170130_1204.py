# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-30 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LostCard', '0004_auto_20170130_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='Holder',
        ),
        migrations.RemoveField(
            model_name='new',
            name='Type',
        ),
    ]
