from django.urls import path, include, reverse_lazy
from .import views 
from reception.documents import generaReportExcel


app_name = "users"
 
urlpatterns= [
    #HTMX
    path('partials/todolist',views.todoUtenteList,name='todolist'),
    path('users/todo_utente',views.todoUtenteList,name="todo_utente"),
    path('users/add_todo',views.add_todo,name="add_todo"),
    path('users/delete_todo/<int:pk>',views.delete_todo,name="delete_todo"),
    path('users/todo_utente/<int:pk>',views.UpdateTodo.as_view(),name="update_todo"),
    
    
    path('dashboard/', views.UsersView.as_view(), name="dashboard"),
    path('cambia_password/', views.CustomChangePassword.as_view(
        template_name="users/cambia_password.html",
        success_url=reverse_lazy("users:password_cambiata")),name="cambia_password"),
    path('password_cambiata/',views.CustomChangePasswordDone.as_view(), name="password_cambiata"),
    path('richiesta-permesso/',views.SceltaPermessi.as_view(), name='richiesta-permesso'),
    
    
    #Dashboard Richieste
    path('dashboard/richiedi-straordinario/',views.AddStraordinariUtente.as_view(), name='richiedi-straordinario'),
    path('dashboard/richiedi-trasferta/',views.AddTrasferteUtente.as_view(), name='richiedi-trasferta'),
    path('dashboard/richiedi-permesso-giorni/',views.RichiesteCreate.as_view(), name='richiedi-permesso-giorni'),
    path('dashboard/richiedi-permesso-orario/',views.RichiesteCreateOrario.as_view(), name='richiedi-permesso-orario'),
    path('dashboard/mie-richieste/',views.richiesteList, name='mie-richieste'),
    
    
    #Straordinari
    path('dashboard/mie-richieste-straordinari/',views.richiesteStraordinariList, name='mie-richieste-straordinari'),
    path('richiesta-straordinario-modifica/<int:id_straordinari>',views.RichiesteStraordinariUpdate.as_view(), name='richiesta-straordinario-modifica'),
    path('richiesta-straordinario-annulla/<int:id_straordinari>',views.RichiesteStraordinariDelete.as_view(), name='richiesta-straordinario-annulla'),
    
    #Trasferte
    path('dashboard/mie-richieste-trasferte/',views.richiesteTrasferteList, name='mie-richieste-trasferte'),
    path('richiesta-trasferta-modifica/<int:id_trasferte>',views.RichiesteTrasferteUpdate.as_view(), name='richiesta-trasferta-modifica'),
    path('richiesta-trasferta-annulla/<int:id_trasferte>',views.RichiesteTrasferteDelete.as_view(), name='richiesta-trasferta-annulla'),
    
    
    #Richieste
    path('richiesta-modifica/<int:id_richiesta>',views.RichiesteUpdate.as_view(), name='richiesta-modifica'),
    path('richiesta-annulla/<int:id_richiesta>',views.RichiesteDelete.as_view(), name='richiesta-annulla'),
    path('richiesta/<int:id_richiesta>',views.RichiesteDetail.as_view(), name='richiesta'),


    #Documenti
    path('documenti/',views.documentiView, name='documenti'),
    path('scarica_qrcode/',views.printQrUser, name='scarica_qrcode'),
    
    
    #QR
    path('get_qr/',views.get_qr, name='get_qr'),
    path('scarica_report_entrate/', generaReportExcel, name='scarica_report_entrate'),

]