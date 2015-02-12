# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import util.fields
import jsonfield.fields
from decimal import Decimal
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('producto', '0003_product_peso'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraOrderItemPriceField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255, verbose_name=b'Label')),
                ('value', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Amount', max_digits=30, decimal_places=2)),
                ('data', jsonfield.fields.JSONField(null=True, verbose_name=b'Serialized extra data', blank=True)),
            ],
            options={
                'verbose_name': 'Extra order item price field',
                'verbose_name_plural': 'Extra order item price fields',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraOrderPriceField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255, verbose_name=b'Label')),
                ('value', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Amount', max_digits=30, decimal_places=2)),
                ('data', jsonfield.fields.JSONField(null=True, verbose_name=b'Serialized extra data', blank=True)),
                ('is_shipping', models.BooleanField(default=False, verbose_name=b'Is shipping', editable=False)),
            ],
            options={
                'verbose_name': 'Extra order price field',
                'verbose_name_plural': 'Extra order price fields',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=10, verbose_name=b'Status', choices=[(10, b'Procesando'), (20, b'Confirmando'), (30, b'Confirmada'), (40, b'Completada'), (50, b'Enviada'), (60, b'Cancelada')])),
                ('order_subtotal', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Orden subtotal', max_digits=30, decimal_places=2)),
                ('order_total', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Orden Total', max_digits=30, decimal_places=2)),
                ('order_totalpeso', models.DecimalField(max_digits=10, decimal_places=3)),
                ('shipping_address_text', models.TextField(null=True, verbose_name=b'Direccion de Envio', blank=True)),
                ('billing_address_text', models.TextField(null=True, verbose_name=b'Direccion de Facturacion', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Updated')),
                ('cart_pk', models.PositiveIntegerField(null=True, verbose_name=b'Cart primary key', blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
                ('user', models.ForeignKey(verbose_name=b'User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name=b'Extra info', blank=True)),
                ('order', models.ForeignKey(related_name='extra_info', verbose_name=b'Order', to='orden.Order')),
            ],
            options={
                'verbose_name': 'Orden informacion extra',
                'verbose_name_plural': 'Orden informacion extra',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_reference', models.CharField(max_length=255, verbose_name=b'Product reference')),
                ('product_name', models.CharField(max_length=255, null=True, verbose_name=b'Product name', blank=True)),
                ('unit_price', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Unit price', max_digits=30, decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name=b'Cantidad')),
                ('line_subtotal', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Line subtotal', max_digits=30, decimal_places=2)),
                ('line_total', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Line total', max_digits=30, decimal_places=2)),
                ('line_subtotalpeso', models.DecimalField(max_digits=30, decimal_places=3)),
                ('line_totalpeso', models.DecimalField(max_digits=30, decimal_places=3)),
                ('order', models.ForeignKey(related_name='items', verbose_name=b'Orden', to='orden.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Producto', blank=True, to='producto.Product', null=True)),
            ],
            options={
                'verbose_name': 'Orden item',
                'verbose_name_plural': 'Orden items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', util.fields.CurrencyField(default=Decimal('0.00'), verbose_name=b'Amount', max_digits=30, decimal_places=2)),
                ('transaction_id', models.CharField(help_text=b"The transaction processor's reference", max_length=255, verbose_name=b'Transaction ID')),
                ('payment_method', models.CharField(help_text=b'The payment backend used to process the purchase', max_length=255, verbose_name=b'Payment method')),
                ('order', models.ForeignKey(verbose_name=b'Order', to='orden.Order')),
            ],
            options={
                'verbose_name': 'Order payment',
                'verbose_name_plural': 'Order payments',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='extraorderpricefield',
            name='order',
            field=models.ForeignKey(verbose_name=b'Order', to='orden.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extraorderitempricefield',
            name='order_item',
            field=models.ForeignKey(verbose_name=b'Order item', to='orden.OrderItem'),
            preserve_default=True,
        ),
    ]
