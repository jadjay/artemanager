# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0005_auto_20160515_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='galerie.themes'),
        ),
    ]