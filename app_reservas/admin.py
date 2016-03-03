from django.contrib import admin

from .models import (
    Area,
    Aula,
    Cuerpo,
    LaboratorioInformatico,
    Nivel,
    ProyectorMultimedia,
)


admin.site.register(Area)
admin.site.register(Aula)
admin.site.register(Cuerpo)
admin.site.register(LaboratorioInformatico)
admin.site.register(Nivel)
admin.site.register(ProyectorMultimedia)
