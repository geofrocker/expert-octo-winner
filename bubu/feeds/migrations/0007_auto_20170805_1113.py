# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-05 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_auto_20170805_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='height_field',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='feed',
            name='width_field',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
