# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-28 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0003_auto_20191028_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]