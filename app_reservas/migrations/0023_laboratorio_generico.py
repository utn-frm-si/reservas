# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import TipoLaboratorio


def crear_tipo_laboratorio_electronica(apps, schema_editor):
    """Crea una instancia TipoLaboratorio para 'Electrónica'."""
    tipo_electronica = TipoLaboratorio(
        nombre='Electrónica',
        slug='electronica',
    )
    tipo_electronica.save()


class Migration(migrations.Migration):
    """
    Creación de laboratorios genéricos con tipo asociado.
    """

    dependencies = [
        ('app_reservas', '0022_laboratorio_electronica_a_laboratorio_generico'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLaboratorio',
            fields=[
                (
                    'id',
                    models.AutoField(
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                        verbose_name='ID'
                    )
                ),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Tipos de laboratorio',
                'ordering': ['nombre'],
                'verbose_name': 'Tipo de laboratorio',
            },
        ),
        migrations.AlterModelOptions(
            name='laboratorio',
            options={
                'ordering': ['alias'],
                'verbose_name': 'Laboratorio de Ingeniería',
                'verbose_name_plural': 'Laboratorios de Ingeniería',
            },
        ),
        migrations.RenameField(
            model_name='visortv',
            old_name='laboratorios_electronica',
            new_name='laboratorios',
        ),
        migrations.RunPython(crear_tipo_laboratorio_electronica),
        migrations.AddField(
            model_name='laboratorio',
            name='tipo',
            field=models.ForeignKey(
                to='app_reservas.TipoLaboratorio',
                default=1,
            ),
            preserve_default=False,
        ),
    ]
