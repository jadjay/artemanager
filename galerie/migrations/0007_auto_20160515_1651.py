# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galerie', '0006_pictures_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='themes',
            options={'verbose_name': 'Theme', 'verbose_name_plural': 'Themes'},
        ),
    ]
