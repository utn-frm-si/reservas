# coding=utf-8

from django.template.defaultfilters import slugify

from ..models.aula import Aula
from ..models.laboratorioElectronica import LaboratorioElectronica
from ..models.laboratorioInformatico import LaboratorioInformatico


def get_recursos_asociados(instancia):
    """Retorna todos los recursos asociados a la instancia.

    Genera una lista conformada por diccionarios, uno por cada tipo de recurso asociado. Cada
    uno de estos diccionarios indica los nombres apropiados del tipo de recurso, y una lista
    con las instancias de ese tipo que están relacionadas a la instancia.
    En caso de que la instancia no tenga recursos relacionados de un cierto tipo, el
    diccionario de este tipo no es añadido a la lista.

    Parameters
    ----------
    instancia : object
        Instancia de la cual se obtienen sus recursos asociados.

    Returns
    -------
    list of dicts
        Lista de diccionarios, uno por cada tipo de recurso asociado que presenta al menos una
        instancia relacionada.
    """
    recursos = []
    tipos_recurso = [
        {
            'modelo': Aula,
            'slug': 'aula',
            'metodo': 'get_aulas',
        },
        {
            'modelo': LaboratorioElectronica,
            'slug': 'laboratorio_electronica',
            'metodo': 'get_laboratorios_electronica',
        },
        {
            'modelo': LaboratorioInformatico,
            'slug': 'laboratorio_informatico',
            'metodo': 'get_laboratorios_informatica',
        },
    ]

    # Itera entre los tipos de recursos especificados.
    for tipo in tipos_recurso:
        # Verifica que la instancia cuente con el método de obtención para el tipo actual.
        if hasattr(instancia, tipo['metodo']):
            # Obtiene los recursos asociados del tipo actual.
            elementos = getattr(instancia, tipo['metodo'])()
            # Verifica que se haya obtenido al menos un elemento asociado.
            if elementos:
                # Añade los recursos asociados del tipo actual.
                recursos.append(
                    {
                        'nombre_singular': tipo['modelo']._meta.verbose_name,
                        'nombre_plural': tipo['modelo']._meta.verbose_name_plural,
                        'slug': tipo['slug'],
                        'elementos': elementos,
                    }
                )

    return recursos
