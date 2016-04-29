# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Renombrado de modelo Bedelia a VisorTv.
    """

    dependencies = [
        ('app_reservas', '0018_ordering_aula_nivel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bedelia',
            new_name='VisorTv',
        ),
    ]
