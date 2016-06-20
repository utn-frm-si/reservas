# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import imagenCarrusel


class Migration(migrations.Migration):
    """
    Creación de carruseles de imágenes.
    """

    dependencies = [
        ('app_reservas', '0025_recurso_ali'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarruselImagenes',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        serialize=False,
                        verbose_name='ID',
                        primary_key=True,
                    )
                ),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('ancho_maximo', models.PositiveSmallIntegerField(default=800)),
            ],
            options={
                'verbose_name_plural': 'Carruseles de imágenes',
                'ordering': ['nombre'],
                'verbose_name': 'Carrusel de imágenes',
            },
        ),
        migrations.CreateModel(
            name='ImagenCarrusel',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        serialize=False,
                        verbose_name='ID',
                        primary_key=True,
                    )
                ),
                ('orden', models.PositiveSmallIntegerField(default=1)),
                (
                    'imagen',
                    models.ImageField(
                        upload_to=imagenCarrusel.establecer_destino_archivo_imagen
                    )
                ),
                (
                    'carrusel',
                    models.ForeignKey(
                        related_name='imagenes',
                        to='app_reservas.CarruselImagenes',
                    )
                ),
            ],
            options={
                'verbose_name_plural': 'Imágenes de carrusel',
                'ordering': ['carrusel', 'orden'],
                'verbose_name': 'Imagen de carrusel',
            },
        ),
    ]
