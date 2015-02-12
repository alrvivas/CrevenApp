# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_auto_20150116_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='fecha_a_agendar',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produccionrealizada',
            name='fecha_de_elaboracion',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
