# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-07 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0001_initial'),
        ('task', '0003_task_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='celery_task_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.TaskResult'),
        ),
    ]
