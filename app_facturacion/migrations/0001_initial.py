# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import regex_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Áreas',
                'verbose_name': 'Área',
            },
        ),
        migrations.CreateModel(
            name='LineaTelefonica',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero', models.PositiveIntegerField()),
                ('descripcion', models.CharField(max_length=50, blank=True)),
                ('area', models.ForeignKey(to='app_facturacion.Area')),
            ],
            options={
                'verbose_name_plural': 'Líneas telefónicas',
                'verbose_name': 'Línea telefónica',
            },
        ),
        migrations.CreateModel(
            name='PlanLinea',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cantidad_total', models.PositiveIntegerField()),
                ('cantidad_cubierta', models.PositiveIntegerField()),
                ('linea', models.ForeignKey(to='app_facturacion.LineaTelefonica')),
            ],
            options={
                'verbose_name_plural': 'Planes de línea',
                'verbose_name': 'Plan de línea',
            },
        ),
        migrations.CreateModel(
            name='TipoConcepto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tarifa', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Tipos de concepto',
                'verbose_name': 'Tipo de concepto',
            },
        ),
        migrations.CreateModel(
            name='TipoConceptoRegex',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('regex', regex_field.fields.RegexField(max_length=128)),
                ('tipo_concepto', models.ForeignKey(to='app_facturacion.TipoConcepto')),
            ],
            options={
                'verbose_name_plural': 'Expresiones regulares para tipo de concepto',
                'verbose_name': 'Expresión regular para tipo de concepto',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'verbose_name': 'Usuario',
            },
        ),
        migrations.AddField(
            model_name='planlinea',
            name='tipo_concepto',
            field=models.ForeignKey(to='app_facturacion.TipoConcepto'),
        ),
        migrations.AddField(
            model_name='lineatelefonica',
            name='usuario',
            field=models.ForeignKey(to='app_facturacion.Usuario'),
        ),
    ]
