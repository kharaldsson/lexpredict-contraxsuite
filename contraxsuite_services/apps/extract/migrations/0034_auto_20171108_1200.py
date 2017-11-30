# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20170818_0632'),
        ('extract', '0033_auto_20171103_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrademarkUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('trademark', models.CharField(db_index=True, max_length=200)),
                ('text_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.TextUnit')),
            ],
            options={
                'ordering': ('text_unit', '-count', 'trademark'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='trademarkusage',
            unique_together=set([('text_unit', 'trademark')]),
        ),
    ]
