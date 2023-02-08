from django.urls import path
from . import views
from .documents_dipendenti import *

app_name = "gestione"

urlpatterns= [
    path('gestione/dashboard/',views.DashboardGestioneView.as_view(), name="dashboard-gestione"),
    path('gestione/altri-dati/',views.AltriDatiGestioneView.as_view(),name='altri-dati'),
    path('crea-ingresso/<int:pk>',views.CreaIngresso.as_view(), name="crea-ingresso"),
    
    #Dipendenti
    path('gestione/dipendenti/',views.ListaDipendentiAttivi.as_view(), name='dipendenti'),
    path('gestione/dipendenti-cessati/',views.ListaDipendentiCessati.as_view(), name='dipendenti-cessati'),
    path('gestione/dipendenti-sospesi/',views.ListaDipendentiSospesi.as_view(), name='dipendenti-sospesi'),
    path('gestione/dipendente/<int:data>',views.ListaDipendentiAttivi.as_view(), name='dipendenti'),
    path('gestione/anagrafica-dipendente/',views.AnagraficaDipendente.as_view(), name="anagrafica-dipendente"),
    path('gestione/update-anagrafica/modifica/<int:pk>',views.AnagraficaDipendenteUpdate.as_view(), name="update-anagrafica"),
    path('delete-anagrafica/<int:pk>',views.AnagraficaDipendenteDelete.as_view(), name='elimina-anagrafica'),

    #Capi Area
    path('gestione/capi_area/',views.ListaCapoArea.as_view(), name='capi_area'),
    path('aggiungi_capo_area/',views.AggiungiCapoArea.as_view(), name="aggiungi_capo_area"),
    path('update_capo_area/<int:pk>',views.CapoAreaUpdate.as_view(), name="update_capo_area"),

    #Dirigenti
    path('aggiungi_dirigente/',views.AggiungiDirigenti.as_view(), name="aggiungi_dirigente"),
    path('update_dirigente/<int:pk>',views.DirigentiUpdate.as_view(), name="update_dirigente"),
    
    #Responsabili
    path('aggiungi_responsabile/',views.AggiungiResponsabili.as_view(), name="aggiungi_responsabile"),
    path('update_responsabile/<int:pk>',views.ResponsabiliUpdate.as_view(), name="update_responsabile"),
    
    #Responsabili Sede
    path('aggiungi_responsabile_sede/',views.AggiungiResponsabiliSede.as_view(), name="aggiungi_responsabile_sede"),
    path('update_responsabile_sede/<int:pk>',views.ResponsabiliSedeUpdate.as_view(), name="update_responsabile_sede"),

    #Aree
    path('gestione/altri-dati/aree/',views.ListaAree.as_view(), name='aree'),
    path('crea-nuova-area/',views.AreaCreateView.as_view(), name="crea-nuova-area"),
    path('modifica-area/<int:pk>',views.AreaUpddateView.as_view(), name="modifica-area"),

    #Contratti
    path('gestione/lista_contratti/',views.ListaContrattiListView.as_view(), name='lista_contratti'),
    path('crea-contratto/',views.ContrattiCreateView.as_view(), name="crea-contratto"),
    path('modifica-contratto/<int:pk>',views.ContrattiUpdateView.as_view(), name="modifica-contratto"),

    #Istruzione
    path('gestione/altri-dati/lista-tipo-di-istruzione/',views.ListaIstruzioni.as_view(), name='lista-tipo-di-istruzione'),
    path('aggiungi-tipo-di-istruzione/',views.IstruzioneCreateView.as_view(), name="aggiungi-tipo-di-istruzione"),
    path('modifica-tipo-di-istruzione/<int:pk>',views.IstruzioneUpdateView.as_view(), name="modifica-tipo-di-istruzione"),

    #Mansione
    path('gestione/altri-dati/lista-mansioni/',views.ListaMansioni.as_view(), name='lista-mansioni'),
    path('aggiungi-tipo-di-mansione/',views.MansioneCreateView.as_view(), name="aggiungi-tipo-di-mansione"),
    path('modifica-mansione/<int:pk>',views.MansioneUpdateView.as_view(), name="modifica-mansione"),

    #Sede
    path('gestione/altri-dati/sedi/',views.ListaSedi.as_view(), name='sedi'),
    path('crea-nuova-sede/',views.SedeCreateView.as_view(), name="crea-nuova-sede"),
    path('modifica-sede/<int:pk>',views.SedeUpdateView.as_view(), name="modifica-sede"),
    
    #Societa
    path('gestione/altri-dati/societa/',views.ListaSocieta2.as_view(), name='societa'),
    path('crea-nuova-societa/',views.SocietaCreateView.as_view(), name="crea-nuova-societa"),
    path('modifica-societa/<int:pk>',views.SocietaUpdateView.as_view(), name="modifica-societa"),
    
    #Tipo Contratto
    path('gestione/altri-dati/lista-tipo-di-contratti/',views.ListaTipoContratti.as_view(), name='lista-tipo-di-contratti'),
    path('aggiungi-tipo-di-contratto/',views.TipoContrattoCreateView.as_view(), name="aggiungi-tipo-di-contratto"),
    path('modifica-tipo-di-contratto/<int:pk>',views.TipoContrattoUpdateView.as_view(), name="modifica-tipo-di-contratto"),

    #Cedolini
    path('gestione/dipendente/<int:data>',views.ListaDipendentiAttivi.as_view(), name='dipendenti'),
    
    #PercContratti
    path('gestione/altri-dati/lista_percentuali_contratti/',views.ListaPercContratti, name='lista_percentuali_contratti'),
    path('aggiungi-perc-contratto/',views.PercContrattiCreateView.as_view(), name="aggiungi-perc-contratto"),
    path('modifica-perc-contratto/<int:pk>',views.PercContrattiUpdateView.as_view(), name="modifica-perc-contratto"),
    
    #Presenze
    path('gestione/dettagli-presenze/', views.DettagliPresenze.as_view(), name="dettagli-presenze"),
    path('gestione/dettagli-presenze-area/',views.DettagliAreaPresenze.as_view(),name='dettagli-presenze-area'),
    path('gestione/richieste-accettate/', views.GestioneRichiestePersonale.as_view(), name="richieste-accettate"),
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

]