# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Establecimiento de opción de ordenamiento para modelos 'Aula' y 'Nivel'.
    """

    dependencies = [
        ('app_reservas', '0017_cuerpo_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={
                'verbose_name_plural': 'Aulas',
                'verbose_name': 'Aula',
                'ordering': ['nivel', 'numero', 'nombre']
            },
        ),
        migrations.AlterModelOptions(
            name='nivel',
            options={
                'verbose_name_plural': 'Niveles',
                'verbose_name': 'Nivel',
                'ordering': ['cuerpo', 'numero']
            },
        ),
    ]
