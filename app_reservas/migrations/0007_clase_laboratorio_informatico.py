# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0006_herencia_aula_recurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratorioInformatico',
            fields=[
                ('recurso_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app_reservas.Recurso')),
                ('nombre', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=10)),
                ('capacidad', models.PositiveSmallIntegerField()),
                ('nivel', models.ForeignKey(to='app_reservas.Nivel')),
            ],
            options={
                'verbose_name_plural': 'Laboratorios informáticos',
                'verbose_name': 'Laboratorio informático',
            },
            bases=('app_reservas.recurso',),
        ),
    ]
