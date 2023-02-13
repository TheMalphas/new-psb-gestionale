from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django import template
register = template.Library()

@register.inclusion_tag('userinfo.html',takes_context = True)
def userinfo(context):
    request = context['request']
    address = request.session['address']
    return {'address':address}


# Create your views here.

def homepage(request):
    utente = "pass"
    return render(request, "base/homepage.html")

class CustomLoginView(LoginView):
    template_name="base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('homepage')