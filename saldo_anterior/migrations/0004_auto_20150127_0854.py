# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saldo_anterior', '0003_auto_20150123_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saldo',
            name='estatus',
            field=models.ForeignKey(default=1, to='saldo_anterior.Estatus'),
            preserve_default=False,
        ),
    ]
