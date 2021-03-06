# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frames', '0009_auto_20160714_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='credit',
            field=models.CharField(blank=True, choices=[('1', 'credit 1'), ('2', 'credit 2'), ('3', 'credit 3'), ('4', 'credit 4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='purpose',
            field=models.CharField(blank=True, choices=[('1', 'purpose 1'), ('2', 'purpose 2'), ('3', 'purpose 3'), ('4', 'purpose 4')], max_length=200, null=True),
        ),
    ]
