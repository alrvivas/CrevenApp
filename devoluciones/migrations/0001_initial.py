# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_product_peso'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevolucionBuena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_entrada', models.DateTimeField(null=True, blank=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DevolucionMala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_salida', models.DateTimeField(null=True, blank=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
