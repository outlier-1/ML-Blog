# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170826_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]