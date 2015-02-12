# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saldo_anterior', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='fecha_de_entrada',
            field=models.DateField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
