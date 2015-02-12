# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0014_produccionrealizada_observacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produccionesperada',
            options={'ordering': ['-fecha_a_agendar'], 'verbose_name': 'Produccion Esperada', 'verbose_name_plural': 'Producciones Esperadas'},
        ),
        migrations.AlterModelOptions(
            name='produccionrealizada',
            options={'ordering': ['-fecha_de_elaboracion'], 'verbose_name': 'Produccion Realizada', 'verbose_name_plural': 'Producciones Realizada'},
        ),
    ]
