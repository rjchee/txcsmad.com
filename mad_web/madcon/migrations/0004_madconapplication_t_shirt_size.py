# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('madcon', '0003_madconapplication_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='madconapplication',
            name='t_shirt_size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')],
                                   max_length=3),
        ),
    ]
