# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0012_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Project URL'),
        ),
    ]
