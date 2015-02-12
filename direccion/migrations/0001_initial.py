# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('address', models.CharField(max_length=255, verbose_name=b'Direccion ')),
                ('address2', models.CharField(max_length=255, verbose_name=b'Direccion2', blank=True)),
                ('zip_code', models.CharField(max_length=20, verbose_name=b'C.P.')),
                ('city', models.CharField(max_length=20, verbose_name=b'Ciudad')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='estado',
            field=models.ForeignKey(verbose_name=b'Estado', blank=True, to='direccion.Estado', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='user_billing',
            field=models.OneToOneField(related_name='billing_address', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='user_shipping',
            field=models.OneToOneField(related_name='shipping_address', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
