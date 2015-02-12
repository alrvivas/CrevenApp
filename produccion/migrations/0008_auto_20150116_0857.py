# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0007_auto_20150116_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='slug',
            field=models.SlugField(verbose_name=b'Slug'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produccionrealizada',
            name='slug',
            field=models.SlugField(verbose_name=b'Slug'),
            preserve_default=True,
        ),
    ]
