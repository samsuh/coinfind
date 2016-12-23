# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-21 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('collaborator', models.CharField(max_length=255)),
                ('follower', models.CharField(max_length=255)),
                ('cred_rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('ACManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project_url', models.TextField()),
                ('summary_url', models.TextField()),
            ],
            managers=[
                ('currencyManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
