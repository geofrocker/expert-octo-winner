# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-05 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20170805_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='photo',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='imagePosts/', width_field='width_field'),
        ),
    ]
