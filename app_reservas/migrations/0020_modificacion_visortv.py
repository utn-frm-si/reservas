# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Modificación de atributos y relaciones de VisorTv.
    """

    dependencies = [
        ('app_reservas', '0019_bedelia_a_visortv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visortv',
            options={'verbose_name': 'Visor de TV', 'verbose_name_plural': 'Visores de TV'},
        ),
        migrations.AddField(
            model_name='visortv',
            name='nombre',
            field=models.CharField(max_length=100, default='Default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visortv',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visortv',
            name='area',
            field=models.ForeignKey(to='app_reservas.Area'),
        ),
    ]
