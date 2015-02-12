# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0011_auto_20150116_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produccionesperada',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='produccionrealizada',
            name='slug',
        ),
    ]
