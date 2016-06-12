from .ali import AliVideoconferenciasDetailView
from .area import AreaDetailView
from .aula import AulaDetailView
from .cuerpo import CuerpoDetailView
from .index import IndexView
from .laboratorio import LaboratorioDetailView
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
    SolicitudAliReclamosSugerencias,
    SolicitudAulaView,
    SolicitudInstalacionSoftwareView,
    SolicitudLaboratorioInformaticoView,
    SolicitudMaterialMultimediaView,
)
from .tipo_laboratorio import TipoLaboratorioDetailView
from .tv import (
    TvCuerposListView,
    TvVisorCuerposDetailView,
    TvVisorDetailView,
)
