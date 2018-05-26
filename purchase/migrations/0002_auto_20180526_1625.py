# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contactNo',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fax_no',
            field=models.CharField(blank=True, default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='gst_pan',
            field=models.CharField(blank=True, default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='pincode',
            field=models.CharField(blank=True, default=0, max_length=6),
        ),
    ]
