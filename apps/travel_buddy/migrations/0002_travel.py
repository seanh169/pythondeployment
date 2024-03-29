# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planner', to='travel_buddy.User')),
                ('tempo', models.ManyToManyField(related_name='joiner', to='travel_buddy.User')),
            ],
        ),
    ]
