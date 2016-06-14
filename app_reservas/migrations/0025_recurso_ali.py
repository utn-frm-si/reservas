# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import TipoRecursoAli


def crear_tipo_proyector_multimedia(apps, schema_editor):
    """Crea una instancia TipoRecursoAli para 'Electrónica'."""
    tipo_proyector_multimedia = TipoRecursoAli(
        nombre='Proyector multimedia',
        nombre_plural='Proyectores multimedia',
        slug='proyectores',
        prefijo='PM',
        is_sufijo=False,
        is_visible_navbar=True,
    )
    tipo_proyector_multimedia.save()


class Migration(migrations.Migration):
    """
    Creación de recursos de ALI genéricos con tipo asociado.
    """

    dependencies = [
        ('app_reservas', '0024_proyector_multimedia_a_recurso_ali'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRecursoAli',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        serialize=False,
                        primary_key=True,
                        verbose_name='ID'
                    )
                ),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_plural', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('prefijo', models.CharField(max_length=5)),
                ('is_sufijo', models.BooleanField(default=False)),
                ('is_visible_navbar', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Tipo de recurso del ALI',
                'verbose_name_plural': 'Tipos de recurso del ALI',
            },
        ),
        migrations.AlterModelOptions(
            name='recursoali',
            options={
                'ordering': ['identificador'],
                'verbose_name': 'Recurso del ALI',
                'verbose_name_plural': 'Recursos del ALI'
            },
        ),
        migrations.RunPython(crear_tipo_proyector_multimedia),
        migrations.AddField(
            model_name='recursoali',
            name='tipo',
            field=models.ForeignKey(to='app_reservas.TipoRecursoAli', default=1),
            preserve_default=False,
        ),
    ]
