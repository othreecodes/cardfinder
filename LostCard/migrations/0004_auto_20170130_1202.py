# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-30 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostCard', '0003_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='Holder',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new',
            name='Type',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
    ]
