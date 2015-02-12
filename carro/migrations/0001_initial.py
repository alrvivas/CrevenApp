# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_product_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['date_created'],
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(related_name='items', to='carro.Cart')),
                ('product', models.ForeignKey(to='producto.Product')),
            ],
            options={
                'verbose_name': 'Carro item',
                'verbose_name_plural': 'Carro items',
            },
            bases=(models.Model,),
        ),
    ]
