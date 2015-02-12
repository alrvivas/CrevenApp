# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0002_auto_20150129_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salida',
            options={'ordering': ['-fecha_de_salida'], 'verbose_name': 'Salida', 'verbose_name_plural': 'Salidas'},
        ),
    ]
