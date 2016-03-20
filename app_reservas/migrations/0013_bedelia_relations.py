# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Modificación de las relaciones de Bedelia:

        * Utilización de OneToOneField para relación con Area.
        * Permiso de campo vacío para las relaciones con Aula y LaboratorioInformatico.
    """

    dependencies = [
        ('app_reservas', '0012_clase_bedelia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedelia',
            name='area',
            field=models.OneToOneField(to='app_reservas.Area'),
        ),
        migrations.AlterField(
            model_name='bedelia',
            name='aulas',
            field=models.ManyToManyField(blank=True, to='app_reservas.Aula'),
        ),
        migrations.AlterField(
            model_name='bedelia',
            name='laboratorios_informatica',
            field=models.ManyToManyField(blank=True, to='app_reservas.LaboratorioInformatico'),
        ),
    ]
