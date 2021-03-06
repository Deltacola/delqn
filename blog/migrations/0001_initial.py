# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=10)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=8)),
                ('total_length', models.IntegerField(default=0)),
                ('del_time', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_area', models.CharField(max_length=10)),
                ('end_area', models.CharField(max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('tel_num', models.CharField(blank=True, max_length=16)),
            ],
        ),
    ]
