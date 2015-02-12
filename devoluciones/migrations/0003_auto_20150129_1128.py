# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devoluciones', '0002_devolucionreproceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucionbuena',
            name='fecha_de_entrada',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='devolucionmala',
            name='fecha_de_salida',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='devolucionreproceso',
            name='fecha_de_entrada',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
