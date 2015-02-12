# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20150117_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(default=b'images/default-01.png', upload_to=b'images/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True),
            preserve_default=True,
        ),
    ]
