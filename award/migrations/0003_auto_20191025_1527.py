# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-25 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_remove_project_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date',
            new_name='pub_date',
        ),
    ]
