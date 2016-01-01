# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservas', '0003_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_codigo', models.CharField(max_length=100)),
                ('calendar_color', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Recursos',
                'verbose_name': 'Recurso',
            },
        ),
        migrations.AddField(
            model_name='aula',
            name='recurso_ptr',
            field=models.OneToOneField(to='app_reservas.Recurso', parent_link=True, auto_created=True, default=None, serialize=False, null=True),
            preserve_default=False,
        ),
    ]
