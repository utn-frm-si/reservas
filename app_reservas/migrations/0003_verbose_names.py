# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0002_area_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Área', 'verbose_name_plural': 'Áreas'},
        ),
        migrations.AlterModelOptions(
            name='aula',
            options={'verbose_name': 'Aula', 'verbose_name_plural': 'Aulas'},
        ),
        migrations.AlterModelOptions(
            name='cuerpo',
            options={'verbose_name': 'Cuerpo', 'verbose_name_plural': 'Cuerpos'},
        ),
        migrations.AlterModelOptions(
            name='nivel',
            options={'verbose_name': 'Nivel', 'verbose_name_plural': 'Niveles'},
        ),
        migrations.AlterField(
            model_name='aula',
            name='calendar_color',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
