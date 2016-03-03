# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import Aula


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0007_clase_laboratorio_informatico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='archivo_ubicacion',
            field=models.FileField(blank=True, upload_to=Aula.establecer_destino_archivo_ubicacion),
        ),
    ]
