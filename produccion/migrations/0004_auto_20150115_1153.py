# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_auto_20150115_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionesperada',
            name='pendiente',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
