# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-21 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1),
        ),
    ]
