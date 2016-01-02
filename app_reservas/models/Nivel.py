# coding=utf-8

from django.db import models


class Nivel(models.Model):
    # Atributos
    numero = models.SmallIntegerField()
    # Relaciones
    cuerpo = models.ForeignKey('Cuerpo')

    # Representación del objeto
    def __str__(self):
        return '%s - %s' % (self.get_nombre_corto(), self.cuerpo)

    def get_nombre_corto(self):
        return 'Nivel %s' % self.numero

    def get_aulas(self):
        return self.aula_set.order_by('numero', 'nombre')

    def get_laboratorios_informaticos(self):
        return self.laboratorioinformatico_set.order_by('alias')

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
