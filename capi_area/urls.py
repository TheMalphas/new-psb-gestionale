from django.urls import path
from capi_area.forms import UpdateEntrata
from . import views

app_name = "capi_area"

urlpatterns= [
    #HTMX
    path('partials/todolist_capo_area',views.assegnaTodo,name="todolist_capo_area"),
    path('capi_area/capi_area_todo',views.listaTodoCapoArea,name="capi_area_todo"),
    path('capi_area/delete_todo_capo_area/<int:pk>',views.delete_todo_capo_area,name="delete_todo_capo_area"),
    path('capi_area/update_todo_capo_area/<int:pk>',views.UpdateTodoCapoArea.as_view(),name="update_todo_capo_area"),
    
    path('capi_area/dashboard-capo-area/', views.dashboardCapoarea, name="dashboard-capo-area"),
    
    #RICHIESTE
    path('capi_area/richieste/', views.capiAreaRichiesteAllList, name="richieste"),
    path('capi_area/richieste-straordinari/', views.capiAreaRichiesteStaordinariList, name="richieste-straordinari"),
    path('capi_area/richieste/accettate/', views.Capi_AreaRichiesteAccettateList.as_view(), name="accettate"),
    path('capi_area/richieste/rifiutate/', views.Capi_AreaRichiesteRifiutateList.as_view(), name="rifiutate"),
    path('capi_area/richieste/da_revisionare/', views.Capi_AreaRichiesteDaRevisionareList.as_view(), name="da_revisionare"),
    
    #GESTIRE
    path('capi_area/richiesta/<int:id_richiesta>', views.AccettaRichiesta.as_view(), name="gestisci-richiesta"),
    path('capi_area/richiesta-straordinari/<int:id_straordinari>', views.AccettaStraordinari.as_view(), name="gestisci_richiesta_straordinari"),
]