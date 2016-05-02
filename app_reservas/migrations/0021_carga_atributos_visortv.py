# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def carga_atributos_visores(apps, schema_editor):
    """Carga el nombre y slug de los visores existentes."""
    VisorTv = apps.get_model('app_reservas', 'VisorTv')
    # Recorre todos los visores existentes.
    for visor in VisorTv.objects.all():
        # Asigna el valor de los nuevos atributos de la instancia.
        visor.nombre = "Departamento de {0!s}".format(visor.area.nombre)
        visor.slug = visor.area.slug
        # Guarda el visor modificado.
        visor.save()


class Migration(migrations.Migration):
    """
    Carga de los nuevos atributos de VisorTv.
    """

    dependencies = [
        ('app_reservas', '0020_modificacion_visortv'),
    ]

    operations = [
        migrations.RunPython(carga_atributos_visores),
    ]
