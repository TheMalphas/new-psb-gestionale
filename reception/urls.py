from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import documents
from . import apiviews
from rest_framework import routers

app_name = "reception"

urlpatterns= [
    #Api
    # path('api/', include(router.urls)),
    path('api/ingressidip', apiviews.IngressidipListAPIView.as_view(),name="ingressiapi"),
    path('reception/datatables/ingressi_json/',apiviews.ingressi_json,name='ingressi_json'),
    path('reception/datatables/mese_json/',apiviews.ingressi_json_mese,name='mese_json'),
    
    #Start-standard-view
    path('crea-ingresso/<int:pk>',views.CreaIngressoDoppio.as_view(), name="crea-ingresso"),
    path('crea-ingresso2/<int:pk>',views.CreaIngressoDoppio.as_view(), name="crea-ingresso2"),
    path('entrate-qr/',views.EntrateQR.as_view(), name="entrate-qr"),
    
    #DashboardPresenze
    path('reception/datatables/', views.getDashboardCompletaPresenze, name='datatables'),
    path('reception/datatables_mese/', views.getDashboardCompletaPresenzeMese, name='datatables_mese'),
    
    #Presenze
    path('reception/dashboard_presenze/', views.DashboardPresenzeView.as_view(), name='dashboard_presenze'),
    path('reception/presenze_per_dip/', views.listaPresenzeDip, name='presenze_per_dip'),
    path('reception/presenze_dip/<int:id_dip_ing>', views.ListaGiorniPresenzeDip.as_view(), name='presenze_dip'),
    path('reception/presenze_mese/', views.listaPresenzeMese, name='presenze_mese'),
    path('reception/presenze/', views.listaPresenze, name='presenze'),
    path('anticipi-ritardi/download/<str:data>',views.DownloadRitardi.as_view(), name="download_ritardi"),
    
    #Documenti
    path('presenze/download/<str:data>',views.DownloadReport.as_view(), name='download_report'),
    path('presenze/download/excel/',documents.generaReportExcelMassa, name='download_excel'),
    path('presenze/download/excel/mese-corrente/',documents.generaReportExcelMassaMeseCorrente, name='download_excel_mese_corrente'),
    path('presenze/download/excel/settimana-corrente/',documents.generaReportExcelMassaSettimanaCorrente, name='download_excel_settimana_corrente'),    
    path('presenze/download/excel/giorno-corrente/',documents.downloadDynamicPresenze, name='download_excel_giorno_corrente'),    
    path('presenze/download/excel/presenze-dipendente/',documents.downloadAllPresenzeDipendente, name='download_excel_presenze_tutte'),    
    path('presenze/download/excel/presenze-per-dipendente/',documents.downloadAllPresenzePerDipendente, name='download_excel_presenze_per_dipendente'),
    
    
    #QR CODES
    path('gestione/makeqr-uuid/',views.printQR,name="makeqr-uuid"),
    path('gestione/makeqr-standard/',views.printQRStandard,name="makeqr-standard"),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)