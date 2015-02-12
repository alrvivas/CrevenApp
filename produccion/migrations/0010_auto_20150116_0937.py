# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0009_auto_20150116_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=b'Slug', blank=True),
            preserve_default=True,
        ),
    ]
