# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processName', models.CharField(max_length=100)),
                ('processId', models.CharField(max_length=100)),
            ],
        ),
    ]