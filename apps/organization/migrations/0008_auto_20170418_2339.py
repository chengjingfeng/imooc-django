# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_courseorg_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='封面图'),
        ),
    ]