from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from .models import AnaDipendenti, AuthUser
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='first_login/')
def homepage(request):
    return render(request,"base/homepage.html")

class CustomLoginView(LoginView):
    template_name="base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('users:dashboard')

class FirstLogin(LoginView):
    template_name="base/first_login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users:dashboard')

class CustomLogoutView(LogoutView):
    template_name="base/logout.html"
    redirect_authenticated_user = True
    login_url = 'base/first_login.html'
        
    def get_success_url(self):
        return reverse_lazy('base:first_login')