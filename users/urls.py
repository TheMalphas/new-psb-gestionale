from django.urls import path,include,reverse_lazy
from .import views 
from reception.documents import generaReportExcel


app_name = "users"

urlpatterns= [
    path('dashboard/', views.UsersView.as_view(), name="dashboard"),
    path('cambia_password/', views.CustomChangePassword.as_view(
        template_name="users/cambia_password.html",
        success_url=reverse_lazy("users:password_cambiata")),name="cambia_password"),
    path('password_cambiata/',views.CustomChangePasswordDone.as_view(), name="password_cambiata"),
    path('richiesta-permesso/',views.SceltaPermessi.as_view(), name='richiesta-permesso'),
    path('dashboard/richiedi-permesso-giorni/',views.RichiesteCreate.as_view(), name='richiedi-permesso-giorni'),
    path('dashboard/richiedi-permesso-orario/',views.RichiesteCreateOrario.as_view(), name='richiedi-permesso-orario'),
    path('richiesta-modifica/<int:id_richiesta>',views.RichiesteUpdate.as_view(), name='richiesta-modifica'),
    path('richiesta-annulla/<int:id_richiesta>',views.RichiesteDelete.as_view(), name='richiesta-annulla'),
    path('dashboard/mie-richieste/',views.RichiesteList.as_view(), name='mie-richieste'),
    path('richiesta/<int:id_richiesta>',views.RichiesteDetail.as_view(), name='richiesta'),
    path('documenti/',views.documentiView, name='documenti'),
    path('scarica_qrcode/',views.printQrUser, name='scarica_qrcode'),
    path('get_qr/',views.get_qr, name='get_qr'),
    path('scarica_report_entrate/', generaReportExcel, name='scarica_report_entrate'),

]