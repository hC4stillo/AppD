# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localizaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='denuncias',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='denuncias',
        ),
    ]
