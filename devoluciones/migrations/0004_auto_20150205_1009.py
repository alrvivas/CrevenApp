# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devoluciones', '0003_auto_20150129_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucionbuena',
            name='observacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='devolucionmala',
            name='observacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='devolucionreproceso',
            name='observacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
