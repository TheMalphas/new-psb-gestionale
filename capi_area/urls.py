from django.urls import path
from capi_area.forms import UpdateEntrata
from . import views

app_name = "capi_area"

urlpatterns= [
    path('capi_area/dashboard-capo-area/', views.dashboardCapoarea, name="dashboard-capo-area"),
    path('capi_area/richieste/', views.capiAreaRichiesteAllList, name="richieste"),
    path('capi_area/richieste/accettate/', views.Capi_AreaRichiesteAccettateList.as_view(), name="accettate"),
    path('capi_area/richieste/rifiutate/', views.Capi_AreaRichiesteRifiutateList.as_view(), name="rifiutate"),
    path('capi_area/richieste/da_revisionare/', views.Capi_AreaRichiesteDaRevisionareList.as_view(), name="da_revisionare"),
    path('capi_area/capi_area-richiesta/<int:id_richiesta>', views.AccettaRichiesta.as_view(), name="gestisci-richiesta"),
    path('capi_area/makeqr/',views.printQR,name="makeqr"),
]