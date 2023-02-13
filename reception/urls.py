from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .documents import generaReportExcelMassa,generaReportExcel
from . import apiviews
from rest_framework import routers

app_name = "reception"

# router = routers.DefaultRouter()
# router.register(r'ingressidip', apiviews.IngressidipViewSet)

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
    
    #Presenze
    path('reception/dashboard_presenze/', views.DashboardPresenzeView.as_view(), name='dashboard_presenze'),
    path('reception/presenze_per_dip/', views.ListaPresenzeDip.as_view(), name='presenze_per_dip'),
    path('reception/presenze_dip/<int:id_dip_ing>', views.ListaGiorniPresenzeDip.as_view(), name='presenze_dip'),
    path('reception/presenze/', views.listaPresenze, name='presenze'),
    path('anticipi-ritardi/download/<str:data>',views.DownloadRitardi.as_view(), name="download_ritardi"),
    
    #Documenti
    path('presenze/download/<str:data>',views.DownloadReport.as_view(), name='download_report'),
    path('presenze/download/excel/<str:data>',generaReportExcelMassa, name='download_excel'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)