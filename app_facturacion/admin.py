from django.contrib import admin

from .models import (
    Area,
    LineaTelefonica,
    PlanLinea,
    TipoConcepto,
    TipoConceptoRegex,
    Usuario,
)


admin.site.register(Area)
admin.site.register(LineaTelefonica)
admin.site.register(PlanLinea)
admin.site.register(TipoConcepto)
admin.site.register(TipoConceptoRegex)
admin.site.register(Usuario)
