from django.urls import path, include, reverse_lazy
from .views import CustomLoginView, FirstLogin, CustomLogoutView
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views

app_name = "base"

urlpatterns= [
    path("",views.homepage, name='homepage'),
    path("first_login/",FirstLogin.as_view(), name='first_login'),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="base/resetta_password.html")
         , name="reset_password"),
    path('password_reset_sent',auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_mandata.html")
         , name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password_resettata.html"),
         name="password_reset_complete"),
]
