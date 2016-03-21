# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Creación de campo 'slug' para Area.
    """

    dependencies = [
        ('app_reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='slug',
            field=models.SlugField(default='Slug'),
            preserve_default=False,
        ),
    ]
