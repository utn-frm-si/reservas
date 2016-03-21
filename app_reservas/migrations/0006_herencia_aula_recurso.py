# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Creación de herencia, de Aula a Recurso.
    """

    dependencies = [
        ('app_reservas', '0005_data_migration_aula_recurso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='calendar_codigo',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='calendar_color',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='id',
        ),
        migrations.AlterField(
            model_name='aula',
            name='recurso_ptr',
            field=models.OneToOneField(to='app_reservas.Recurso',
                                       primary_key=True,
                                       parent_link=True,
                                       auto_created=True,
                                       serialize=False),
        ),
    ]
