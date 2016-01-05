# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0008_directorio_archivo_ubicacion_aula'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectorMultimedia',
            fields=[
                ('recurso_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app_reservas.Recurso')),
                ('identificador', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Proyector multimedia',
                'verbose_name_plural': 'Proyectores multimedia',
            },
            bases=('app_reservas.recurso',),
        ),
    ]
