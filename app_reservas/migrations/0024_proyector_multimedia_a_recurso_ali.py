# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Renombrado de modelo ProyectorMultimedia a RecursoAli.
    """

    dependencies = [
        ('app_reservas', '0023_laboratorio_generico'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProyectorMultimedia',
            new_name='RecursoAli',
        ),
    ]
