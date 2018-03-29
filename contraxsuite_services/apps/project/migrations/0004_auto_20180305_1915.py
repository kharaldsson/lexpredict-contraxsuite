# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0020_auto_20180305_1404'),
        ('project', '0003_auto_20180302_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.DocumentType'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
