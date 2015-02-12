# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saldo_anterior', '0005_auto_20150128_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='saldo',
            name='observacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
