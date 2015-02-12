# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import util.fields
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Slug')),
                ('active', models.BooleanField(default=False, verbose_name=b'Activo')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de Creacion')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
                ('orden', models.PositiveIntegerField()),
                ('unit_price', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Precio', max_digits=30, decimal_places=2)),
                ('precio_a', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Precio A', max_digits=30, decimal_places=2)),
                ('precio_b', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Precio B', max_digits=30, decimal_places=2)),
                ('precio_c', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Precio C', max_digits=30, decimal_places=2)),
                ('imagen', models.ImageField(upload_to=b'images/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True)),
                ('categoria', models.ForeignKey(to='categoria.Categoria')),
            ],
            options={
                'ordering': ['orden'],
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
            bases=(models.Model,),
        ),
    ]
