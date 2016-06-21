# coding=utf-8

from django.db import models


class Cuerpo(models.Model):
    # Atributos
    nombre = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Nombre',
        help_text='Nombre del cuerpo, en caso de que posea. En caso de que no corresponda, dejar '
                  'el campo vacío. Por ejemplo, "Edificio central".',
    )
    numero = models.PositiveSmallIntegerField(
        verbose_name='Número',
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['numero']
        verbose_name = 'Cuerpo'
        verbose_name_plural = 'Cuerpos'

    def __str__(self):
        """
        Representación de la instancia.
        """
        if self.nombre:
            s = '{0!s}: {1!s}'.format(self.get_nombre_corto(),
                                      self.nombre)
        else:
            s = '{0!s}'.format(self.get_nombre_corto())
        return s

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'Cuerpo {0:d}'.format(self.numero)

    def get_niveles(self):
        """
        Retorna el listado de niveles asociados a la instancia.
        """
        return self.nivel_set.all()
