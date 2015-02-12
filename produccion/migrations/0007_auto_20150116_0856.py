# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0006_auto_20150115_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccionesperada',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name=b'Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionrealizada',
            name='slug',
            field=models.SlugField(default=2, unique=True, verbose_name=b'Slug'),
            preserve_default=False,
        ),
    ]
