# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0007_auto_20160515_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='test',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='description',
            field=models.TextField(null=True),
        ),
    ]