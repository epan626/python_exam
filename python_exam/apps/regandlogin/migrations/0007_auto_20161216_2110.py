# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 21:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regandlogin', '0006_auto_20161216_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='product',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wish',
        ),
    ]