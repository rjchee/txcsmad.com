# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-26 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0004_auto_20170117_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_tags',
        ),
        migrations.AddField(
            model_name='event',
            name='event_tags',
            field=models.ManyToManyField(related_name='event_tags', to='events.EventTag', verbose_name='Tags'),
        ),
    ]
