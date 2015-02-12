# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saldo_anterior', '0004_auto_20150127_0854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saldo',
            options={'ordering': ['-fecha_cracion'], 'verbose_name': 'Saldo', 'verbose_name_plural': 'Saldos'},
        ),
        migrations.AlterField(
            model_name='saldo',
            name='fecha_cracion',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
