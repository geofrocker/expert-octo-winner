# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-08 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0016_auto_20170808_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='content',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]