from .area import AreaDetailView
from .aula import AulaDetailView
from .cuerpo import CuerpoDetailView
from .index import IndexView
from .laboratorio_electronica import (
    LaboratorioElectronicaDetailView,
    LaboratorioElectronicaListView,
)
from .laboratorio_informatico import (
    LaboratorioInformaticoDetailView,
    LaboratorioInformaticoListView,
)
from .nivel import NivelDetailView
from .proyector_multimedia import (
    ProyectorMultimediaDetailView,
    ProyectorMultimediaListView,
)
from .recurso import recurso_eventos_json
from .solicitud import (
    SolicitudAulaView,
    SolicitudInstalacionSoftwareView,
    SolicitudLaboratorioInformaticoView,
    SolicitudMaterialMultimediaView,
)
from .tv import (
    TvCuerposListView,
    TvVisorCuerposDetailView,
    TvVisorDetailView,
)
