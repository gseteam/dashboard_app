# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20160601_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_model',
            name='state',
            field=models.CharField(default=b'1', max_length=10),
        ),
    ]
