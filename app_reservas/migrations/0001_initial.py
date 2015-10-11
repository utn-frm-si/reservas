# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('capacidad', models.PositiveSmallIntegerField()),
                ('calendar_codigo', models.CharField(max_length=100)),
                ('calendar_color', models.CharField(max_length=10)),
                ('archivo_ubicacion', models.FileField(upload_to='ubicacion_aulas', blank=True)),
                ('areas', models.ManyToManyField(to='app_reservas.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Cuerpo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.SmallIntegerField()),
                ('cuerpo', models.ForeignKey(to='app_reservas.Cuerpo')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='nivel',
            field=models.ForeignKey(to='app_reservas.Nivel'),
        ),
    ]
