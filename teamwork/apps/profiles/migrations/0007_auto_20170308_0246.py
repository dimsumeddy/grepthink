# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170308_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
