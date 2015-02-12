# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_produccionesperada_pendiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='pendiente',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
