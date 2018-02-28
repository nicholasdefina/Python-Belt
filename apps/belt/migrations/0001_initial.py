# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20180227_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoted_by', models.CharField(max_length=15)),
                ('quote', models.CharField(max_length=150)),
                ('favorites', models.ManyToManyField(related_name='userfaves', to='login_app.User')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userposts', to='login_app.User')),
            ],
        ),
    ]
