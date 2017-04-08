# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valid_at', models.DateTimeField(db_index=True)),
                ('value', models.FloatField()),
                ('units', models.CharField(db_index=True, max_length=10)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'valid_at',
            },
        ),
        migrations.CreateModel(
            name='PowerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valid_at', models.DateTimeField(db_index=True)),
                ('is_on', models.BooleanField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'valid_at',
            },
        ),
    ]
