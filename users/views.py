from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect,FileResponse, JsonResponse, Http404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Richieste, AuthUser, AnaDipendenti, CapoArea, Permessi, RichiesteAccettate, AppoggioVerificaQr
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from datetime import time, datetime, timedelta
from dateutil.relativedelta import relativedelta
from django import forms
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .forms import CreateRichiestaForm, CreateRichiestaOrarioForm
import qrcode

# Create your views here.

@login_required
def documentiView(request):
    listaMesi = ["Gennaio","Febbraio", "Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]
    context = {'mesi':listaMesi}
    return render(request,'users/documenti.html', context)
    
@login_required
def get_qr(request):
    dip = AnaDipendenti.objects.get(user_id=request.user.id)
    uuid = AppoggioVerificaQr.objects.get(id_dipendente=dip.id_dip)
    response = HttpResponse(content_type='image/png')
    dipname = dip.nome
    dipsurname = dip.cognome
    fl = f'{dipname} {dipsurname}'
    response['Content-Disposition'] = f'fattachment; filename= "QR CODE - {fl}".png'
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(uuid.uuid_qr)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(response)
    return response


@login_required
def printQrUser(request):
    user = request.user.pk
    dip=AnaDipendenti.objects.get(user_id=user)
    uuid = AppoggioVerificaQr.objects.get(id_dipendente=dip.id_dip)
    
    if request.method == 'POST':
        input_data = request.POST['get_qr']
        uuid = AppoggioVerificaQr.objects.get(id_dipendente=input_data)
        response = HttpResponse(content_type='image/png')
        dipname = dip.nome
        dipsurname = dip.cognome
        fl = f'{dipname} {dipsurname}'
        response['Content-Disposition'] = f'fattachment; filename= "QR CODE - {fl}".png'
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(uuid.uuid_qr)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(response)
        return response
    
    return render(request,'capi_area/makeqr.html')


class CustomChangePassword(PasswordChangeView):
    template_name="users/cambia_password.html"
    success_url = reverse_lazy("users:password_cambiata")

class CustomChangePasswordDone(PasswordChangeDoneView):
    template_name= "users/password_cambiata.html"
    fields = "__all__"

class UsersView(LoginRequiredMixin, View):
    template_name= "users/dashboard.html"
    login_url = '/first_login/'


    def get_context_data(self, **kwargs):
        context = {}
        dip = AnaDipendenti.objects.get(user_id=self.request.user.pk)
        richieste = Richieste.objects.filter(id_dipendente_richiesta=dip.id_dip)
        richiesteList = [el.id_richiesta for el in richieste]
        numeroPermessiAttiviGiorno = RichiesteAccettate.objects.filter(id_richieste__in=richieste,ora_inizio_permesso__isnull=False).count()
        numeroPermessiAttiviOre = RichiesteAccettate.objects.filter(id_richieste__in=richieste,ora_inizio_permesso=None).count()
        permessiInAttesa = richieste.count()
        context["numeroPermessiAttiviGiorno"] = numeroPermessiAttiviGiorno
        context["numeroPermessiAttiviOre"] = numeroPermessiAttiviOre
        context["permessiInAttesa"] = permessiInAttesa

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user= AuthUser.objects.get(id=self.request.user.pk)
        context["utente"] = user
        return render(request, self.template_name, context)


class SceltaPermessi(LoginRequiredMixin, TemplateView):
    template_name = "users/richiesta-permesso.html"

    def get(self, request, *args, **kwargs):
        
        try:
            if request.GET.get("permesso"):
                return redirect('users/richiedi-permesso-giorni.html')
            elif request.GET.get("permesso-orario"):
                return redirect('users/richiedi-permesso-orario.html')
        except:
            pass
    
        return render(request, self.template_name)

class RichiesteCreate(LoginRequiredMixin,CreateView):
    model= Richieste
    form_class = CreateRichiestaForm
    template_name = 'users/richiedi-permesso-giorni.html'
    success_url= reverse_lazy('users:mie-richieste')
    
    def form_valid(self, form):
        form.instance.id_user=AuthUser.objects.get(id=self.request.user.pk)
        form.instance.id_dipendente_richiesta = AnaDipendenti.objects.get(user_id=self.request.user.pk)
        form.instance.nominativo = AuthUser.objects.values_list("first_name","last_name").get(id=self.request.user.pk)
        form.instance.nominativo = form.instance.nominativo[0] + " " + form.instance.nominativo[1]
        if form.is_valid():
            
            return super(RichiesteCreate, self).form_valid(form)

class RichiesteCreateOrario(LoginRequiredMixin,CreateView):
    model= Richieste
    form_class = CreateRichiestaOrarioForm
    template_name = 'users/richiedi-permesso-orario.html'
    success_url= reverse_lazy('users:mie-richieste')
    
    def form_valid(self, form):
        form.instance.id_user=AuthUser.objects.get(id=self.request.user.pk)
        form.instance.id_dipendente_richiesta = AnaDipendenti.objects.get(user_id=self.request.user.pk)
        form.instance.nominativo = AuthUser.objects.values_list("first_name","last_name").get(id=self.request.user.pk)
        form.instance.nominativo = form.instance.nominativo[0] + " " + form.instance.nominativo[1]
        form.instance.a_giorno_richiesta = form.instance.da_giorno_richiesta
        if form.is_valid():
            return super(RichiesteCreateOrario, self).form_valid(form)

@login_required
def richiesteList(request):
    template_name = "users/mie-richieste.html"
    query = ""
    
    today = datetime.now()
    dip = AnaDipendenti.objects.get(user_id=request.user.pk)
    queryset = Richieste.objects.filter(id_user=request.user.pk).order_by("-timestamp")
    accettate = queryset.filter(stato=1,a_giorno_richiesta__gte=today).count()
    rifiutate = queryset.filter(stato=0,a_giorno_richiesta__gte=today).count()
    inAttesa = queryset.filter(stato=None).count()
    
    return render(request,template_name,{'richieste':queryset,'accettate':accettate,'rifiutate':rifiutate,'inAttesa':inAttesa})



def get(self,request,*args,**kwargs):
    twoMonthsAgo = datetime.now() + relativedelta(months=2)
    mostra = request.GET.get("mostratutto")
    if mostra is None:
        queryset = Richieste.objects.filter(id_user=self.request.user.pk, a_giorno_richiesta__gte=twoMonthsAgo).order_by("-timestamp")
    else:
        try:
            mostra = int(mostra)
            if mostra == 0:
                queryset = Richieste.objects.filter(id_user=self.request.user.pk, a_giorno_richiesta__gte=twoMonthsAgo).order_by("-timestamp")
            else:
                queryset = Richieste.objects.filter(id_user=self.request.user.pk).order_by("-timestamp")
        except ValueError:
            return HttpResponseBadRequest("Invalid 'mostratutto' parameter. Expecting a number.")

    return queryset


class RichiesteUpdate(LoginRequiredMixin,UpdateView):
    model= Richieste
    template_name = "users/richiesta-modifica.html"
    context_object_name = "richiesta"
    form_class = CreateRichiestaForm
    success_url= reverse_lazy('users:mie-richieste')
    # fields= ('da_giorno_richiesta', 'a_giorno_richiesta', 'urgente', 'note_richiesta')

    def get_object(self):
        id_richiesta = self.kwargs.get("id_richiesta")
        return get_object_or_404(Richieste, id_richiesta=id_richiesta)


class RichiesteDelete(LoginRequiredMixin, DeleteView):
    model = Richieste
    template_name = "users/richiesta-annulla.html"
    context_object_name = "richiesta"
    success_url= reverse_lazy('users/mie-richieste')
    
    def get_object(self):
        id_richiesta = self.kwargs.get("id_richiesta")
        return get_object_or_404(Richieste, id_richiesta=id_richiesta)
    
    def get_success_url(self):
        return reverse('users:mie-richieste')


class RichiesteDetail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model= Richieste
    context_object_name = "richiesta"
    template_name = "users/richiesta.html"
    permission_required = ('richieste.add_choice', 'richieste.change_choice')
    
    def get_object(self):
        id_richiesta = self.kwargs.get("id_richiesta")
        return get_object_or_404(Richieste, id_richiesta=id_richiesta)
    
    def test_func(self):
        return
    
    def handle_no_permission(self):
        return redirect('users/richieste')
