# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('slug', models.SlugField(null=True, blank=True, help_text=b'Valor unico por producto URL pagina, creado desde nombre.', unique=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('orden', models.PositiveIntegerField(null=True, blank=True)),
                ('imagen', models.ImageField(upload_to=b'images/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True)),
            ],
            options={
                'ordering': ['orden'],
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
    ]
