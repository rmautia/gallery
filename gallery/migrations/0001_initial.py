# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
    ]
