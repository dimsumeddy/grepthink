# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170216_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='project2',
            name='members',
            field=models.ManyToManyField(through='core.Membership', to='core.Studs'),
        ),
    ]
