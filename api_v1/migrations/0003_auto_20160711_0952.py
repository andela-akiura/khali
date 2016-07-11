# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20160711_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
        migrations.AddField(
            model_name='image',
            name='filter_name',
            field=models.CharField(choices=[('NONE', 'none'), ('BLUR', 'blur'), ('CONTOUR', 'contour'), ('DETAIL', 'detail'), ('EDGE_ENHANCE', 'enhance'), ('EMBOSS', 'emboss'), ('SMOOTH', 'smoothen'), ('SHARPEN', 'sharpen'), ('FLIP', 'flip'), ('GRAYSCALE ', 'grayscale'), ('FIND_EDGES', 'find edges')], default='', max_length=100),
        ),
    ]