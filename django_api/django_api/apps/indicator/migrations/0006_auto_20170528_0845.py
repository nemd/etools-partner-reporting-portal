# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0005_auto_20170528_0128'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='disaggregation',
            unique_together=set([('name', 'reportable')]),
        ),
    ]
