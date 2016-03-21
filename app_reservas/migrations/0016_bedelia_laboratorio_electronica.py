# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Creación de relación entre Bedelia y LaboratorioElectronica.
    """

    dependencies = [
        ('app_reservas', '0015_clase_laboratorio_electronica'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedelia',
            name='laboratorios_electronica',
            field=models.ManyToManyField(to='app_reservas.LaboratorioElectronica', blank=True),
        ),
    ]
