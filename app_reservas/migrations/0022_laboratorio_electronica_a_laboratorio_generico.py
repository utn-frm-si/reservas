# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Renombrado de modelo LaboratorioElectronica a Laboratorio.
    """

    dependencies = [
        ('app_reservas', '0021_carga_atributos_visortv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaboratorioElectronica',
            new_name='Laboratorio',
        ),
    ]
