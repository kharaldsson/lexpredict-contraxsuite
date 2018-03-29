# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180302_0904'),
        ('document', '0019_auto_20180223_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AddField(
            model_name='historicaldocument',
            name='project',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project'),
        ),
    ]
