# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0002_auto_20150108_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_totalpeso',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
