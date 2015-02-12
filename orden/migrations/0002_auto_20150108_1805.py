# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='line_subtotalpeso',
            field=models.DecimalField(null=True, max_digits=30, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='line_totalpeso',
            field=models.DecimalField(null=True, max_digits=30, decimal_places=3),
            preserve_default=True,
        ),
    ]
