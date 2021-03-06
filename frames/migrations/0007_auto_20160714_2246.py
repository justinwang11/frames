# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frames', '0006_auto_20160714_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='credit',
            field=models.CharField(choices=[('1', 'credit 1'), ('2', 'credit 2'), ('3', 'credit 3'), ('4', 'credit 4')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='credit_request_type',
            field=models.CharField(blank=True, choices=[('1', 'credit request type 1'), ('2', 'credit request type 2'), ('3', 'credit request type 3'), ('4', 'credit request type 4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='other_income',
            field=models.CharField(blank=True, choices=[('NONE', 'None'), ('OTHER', 'Other'), ('CHILD SUPPORT', 'Child Support'), ('ALIMONY', 'Alimony')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='purpose',
            field=models.CharField(choices=[('1', 'purpose 1'), ('2', 'purpose 2'), ('3', 'purpose 3'), ('4', 'purpose 4')], max_length=200),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='rank',
            field=models.CharField(blank=True, choices=[('1', 'rank 1'), ('2', 'rank 2'), ('3', 'rank 3'), ('4', 'rank 4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='service_branch',
            field=models.CharField(blank=True, choices=[('1', 'branch 1'), ('2', 'branch 2'), ('3', 'branch 3'), ('4', 'branch 4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='service_type',
            field=models.CharField(blank=True, choices=[('1', 'type 1'), ('2', 'type 2'), ('3', 'type 3'), ('4', 'type 4')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=200, null=True),
        ),
    ]
