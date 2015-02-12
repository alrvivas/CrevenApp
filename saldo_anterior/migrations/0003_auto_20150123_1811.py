# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saldo_anterior', '0002_auto_20150123_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='fecha_de_entrada',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
