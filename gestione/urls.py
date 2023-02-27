from django.urls import path
from . import views
from . import apiviews
from .documents_dipendenti import *

app_name = "gestione"

urlpatterns= [
    path('gestione/dashboard/',views.DashboardGestioneView.as_view(), name="dashboard-gestione"),
    path('gestione/dashboard/contratti',views.DashboardContrattiView.as_view(), name="dashboard-contratti"),
    path('gestione/altri-dati/',views.AltriDatiGestioneView.as_view(),name='altri-dati'),
    path('crea-ingresso/<int:pk>',views.CreaIngresso.as_view(), name="crea-ingresso"),
    
    #Trasferte
    path('gestione/richieste-trasferte/', views.gestioneTrasfertePersonale, name="richieste-trasferte"),
    path('gestione/conferma-richieste-trasferte/<int:id_trasferte>', views.RichiesteTrasferteUpdate.as_view(), name="conferma-richieste-trasferte"),
    path('gestione/rifiuta-richieste-trasferte/<int:pk>', views.RichiesteTrasferteRifiuta.as_view(), name="rifiuta-richieste-trasferte"),
    
    #Dashboard
    path('gestione/dipendenti/datatables/', views.getDashboardCompletaDipendenti, name='datatables'),
    path('gestione/dipendenti/datatables_misc/', views.getDashboardDipendentiMisc, name='datatables_misc'),
    path('gestione/contratti/datatables_contratti/', views.getDashboardCompletaContratti, name='datatables_contratti'),
    
    #Dipendenti
    path('gestione/dashboard-richieste/',views.DashboardRichiesteView.as_view(), name="dashboard-richieste"),
    path('gestione/dashboard/responsabili',views.DashboardResponsabiliView.as_view(), name="dashboard-responsabili"),
    path('gestione/dipendenti/',views.listaDipendentiAttivi, name='dipendenti'),
    path('gestione/datatables/contratti_json/',apiviews.contratti_json, name='contratti_json'),
    path('gestione/datatables/dipendenti_json/',apiviews.dipendenti_json, name='dipendenti_json'),
    path('gestione/datatables/dipendenti_misc_json/',apiviews.dipendenti_misc_json, name='datatables_misc_json'),
    path('gestione/anagrafica-dipendente/',views.AnagraficaDipendente.as_view(), name="anagrafica-dipendente"),
    path('gestione/update-anagrafica/modifica/<int:pk>',views.AnagraficaDipendenteUpdate.as_view(), name="update-anagrafica"),
    path('update-stato/modifica/<int:pk>',views.StatoDipendenteUpdate.as_view(), name="update-stato"),
    path('delete-anagrafica/<int:pk>',views.AnagraficaDipendenteDelete.as_view(), name='elimina-anagrafica'),

    #Capi Area
    path('gestione/dashboard/responsabili/capi_area',views.listaCapoArea, name='capi_area'),
    path('gestione/dashboard/responsabili/capi_area/aggiungi_capo_area/',views.AggiungiCapoArea.as_view(), name="aggiungi_capo_area"),
    path('gestione/dashboard/responsabili/capi_area/update_capo_area/<int:pk>',views.CapoAreaUpdate.as_view(), name="update_capo_area"),
    path('gestione/dashboard/responsabili/capi_area/delete_capo_area/<int:pk>',views.CapoAreaDelete.as_view(), name='delete_capo_area'),
    
    #Dirigenti
    path('gestione/dashboard/responsabili',views.DashboardResponsabiliView.as_view(), name="dashboard-responsabili"),
    path('gestione/dashboard/responsabili/dirigenti',views.listaDirigenti, name='dirigenti'),
    path('gestione/dashboard/responsabili/dirigenti/aggiungi_dirigente/',views.AggiungiDirigenti.as_view(), name="aggiungi_dirigente"),
    path('gestione/dashboard/responsabili/dirigenti/update_dirigente/<int:pk>',views.DirigentiUpdate.as_view(), name="update_dirigente"),
    path('gestione/dashboard/responsabili/dirigenti/delete_dirigente/<int:pk>',views.DirigentiDelete.as_view(), name='delete_dirigente'),
    
    #Responsabili
    path('gestione/dashboard/responsabili',views.DashboardResponsabiliView.as_view(), name="dashboard-responsabili"),
    path('gestione/dashboard/responsabili/responsabili',views.listaResponsabili, name='responsabili'),
    path('gestione/dashboard/responsabili/responsabili/aggiungi_responsabile/',views.AggiungiResponsabili.as_view(), name="aggiungi_responsabile"),
    path('gestione/dashboard/responsabili/responsabili/update_responsabile/<int:pk>',views.ResponsabiliUpdate.as_view(), name="update_responsabile"),
    path('gestione/dashboard/responsabili/responsabili/delete_responsabile/<int:pk>',views.ResponsabiliDelete.as_view(), name='delete_responsabile'),
    
    #Responsabili Sede
    path('gestione/dashboard/responsabili',views.DashboardResponsabiliView.as_view(), name="dashboard-responsabili"),
    path('gestione/dashboard/responsabili/responsabili_sede',views.listaResponsabiliSede, name='responsabili_sede'),
    path('gestione/dashboard/responsabili/responsabili_sede/aggiungi_responsabile_sede/',views.AggiungiResponsabiliSede.as_view(), name="aggiungi_responsabile_sede"),
    path('gestione/dashboard/responsabili/responsabili_sede/update_responsabile_sede/<int:pk>',views.ResponsabiliSedeUpdate.as_view(), name="update_responsabile_sede"),
    path('gestione/dashboard/responsabili/responsabili_sede/delete_responsabile_sede/<int:pk>',views.ResponsabiliSedeDelete.as_view(), name='delete_responsabile_sede'),

    #Aree
    path('gestione/altri-dati/aree/',views.ListaAree.as_view(), name='aree'),
    path('crea-nuova-area/',views.AreaCreateView.as_view(), name="crea-nuova-area"),
    path('modifica-area/<int:pk>',views.AreaUpddateView.as_view(), name="modifica-area"),
    path('delete-area/<int:pk>',views.AreaDeleteView.as_view(), name="delete-area"),

 
    #Contratti
    path('gestione/lista_contratti/',views.ListaContrattiListView.as_view(), name='lista_contratti'),
    path('gestione/lista_contratti_scaduti/',views.ListaContrattiScadutiListView.as_view(), name='lista_contratti_scaduti'),
    path('crea-contratto/',views.ContrattiCreateView.as_view(), name="crea-contratto"),
    path('modifica-contratto/<int:pk>',views.ContrattiUpdateView.as_view(), name="modifica-contratto"),


    #Istruzione
    path('gestione/altri-dati/lista-tipo-di-istruzione/',views.ListaIstruzioni.as_view(), name='lista-tipo-di-istruzione'),
    path('aggiungi-tipo-di-istruzione/',views.IstruzioneCreateView.as_view(), name="aggiungi-tipo-di-istruzione"),
    path('modifica-tipo-di-istruzione/<int:pk>',views.IstruzioneUpdateView.as_view(), name="modifica-tipo-di-istruzione"),
    path('delete-tipo-di-istruzione/<int:pk>',views.IstruzioneDeleteView.as_view(), name="delete-tipo-di-istruzione"),

    #Mansione
    path('gestione/altri-dati/lista-mansioni/',views.ListaMansioni.as_view(), name='lista-mansioni'),
    path('aggiungi-tipo-di-mansione/',views.MansioneCreateView.as_view(), name="aggiungi-tipo-di-mansione"),
    path('modifica-mansione/<int:pk>',views.MansioneUpdateView.as_view(), name="modifica-mansione"),
    path('delete-mansione/<int:pk>',views.MansioneDeleteView.as_view(), name="delete-mansione"),

    #Sede
    path('gestione/altri-dati/sedi/',views.ListaSedi.as_view(), name='sedi'),
    path('crea-nuova-sede/',views.SedeCreateView.as_view(), name="crea-nuova-sede"),
    path('modifica-sede/<int:pk>',views.SedeUpdateView.as_view(), name="modifica-sede"),
    path('delete-sede/<int:pk>',views.SedeDeleteView.as_view(), name="delete-sede"),
    
    #Societa
    path('gestione/altri-dati/societa/',views.ListaSocieta2.as_view(), name='societa'),
    path('crea-nuova-societa/',views.SocietaCreateView.as_view(), name="crea-nuova-societa"),
    path('modifica-societa/<int:pk>',views.SocietaUpdateView.as_view(), name="modifica-societa"),
    path('delete-societa/<int:pk>',views.SocietaDeleteView.as_view(), name="delete-societa"),
    
    #Tipo Contratto
    path('gestione/altri-dati/lista-tipo-di-contratti/',views.ListaTipoContratti.as_view(), name='lista-tipo-di-contratti'),
    path('aggiungi-tipo-di-contratto/',views.TipoContrattoCreateView.as_view(), name="aggiungi-tipo-di-contratto"),
    path('modifica-tipo-di-contratto/<int:pk>',views.TipoContrattoUpdateView.as_view(), name="modifica-tipo-di-contratto"),
    path('delete-tipo-di-contratto/<int:pk>',views.TipoContrattoDeleteView.as_view(), name="delete-tipo-di-contratto"),


    #Cedolini
    
    #PercContratti
    path('gestione/altri-dati/lista_perc_contratti/',views.ListaPercContratti, name='lista_perc_contratti'),
    path('aggiungi-perc-contratto/',views.PercContrattiCreateView.as_view(), name="aggiungi-perc-contratto"),
    path('modifica-perc-contratto/<int:pk>',views.PercContrattiUpdateView.as_view(), name="modifica-perc-contratto"),
    path('delete-perc-contratto/<int:pk>',views.PercContrattiDeleteView.as_view(), name="delete-perc-contratto"),
    
    #Presenze
    path('gestione/dettagli-presenze/', views.DettagliPresenze.as_view(), name="dettagli-presenze"),
    path('gestione/dettagli-presenze-area/',views.DettagliAreaPresenze.as_view(),name='dettagli-presenze-area'),
    path('gestione/richieste-accettate/', views.gestioneRichiestePersonale, name="richieste-accettate"),
    path('conferma-richieste-accettate/<int:pk>/conferma-ritorno',views.RichiesteAccettateUpdate.as_view(), name="conferma-richieste-accettate"),
    path('modifica-richieste-accettate/<int:pk>/modifica-richesta',views.ModifcaRichiesteAccettate.as_view(), name="modifica-richieste-accettate"),

    #Documenti
    path('lista-dipendenti-excel/', generaExcelDipendenti, name="lista-dipendenti-excel"),
    path('lista-mansioni-excel/', generaExcelMansioni, name="lista-mansioni-excel"),
    path('lista-contratti-excel/', generaExcelContratti, name="lista-contratti-excel"),
    path('lista-istruzioni-excel/', generaExcelIstruzione, name="lista-istruzioni-excel"),
    path('lista-societa-excel/', generaExcelSocieta, name="lista-societa-excel"),
    path('lista-sedi-excel/', generaExcelSedi, name="lista-sedi-excel"),
    path('lista-aree-excel/', generaExcelArea, name="lista-aree-excel"),
    path('lista-capiarea-excel/', generaExcelCapiArea, name="lista-capiarea-excel"),
    path('lista-responsabili-excel/', generaExcelResponsabili, name="lista-responsabili-excel"),
    path('lista-responsabili-sede-excel/', generaExcelResponsabiliSede, name="lista-responsabili-sede-excel"),
    path('lista-dirigenti-excel/', generaExcelDirigenti, name="lista-dirigenti-excel"),
    path('gestione/richieste-accettate/scarica/<str:data>/<str:dipendente>/', scaricaRichiestePersonale, name="scarica-richieste"),
    path('gestione/lista_contratti/scarica/<str:dipendente>/', generaContratti, name="scarica-contratti"),
]