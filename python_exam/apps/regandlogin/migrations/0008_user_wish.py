# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_user'),
        ('regandlogin', '0007_auto_20161216_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wish',
            field=models.ManyToManyField(related_name='user__wish', to='products.Product'),
        ),
    ]