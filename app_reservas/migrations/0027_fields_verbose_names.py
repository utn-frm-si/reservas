# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from ..models import (
    aula,
    imagenCarrusel,
    laboratorio,
    laboratorioInformatico,
)


class Migration(migrations.Migration):
    """
    Creación de 'verbose_name' y 'help_text' para los campos de los modelos existentes.
    """

    dependencies = [
        ('app_reservas', '0026_carrusel_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre'
            ),
        ),
        migrations.AlterField(
            model_name='area',
            name='slug',
            field=models.SlugField(
                verbose_name='Slug',
                help_text='Etiqueta corta que identifica al área, y sólo puede contener letras, '
                          'números, guiones bajos y guiones medios. Generalmente es utilizada '
                          'para las direcciones URL. Por ejemplo, si el nombre del área es '
                          '"Dirección TIC", un slug posible sería "ditic" o "direccion_tic".'
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='archivo_ubicacion',
            field=models.FileField(
                verbose_name='Archivo de ubicación',
                help_text='Archivo que indica la ubicación del aula dentro de la facultad.',
                blank=True,
                upload_to=aula.establecer_destino_archivo_ubicacion
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='areas',
            field=models.ManyToManyField(
                to='app_reservas.Area',
                verbose_name='Áreas a cargo'
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='capacidad',
            field=models.PositiveSmallIntegerField(
                verbose_name='Capacidad',
                help_text='Capacidad del aula. En caso de que no corresponda, introducir "0".'
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='nivel',
            field=models.ForeignKey(
                to='app_reservas.Nivel',
                verbose_name='Nivel'
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre',
                help_text='Nombre del aula, en caso de que posea. En caso de que no corresponda, '
                          'dejar el campo vacío. Por ejemplo, "Aula de dibujo".',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='aula',
            name='numero',
            field=models.PositiveSmallIntegerField(
                verbose_name='Número',
                help_text='Número del aula. En caso de que no corresponda, introducir "0".'
            ),
        ),
        migrations.AlterField(
            model_name='carruselimagenes',
            name='ancho_maximo',
            field=models.PositiveSmallIntegerField(
                verbose_name='Ancho máximo',
                default=800,
                help_text='Ancho máximo del carrusel, medido en píxeles (px).'
            ),
        ),
        migrations.AlterField(
            model_name='carruselimagenes',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre',
                unique=True
            ),
        ),
        migrations.AlterField(
            model_name='carruselimagenes',
            name='slug',
            field=models.SlugField(
                verbose_name='Slug',
                help_text='Etiqueta corta que identifica al carrusel, y sólo puede contener '
                          'letras, números, guiones bajos y guiones medios.',
                unique=True
            ),
        ),
        migrations.AlterField(
            model_name='cuerpo',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre',
                help_text='Nombre del cuerpo, en caso de que posea. En caso de que no '
                          'corresponda, dejar el campo vacío. Por ejemplo, "Edificio central".',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='cuerpo',
            name='numero',
            field=models.PositiveSmallIntegerField(
                verbose_name='Número'
            ),
        ),
        migrations.AlterField(
            model_name='imagencarrusel',
            name='carrusel',
            field=models.ForeignKey(
                to='app_reservas.CarruselImagenes',
                related_name='imagenes',
                verbose_name='Carrusel'
            ),
        ),
        migrations.AlterField(
            model_name='imagencarrusel',
            name='imagen',
            field=models.ImageField(
                verbose_name='Imagen',
                help_text='Archivo de imagen.',
                upload_to=imagenCarrusel.establecer_destino_archivo_imagen
            ),
        ),
        migrations.AlterField(
            model_name='imagencarrusel',
            name='orden',
            field=models.PositiveSmallIntegerField(
                verbose_name='Orden',
                default=1,
                help_text='Orden de la imagen en el carrusel.'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='alias',
            field=models.CharField(
                max_length=10,
                verbose_name='Alias',
                help_text='Alias del laboratorio. Por lo general es una abreviatura del mismo, y '
                          'se utiliza en las direcciones URL. Por ejemplo, el alias del '
                          '"Laboratorio de Electrónica 1" es "LE1".'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='archivo_ubicacion',
            field=models.FileField(
                verbose_name='Archivo de ubicación',
                help_text='Archivo que indica la ubicación del laboratorio dentro de la facultad.',
                blank=True,
                upload_to=laboratorio.establecer_destino_archivo_ubicacion
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='capacidad',
            field=models.PositiveSmallIntegerField(
                verbose_name='Capacidad',
                help_text='Capacidad del laboratorio. En caso de que no corresponda, introducir '
                '"0".'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='nivel',
            field=models.ForeignKey(
                to='app_reservas.Nivel',
                verbose_name='Nivel'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='tipo',
            field=models.ForeignKey(
                to='app_reservas.TipoLaboratorio',
                verbose_name='Tipo'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorioinformatico',
            name='alias',
            field=models.CharField(
                max_length=10,
                verbose_name='Alias',
                help_text='Alias del laboratorio. Por lo general es una abreviatura del mismo, y '
                          'se utiliza en las direcciones URL. Por ejemplo, el alias del '
                          '"Laboratorio Informático Microsoft" es "LIM".'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorioinformatico',
            name='archivo_ubicacion',
            field=models.FileField(
                verbose_name='Archivo de ubicación',
                help_text='Archivo que indica la ubicación del laboratorio dentro de la facultad.',
                blank=True,
                upload_to=laboratorioInformatico.establecer_destino_archivo_ubicacion
            ),
        ),
        migrations.AlterField(
            model_name='laboratorioinformatico',
            name='capacidad',
            field=models.PositiveSmallIntegerField(
                verbose_name='Capacidad',
                help_text='Capacidad del laboratorio. En caso de que no corresponda, introducir '
                '"0".'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorioinformatico',
            name='nivel',
            field=models.ForeignKey(
                to='app_reservas.Nivel',
                verbose_name='Nivel'
            ),
        ),
        migrations.AlterField(
            model_name='laboratorioinformatico',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre'
            ),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='cuerpo',
            field=models.ForeignKey(
                to='app_reservas.Cuerpo',
                verbose_name='Cuerpo'
            ),
        ),
        migrations.AlterField(
            model_name='nivel',
            name='numero',
            field=models.SmallIntegerField(
                verbose_name='Número'
            ),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='calendar_codigo',
            field=models.CharField(
                max_length=100,
                verbose_name='ID del calendario',
                help_text='Puede conocerse al acceder a los detalles del calendario en Google '
                          'Calendar. Su formato habitual es: '
                          '"identificador@group.calendar.google.com". Por ejemplo, un valor '
                          'válido es: "pi4pfu4alasbojtd1v1bj32oc0@group.calendar.google.com".'
            ),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='calendar_color',
            field=models.CharField(
                max_length=10,
                verbose_name='Color del calendario',
                help_text='Color con el que se visualizan los eventos del calendario. Debe estar '
                          'en formato hexadecimal. Por ejemplo, un valor válido es: "#ff8c0a"',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='recursoali',
            name='identificador',
            field=models.CharField(
                max_length=20,
                verbose_name='Identificador',
                help_text='Identificador del recurso. No debe incluirse el prefijo o sufijo '
                          'propio del tipo de recurso. Por ejemplo, si el identificador completo '
                          'es "PM-078-DIE", en este campo debe introducirse "078-DIE", ya que el '
                          'prefijo "PM" es propio del tipo de recurso "Proyector multimedia".'
            ),
        ),
        migrations.AlterField(
            model_name='recursoali',
            name='tipo',
            field=models.ForeignKey(
                to='app_reservas.TipoRecursoAli',
                verbose_name='Tipo'
            ),
        ),
        migrations.AlterField(
            model_name='tipolaboratorio',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre'
            ),
        ),
        migrations.AlterField(
            model_name='tipolaboratorio',
            name='slug',
            field=models.SlugField(
                verbose_name='Slug',
                help_text='Etiqueta corta que identifica al tipo de laboratorio, y sólo puede '
                          'contener letras, números, guiones bajos y guiones medios. Generalmente '
                          'es utilizada para las direcciones URL. Por ejemplo, si el nombre del '
                          'tipo de laboratorio es "Química", un slug posible sería "quimica".'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='is_sufijo',
            field=models.BooleanField(
                verbose_name='¿Es sufijo?',
                default=False,
                help_text='Indica si el prefijo indicado en realidad se utiliza como sufijo.'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='is_visible_navbar',
            field=models.BooleanField(
                verbose_name='Visible en la navbar',
                default=False,
                help_text='Indica si el tipo de recurso se lista dentro de las opciones del ALI, '
                          'en la navbar (barra de navegación superior) del sitio.'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='nombre',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre',
                help_text='Nombre del tipo de recurso, en singular.'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='nombre_plural',
            field=models.CharField(
                max_length=50,
                verbose_name='Nombre en plural',
                help_text='Nombre del tipo de recurso, en plural.'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='prefijo',
            field=models.CharField(
                max_length=5,
                verbose_name='Prefijo',
                help_text='Prefijo del tipo de recurso, utilizado en los identificadores de los '
                          'recursos de dicho tipo. Por ejemplo, el prefijo "PM" es propio del '
                          'tipo de recurso "Proyector multimedia", ya que todos los recursos de '
                          'este tipo tienen un identificador que comienza con "PM".'
            ),
        ),
        migrations.AlterField(
            model_name='tiporecursoali',
            name='slug',
            field=models.SlugField(
                verbose_name='Slug',
                help_text='Etiqueta corta que identifica al tipo de recurso, y sólo puede '
                          'contener letras, números, guiones bajos y guiones medios. Generalmente '
                          'es utilizada para las direcciones URL. Por ejemplo, si el nombre del '
                          'tipo de recurso es "Proyectores multimedia", un slug posible sería '
                          '"proyectores" o "proyectores_multimedia".'
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='area',
            field=models.ForeignKey(
                to='app_reservas.Area',
                verbose_name='Área'
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='aulas',
            field=models.ManyToManyField(
                to='app_reservas.Aula',
                verbose_name='Aulas',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='laboratorios',
            field=models.ManyToManyField(
                to='app_reservas.Laboratorio',
                verbose_name='Laboratorios de Ingeniería',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='laboratorios_informatica',
            field=models.ManyToManyField(
                to='app_reservas.LaboratorioInformatico',
                verbose_name='Laboratorios de Informática',
                blank=True
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='nombre',
            field=models.CharField(
                max_length=100,
                verbose_name='Nombre'
            ),
        ),
        migrations.AlterField(
            model_name='visortv',
            name='slug',
            field=models.SlugField(
                verbose_name='Slug',
                help_text='Etiqueta corta que identifica al visor de TV, y sólo puede contener '
                          'letras, números, guiones bajos y guiones medios. Generalmente es '
                          'utilizada para las direcciones URL. Por ejemplo, si el nombre del '
                          'visor de TV es "Departamento de Sistemas", un slug posible sería '
                          '"sistemas" o "departamento_sistemas".'
            ),
        ),
    ]
