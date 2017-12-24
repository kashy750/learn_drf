# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-24 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('identification_no', models.CharField(max_length=45)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('salutation', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=45)),
                ('profession', models.CharField(max_length=45)),
                ('income_range', models.CharField(max_length=45)),
                ('smoker', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('business_registration', models.CharField(max_length=45)),
                ('company_type', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('start_age', models.IntegerField()),
                ('end_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.IntegerField()),
                ('product_no', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=1)),
                ('sum_assured', models.CharField(max_length=45)),
                ('term_years', models.CharField(max_length=45)),
                ('premiums', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('sub_category', models.CharField(max_length=45)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category_id', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type_id', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=45)),
                ('registration_date', models.DateField()),
                ('email_verified', models.BooleanField()),
                ('mobile_verified', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Client')),
            ],
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ProductCategory'),
        ),
        migrations.AddField(
            model_name='policy',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Product'),
        ),
        migrations.AddField(
            model_name='package',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Policy'),
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Company'),
        ),
    ]
