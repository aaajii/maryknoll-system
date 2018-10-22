# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-22 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('work_type', models.CharField(choices=[('f', 'Full Time'), ('p', 'Part Time'), ('n', 'Others')], default='n', max_length=1)),
                ('emp_type', models.CharField(choices=[('c', 'Cashier'), ('r', 'Registrar'), ('h', 'Academic Head'), ('t', 'Teacher'), ('n', 'Others')], default='n', max_length=1)),
                ('emp_status', models.CharField(choices=[('a', 'Active'), ('o', 'On Leave'), ('i', 'Inactive')], default='i', max_length=1)),
            ],
            options={
                'verbose_name': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Promissory',
            fields=[
                ('promissory_ID', models.AutoField(primary_key=True, serialize=False)),
                ('promissory_title', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=500)),
                ('date_filed', models.DateTimeField(auto_now=True, null=True)),
                ('date_approved', models.DateTimeField(auto_now=True, null=True)),
                ('due_of_payment', models.DateTimeField(blank=True, null=True)),
                ('promissory_status', models.CharField(choices=[('h', 'On Hold'), ('p', 'Approved'), ('d', 'Declined')], default='h', max_length=1)),
            ],
            options={
                'verbose_name': 'Promissory Note',
            },
        ),
    ]
