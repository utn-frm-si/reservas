# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Establecimiento de opción de ordenamiento para modelos.
    """

    dependencies = [
        ('app_reservas', '0013_bedelia_relations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['nombre'],
                     'verbose_name_plural': 'Áreas',
                     'verbose_name': 'Área'},
        ),
        migrations.AlterModelOptions(
            name='cuerpo',
            options={'ordering': ['numero'],
                     'verbose_name_plural': 'Cuerpos',
                     'verbose_name': 'Cuerpo'},
        ),
        migrations.AlterModelOptions(
            name='laboratorioinformatico',
            options={'ordering': ['alias'],
                     'verbose_name_plural': 'Laboratorios informáticos',
                     'verbose_name': 'Laboratorio informático'},
        ),
        migrations.AlterModelOptions(
            name='proyectormultimedia',
            options={'ordering': ['identificador'],
                     'verbose_name_plural': 'Proyectores multimedia',
                     'verbose_name': 'Proyector multimedia'},
        ),
    ]
