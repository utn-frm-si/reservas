# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Creación de modelo Bedelia.
    """

    dependencies = [
        ('app_reservas', '0011_redefinicion_archivo_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedelia',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        verbose_name='ID',
                                        primary_key=True,
                                        serialize=False)),
            ],
            options={
                'verbose_name': 'Bedelía',
                'verbose_name_plural': 'Bedelías',
            },
        ),
        migrations.AddField(
            model_name='bedelia',
            name='area',
            field=models.ForeignKey(to='app_reservas.Area'),
        ),
        migrations.AddField(
            model_name='bedelia',
            name='aulas',
            field=models.ManyToManyField(to='app_reservas.Aula'),
        ),
        migrations.AddField(
            model_name='bedelia',
            name='laboratorios_informatica',
            field=models.ManyToManyField(to='app_reservas.LaboratorioInformatico'),
        ),
    ]
