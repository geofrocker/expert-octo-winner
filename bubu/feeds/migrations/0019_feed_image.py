# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-28 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0018_remove_feed_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='image',
            field=models.ImageField(blank=True, upload_to='timeline/'),
        ),
    ]
