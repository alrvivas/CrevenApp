# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='fecha_de_salida',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
