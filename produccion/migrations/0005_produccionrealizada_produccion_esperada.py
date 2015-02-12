# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0004_auto_20150115_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccionrealizada',
            name='produccion_esperada',
            field=models.ForeignKey(default=13, to='produccion.ProduccionEsperada'),
            preserve_default=False,
        ),
    ]
