# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-02 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170731_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='products/', width_field='width_field'),
        ),
    ]
