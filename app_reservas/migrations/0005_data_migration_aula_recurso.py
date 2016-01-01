# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def crear_recursos_desde_aulas(apps, schema_editor):
    Aula = apps.get_model('app_reservas', 'Aula')
    Recurso = apps.get_model('app_reservas', 'Recurso')
    # Recorre todas las aulas existentes.
    for aula in Aula.objects.all():
        # Crea un nuevo recurso, con los datos necesarios.
        recurso = Recurso(
            calendar_codigo=aula.calendar_codigo,
            calendar_color=aula.calendar_color,
        )
        recurso.save()
        # Asocia el aula al recurso creado.
        aula.recurso_ptr = recurso
        aula.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0004_clase_recurso'),
    ]

    operations = [
        migrations.RunPython(crear_recursos_desde_aulas)
    ]
