# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-24 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='users',
            name='registration_date',
            field=models.CharField(max_length=10),
        ),
    ]
