# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Creación de campo 'nombre' en Cuerpo.
    """

    dependencies = [
        ('app_reservas', '0016_bedelia_laboratorio_electronica'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuerpo',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
