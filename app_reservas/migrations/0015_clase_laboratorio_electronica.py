# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import laboratorioElectronica


class Migration(migrations.Migration):
    """
    Creación de modelo LaboratorioElectronica, subclase de Recurso.
    """

    dependencies = [
        ('app_reservas', '0014_model_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratorioElectronica',
            fields=[
                ('recurso_ptr', models.OneToOneField(parent_link=True,
                                                     auto_created=True,
                                                     primary_key=True,
                                                     to='app_reservas.Recurso',
                                                     serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=10)),
                ('capacidad', models.PositiveSmallIntegerField()),
                (
                    'archivo_ubicacion',
                    models.FileField(blank=True,
                                     upload_to=laboratorioElectronica
                                     .establecer_destino_archivo_ubicacion)
                ),
                ('nivel', models.ForeignKey(to='app_reservas.Nivel')),
            ],
            options={
                'verbose_name': 'Laboratorio de Electrónica',
                'verbose_name_plural': 'Laboratorios de Electrónica',
                'ordering': ['alias'],
            },
            bases=('app_reservas.recurso',),
        ),
    ]
