# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-06 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LostCard', '0008_specs_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specs',
            old_name='card',
            new_name='cards',
        ),
    ]
