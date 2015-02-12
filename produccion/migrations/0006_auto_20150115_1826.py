# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_produccionrealizada_produccion_esperada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produccionesperada',
            old_name='pendiente',
            new_name='realizada',
        ),
    ]
