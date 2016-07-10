# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='images/')),
                ('image_url', models.URLField(max_length=250)),
                ('created_by', models.CharField(blank=True, default='', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image_name', models.CharField(blank=True, default='', max_length=100)),
                ('folder_name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
