# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_product_peso'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['categoria'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
