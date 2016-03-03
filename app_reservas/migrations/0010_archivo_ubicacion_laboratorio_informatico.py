# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import LaboratorioInformatico


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0009_clase_proyector_multimedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorioinformatico',
            name='archivo_ubicacion',
            field=models.FileField(upload_to=LaboratorioInformatico.establecer_destino_archivo_ubicacion, blank=True),
        ),
    ]
