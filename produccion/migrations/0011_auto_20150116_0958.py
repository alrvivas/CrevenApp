# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0010_auto_20150116_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='slug',
            field=models.SlugField(null=True, blank=True, unique=True, verbose_name=b'Slug'),
            preserve_default=True,
        ),
    ]
