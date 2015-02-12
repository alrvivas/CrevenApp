# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0013_auto_20150128_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccionrealizada',
            name='observacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
