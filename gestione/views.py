from django.apps import AppConfig
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, date, timedelta
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.db.models import Q
from django.views import View
from django.contrib import messages
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.urls import reverse, reverse_lazy
from .models import AnaDipendenti,Area,CapoArea,Contratti,Dirigenti,Istruzione,Ingressidip,ListaSocieta
from .models import Mansione,Mese,Permessi,Responsabili,ResponsabiliSede,Richieste,RichiesteAccettate,Sede,Sesso,Societa, PercentualiContratto,TipoContratto
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django import forms
from .forms import *
from datetime import time, datetime, timedelta
from django.contrib.auth.views import redirect_to_login
from django.db.models import Count
import qrcode
import traceback 


class DashboardGestioneView(LoginRequiredMixin, PermissionRequiredMixin,View):
    template_name= "gestione/dashboard-gestione.html"
    permission_required = 'gestione.change_anadipendenti'
    today = datetime.now().date()
    def get(self, request, *args, **kwargs):
        dipendenti = AnaDipendenti.objects.filter(stato="Attivo")
        context = {'dipendenti':dipendenti.count()}
        
        sedes= Sede.objects.all()
        listaSedi = []
        for sede in sedes:
            element = dipendenti.filter(sede=sede.id_sede).count()
            tuplaSede = (f'{(sede.nome_sede).replace("/"," ")}', element)
            listaSedi.append(tuplaSede)
        context["sedi"] = listaSedi
        
        societas= Societa.objects.all()
        listaSocieta = []
        for societa in societas:
            element = dipendenti.filter(societa=societa.id_societa).count()
            tuplaSocieta = (f'{(societa.nome_societa).replace("/"," ").title()}', element)
            listaSocieta.append(tuplaSocieta)
        context["societa"] = listaSocieta
        
        areas = Area.objects.all()
        listaAree = []
        for area in areas:
            element = dipendenti.filter(area=area.id_area).count()
            tuplaArea = (f'{(area.nome_area).replace("/","")}', element)
            listaAree.append(tuplaArea)
        context["aree"] = listaAree
        return render(request, self.template_name,context)


class AltriDatiGestioneView(LoginRequiredMixin, PermissionRequiredMixin,View):
    template_name= "gestione/altri-dati.html"
    permission_required = 'gestione.change_anadipendenti'
    
    def get(self, request, *args, **kwargs):
        aree = Area.objects.all().count()
        context = {'areeNumero':aree}
        context["societaNumero"] = Societa.objects.all().count()
        context["sediNumero"] = Sede.objects.all().count()
        context["tipoContrattiNumero"] = TipoContratto.objects.all().count()
        context["mansioniNumero"] = Mansione.objects.all().count()
        context["percContrattiNumero"] = PercentualiContratto.objects.all().count()
        context["istruzioneNumero"] = Istruzione.objects.all().count()

        return render(request, self.template_name, context)

#CAPOAREA

class ListaCapoArea(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CapoArea
    context_object_name = "capiarea"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/capi_area.html'
    form_class = CapoAreaForm
    paginate_by = 50
    query = ""
    
    def get_context_data(self, **kwargs):
        listaAree = [9,23,24,46]
        context = super(ListaCapoArea, self).get_context_data(**kwargs)
        queryDir = Dirigenti.objects.all().order_by("nomecompleto")
        queryResp = Responsabili.objects.all().order_by("nomecompleto")
        queryRespSede = ResponsabiliSede.objects.all().order_by("nomecompleto")
        queryRefer = AnaDipendenti.objects.filter(stato='Attivo',area=46).order_by("cognome")
        context['dirigenti'] = queryDir
        context['respo'] = queryResp
        context['resposede'] = queryRespSede
        context['refer'] = queryRefer
        context["form"] = self.form_class()
        
        if self.query != "":
            data=self.query
            queryDir = Dirigenti.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['dirigenti'] = queryDir
            queryResp = Responsabili.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['respo'] = queryResp
            queryRespSede = ResponsabiliSede.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['resposede'] = queryRespSede
            queryRefer = AnaDipendenti.objects.filter(Q(stato='Attivo',area=46,cognome__icontains=data)|Q(stato='Attivo',area=46,nome__icontains=data)).order_by("cognome")
            context['refer'] = queryRefer
            return context
        else:
            data = self.query
            queryDir = Dirigenti.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['dirigenti'] = queryDir
            queryResp = Responsabili.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['respo'] = queryResp
            queryRespSede = ResponsabiliSede.objects.filter(Q(nomecompleto__icontains=data)).order_by("nomecompleto")
            context['resposede'] = queryRespSede
            queryRefer = AnaDipendenti.objects.filter(Q(stato='Attivo',area=46,cognome__icontains=data)|Q(stato='Attivo',area=46,nome__icontains=data)).order_by("cognome")
            context['refer'] = queryRefer
            return context

    def get_queryset(self):
        queryset = CapoArea.objects.all().order_by("nomecompleto")
        listaGets = ['capiarea','dirigenti','responsabili','responsabilisede','referenti']
        self.query = ""
        for element in listaGets:
            if self.request.GET.get(element) or self.request.GET.get(element) in listaGets:
                self.query = self.request.GET.get(element)
                break
        if self.query:
            queryset = CapoArea.objects.filter(Q(nomecompleto__icontains=self.query)).order_by("nomecompleto")
        return queryset


class AggiungiCapoArea(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= CapoArea
    form_class = CapoAreaForm
    template_name = 'gestione/aggiungi_capo_area.html'
    permission_required = 'gestione.change_anadipendenti'
    success_url= reverse_lazy('gestione:capi_area')
    success_message = 'Capo area creato con successo.'
    error_meesage = "Errore nel creare il capo area, controlla che tutti i campi siano corretti."
    
    def form_valid(self, form):
        dipendente = form.cleaned_data['dipendenti']
        dipendente_id = dipendente.pk
        dip = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp = form.save()
        temp.id_dipendente = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp.nomecompleto = dip.cognome.title()+" "+dip.nome.title()
        temp.save()
        return super().form_valid(form)      


class CapoAreaUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= CapoArea
    form_class = CapoAreaUpdateForm
    template_name = "gestione/update_capo_area.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "dipendente"
    success_url= reverse_lazy('gestione:capi_area')

#DIRIGENTI

class ListaDirigenti(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Dirigenti
    context_object_name = "dirigenti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/dirigenti.html'
    form_class = DirigentiForm
    paginate_by = 10
    query = ""
    

    def get_queryset(self):
        queryset = Dirigenti.objects.all().order_by("nomecompleto")
        if self.request.GET.get('dirigenti'):
            self.query = self.request.GET.get('dirigenti') or ""
        if self.query:
            queryset = Dirigenti.objects.filter(Q(nomecompleto__icontains=self.query)).order_by("nomecompleto")
        return queryset



class AggiungiDirigenti(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Dirigenti
    form_class = DirigentiForm
    template_name = 'gestione/aggiungi_dirigente.html'
    permission_required = 'gestione.change_anadipendenti'
    success_url= reverse_lazy('gestione:dirigenti')
    success_message = 'Capo area creato con successo.'
    error_meesage = "Errore nel creare il dirigente, controlla che tutti i campi siano corretti."
    
    def form_valid(self, form):
        dipendente = form.cleaned_data['dipendenti']
        dipendente_id = dipendente.pk
        dip = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp = form.save()
        temp.id_dipendente = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp.nomecompleto = dip.cognome.title()+" "+dip.nome.title()
        temp.save()
        return super().form_valid(form)      


class DirigentiUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Dirigenti
    form_class = DirigentiUpdateForm
    template_name = "gestione/update_dirigente.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "dirigente"
    success_url= reverse_lazy('gestione:dirigenti')

#RESPONSABILI

class ListaResponsabili(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Responsabili
    context_object_name = "responsabili"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/responsabili.html'
    form_class = ResponsabiliForm
    paginate_by = 10
    query = ""
    

    def get_queryset(self):
        queryset = Responsabili.objects.all().order_by("nomecompleto")
        if self.request.GET.get('responsabili'):
            self.query = self.request.GET.get('responsabili') or ""
        if self.query:
            queryset = Responsabili.objects.filter(Q(nomecompleto__icontains=self.query)).order_by("nomecompleto")
        return queryset


class AggiungiResponsabili(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Responsabili
    form_class = ResponsabiliForm
    template_name = 'gestione/aggiungi_responsabile.html'
    permission_required = 'gestione.change_anadipendenti'
    success_url= reverse_lazy('gestione:responsabili')
    success_message = 'Capo area creato con successo.'
    error_meesage = "Errore nel creare il responsabile, controlla che tutti i campi siano corretti."
    
    def form_valid(self, form):
        dipendente = form.cleaned_data['dipendenti']
        dipendente_id = dipendente.pk
        dip = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp = form.save()
        temp.id_dipendente = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp.nomecompleto = dip.cognome.title()+" "+dip.nome.title()
        temp.save()
        return super().form_valid(form)      


class ResponsabiliUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Responsabili
    form_class = ResponsabiliUpdateForm
    template_name = "gestione/update_responsabile.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "responsabile"
    success_url= reverse_lazy('gestione:capi_area')


#RESPONSABILI SEDE


class ListaResponsabiliSede(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ResponsabiliSede
    context_object_name = "responsabilisede"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/responsabili_sede.html'
    form_class = ResponsabiliSedeForm
    paginate_by = 10
    query = ""
    

    def get_queryset(self):
        queryset = ResponsabiliSede.objects.all().order_by("nomecompleto")
        if self.request.GET.get('responsabilisede'):
            self.query = self.request.GET.get('responsabilisede') or ""
        if self.query:
            queryset = ResponsabiliSede.objects.filter(Q(nomecompleto__icontains=self.query)).order_by("nomecompleto")
        return queryset



class AggiungiResponsabiliSede(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= ResponsabiliSede
    form_class = ResponsabiliSedeForm
    template_name = 'gestione/aggiungi_responsabile_sede.html'
    permission_required = 'gestione.change_anadipendenti'
    success_url= reverse_lazy('gestione:responsabili_sede')
    success_message = 'Capo area creato con successo.'
    error_meesage = "Errore nel creare il capo area, controlla che tutti i campi siano corretti."

    def form_valid(self, form):
        dipendente = form.cleaned_data['dipendenti']
        dipendente_id = dipendente.pk
        dip = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp = form.save()
        temp.id_dipendente = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp.nomecompleto = dip.cognome.title()+" "+dip.nome.title()
        temp.save()
        return super().form_valid(form)      


class ResponsabiliSedeUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= ResponsabiliSede
    form_class = ResponsabiliSedeUpdateForm
    template_name = "gestione/update_responsabile_sede.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "responsabilesede"
    success_url= reverse_lazy('gestione:responsabili_sede')


#DIPENDENTI

class ListaDipendentiAttivi(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AnaDipendenti
    context_object_name = "dipendenti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/dipendenti.html'
    paginate_by = 300
    query = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dipendentiAttivi"] = AnaDipendenti.objects.filter(stato="Attivo").count()
        context["dipendentiCessati"] = AnaDipendenti.objects.filter(stato="Cessato").count()
        context["dipendentiSospesi"] = AnaDipendenti.objects.filter(stato="Sospeso").count()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context


    def get_queryset(self):
        queryset = AnaDipendenti.objects.filter(stato="Attivo").order_by("cognome")
        print(self.request.GET)
        if self.request.GET.get("getDip") or "":
            self.query = self.request.GET.get("getDip") or "" 
            if self.query:
                queryset = AnaDipendenti.objects.all().filter(Q(nome__icontains=self.query) | Q(cognome__icontains=self.query)).order_by("cognome")
                return queryset
        # elif self.request.GET.get("area") or "":
        #     self.query = self.request.GET.get("area") or "" 
        #     if self.query:
        #         queryset = AnaDipendenti.objects.all().filter(Q(area=self.query)).order_by("cognome")
        #         return queryset
        # elif self.request.GET.get("sede") or "":
        #     self.query = self.request.GET.get("sede") or "" 
        #     if self.query:
        #         queryset = AnaDipendenti.objects.all().filter(Q(sede=self.query)).order_by("cognome")
        #         return queryset
        # elif self.request.GET.get("societa") or "":
        #     self.query = self.request.GET.get("societa") or "" 
        #     if self.query:
        #         queryset = AnaDipendenti.objects.all().filter(Q(societa=self.query)).order_by("cognome")
        #         return queryset
        # elif self.request.GET.get("contratto") or "":
        #     self.query = self.request.GET.get("contratto") or "" 
        #     if self.query:
        #         queryset = AnaDipendenti.objects.all().filter(Q(tipo_contratto=self.query)).order_by("cognome")
        #         return queryset
        return queryset
    
    
    
class ListaDipendentiCessati(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AnaDipendenti
    context_object_name = "dipendenti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/dipendenti-cessati.html'
    paginate_by = 50
    query = ""


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.query != "":
            data = self.query
            return context
        else:
            data = self.query
            return context

    def get_queryset(self):
        queryset = AnaDipendenti.objects.filter(stato="Cessato").order_by("cognome")
        self.query = self.request.GET.get("dip") or ""
        if self.query:
            queryset = AnaDipendenti.objects.filter(stato="Cessato").filter(Q(nome__icontains=self.query) | Q(cognome__icontains=self.query)).order_by("cognome")
            return queryset
        return queryset
    
    
class ListaDipendentiSospesi(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AnaDipendenti
    context_object_name = "dipendenti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/dipendenti-sospesi.html'
    paginate_by = 50
    query = ""


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context

    def get_queryset(self):
        queryset = AnaDipendenti.objects.filter(stato="Sospeso").order_by("cognome")
        self.query = self.request.GET.get("dip") or ""
        if self.query:
            queryset = AnaDipendenti.objects.filter(stato="Sospeso").filter(Q(nome__icontains=self.query) | Q(cognome__icontains=self.query)).order_by("cognome")
            return queryset
        return queryset


class AnagraficaDipendente(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= AnaDipendenti
    form_class = DipendentiForm
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/anagrafica-dipendente.html'
    success_url= reverse_lazy('gestione:dipendenti')
    success_message = 'Dipendente creato con successo.'
    error_meesage = "Errore nel creare il dipendente, controlla che tutti i campi siano corretti."
    
    def form_valid(self, form):
        temp = form.save(commit=False)
        return super().form_valid(form)            
    

class AnagraficaDipendenteUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= AnaDipendenti
    template_name = "gestione/update-anagrafica.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "dipendente"
    form_class = UpdateDipendentiForm
    success_url= reverse_lazy('gestione:dipendenti')


class AnagraficaDipendenteDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = AnaDipendenti
    template_name = "gestione/delete-anagrafica.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "dipendente"
    form_class = DipendentiForm
    success_url= reverse_lazy('gestione/dipendenti')


class DettagliPresenze(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Ingressidip
    today = datetime.now().date()
    excludeIdList = [9,23,24,31,32]
    presenze = Ingressidip.objects.filter(giorno=today).exclude(id_dip_ing__area__in=excludeIdList).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
    context = {"presenze" : presenze}
    context["totale_entrate"] = presenze.filter(giorno=today,checked_in=True).count()    
    context["totale_uscite"] = presenze.filter(giorno=today,checked_out=True).count()
    context["totale_assenze"] = presenze.filter(giorno=today,checked_in=False,in_permesso=False).count()
    context["data"] = today
    permission_required = 'gestione.change_anadipendenti'
    template_name= "reception/presenze.html"
        
    def getDipDay(self, id_dip_ing):
        richiesteDip = Richieste.objects.filter(id_dipendente_richiesta=id_dip_ing)
        richiesteAccettateDip = RichiesteAccettate.objects.raw("SELECT ID_Richiesta, nominativo, da_giorno_richiesta, da_ora_richiesta, a_giorno_richiesta a_ora_richiesta FROM Richieste JOIN Richieste_Accettate ON ID_richiesta = ID_richieste WHERE ID_dipendente_richiesta = %s", [id_dip_ing])

        return richiesteAccettateDip
    
    
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        queryset = Ingressidip.objects.filter(giorno=today).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
        context= {"presenze":queryset}
        context["totale_entrate"] = queryset.filter(giorno=today,checked_in=True).count()    
        context["totale_uscite"] = queryset.filter(giorno=today,checked_out=True).count()
        context["totale_assenze"] = queryset.filter(giorno=today,checked_in=False,in_permesso=False).count()
        context["totale_permessi"] = queryset.filter(giorno=today,checked_in=False,in_permesso=True).count()

        context["data"] = today
        try:
            if request.method == "GET" and (request.GET.get("data") == None) or (request.GET.get("data") == "") :
                data = self.request.GET.get("data") or today
                today = datetime.now().date()
                context["presenze"] = Ingressidip.objects.filter(giorno=today).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = context["presenze"].filter(giorno=today,checked_in=True).count()    
                context["totale_uscite"] = context["presenze"].filter(giorno=today,checked_out=True).count()
                context["totale_assenze"] = context["presenze"].filter(giorno=today,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = context["presenze"].filter(giorno=today,checked_in=False,in_permesso=True).count()

                context["data"] = today
                return render(request, self.template_name, context)
            elif request.method == "GET" and (request.GET.get("prec")):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                data = (data - timedelta(1))
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = context["presenze"].filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = context["presenze"].filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = context["presenze"].filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = context["presenze"].filter(giorno=today,checked_in=False,in_permesso=True).count()

                context["data"] = data
            elif request.method == "GET" and (request.GET.get("succ")):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                data = (data + timedelta(1))
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = context["presenze"].filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = context["presenze"].filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = context["presenze"].filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = context["presenze"].filter(giorno=today,checked_in=False,in_permesso=True).count()

                context["data"] = data
            elif request.method == "GET" and (request.GET.get("data") != None):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = context["presenze"].filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = context["presenze"].filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = context["presenze"].filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = context["presenze"].filter(giorno=today,checked_in=False,in_permesso=True).count()

                context["data"] = data
                return render(request, self.template_name, context)
        except Exception as error:
            print(error)
        
        return render(request, self.template_name,context)

class CreaIngresso(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Ingressidip
    form_class = CreaEntrata
    context_object_name= "ingresso"
    permission_required = 'gestione.change_anadipendenti'
    template_name = "reception/crea-ingresso.html"
    success_url= reverse_lazy('reception:presenze')
        
    def get_context_data(self, **kwargs):
        kwargs["CreaIngresso"] = self.get_form()
        return super().get_context_data(**kwargs)
    

class DettagliAreaPresenze(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= Ingressidip
    today = datetime.now().date()
    excludeIdList = [9,23,24,31,32]
    presenze = Ingressidip.objects.filter(giorno=today).exclude(id_dip_ing__area__in=excludeIdList).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
    context = {"presenze" : presenze}
    context["totale_entrate"] = presenze.filter(giorno=today,checked_in=True).count()    
    context["totale_uscite"] = presenze.filter(giorno=today,checked_out=True).count()
    context["totale_assenze"] = presenze.filter(giorno=today,checked_in=False,in_permesso=False).count()
    context["data"] = today
    permission_required = 'gestione.change_anadipendenti'
    template_name= "gestione/dettagli-presenze-area.html"
        
    def getDipDay(self, id_dip_ing):
        richiesteDip = Richieste.objects.filter(id_dipendente_richiesta=id_dip_ing)
        richiesteAccettateDip = RichiesteAccettate.objects.raw("SELECT ID_Richiesta, nominativo, da_giorno_richiesta, da_ora_richiesta, a_giorno_richiesta a_ora_richiesta FROM Richieste JOIN Richieste_Accettate ON ID_richiesta = ID_richieste WHERE ID_dipendente_richiesta = %s", [id_dip_ing])

        return richiesteAccettateDip
    
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        queryset = Ingressidip.objects.filter(giorno=today).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
        context= {"presenze":queryset}
        context["totale_entrate"] = queryset.filter(giorno=today,checked_in=True).count()    
        context["totale_assenze"] = queryset.filter(giorno=today,checked_in=False,in_permesso=False).count()
        context["totale_permessi"] = queryset.filter(giorno=today,checked_in=False,in_permesso=True).count()
        context["totale_area_presenze_amm"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
        context["totale_area_assenze_amm"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
        context["totale_area_presenze_APL"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=2).count() # APL
        context["totale_area_assenze_APL"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=2).count() # APL
        context["totale_area_presenze_AR_VR"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=3).count() # AR/VR
        context["totale_area_assenze_AR_VR"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=3).count() # AR/VR
        context["totale_area_presenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=4).count() # Assistenza Direzione
        context["totale_area_assenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=4).count() # Assistenza Direzione
        context["totale_area_presenze_Commerciale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=5).count() # Commerciale
        context["totale_area_assenze_Commerciale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=5).count() # Commerciale
        context["totale_area_presenze_Customer_Service"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=6).count() # Customer Service
        context["totale_area_assenze_Customer_Service"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=6).count() # Customer Service
        context["totale_area_presenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=7).count() # Didattica Autofinanziata
        context["totale_area_assenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=7).count() # Didattica Autofinanziata
        context["totale_area_presenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=8).count() # Didattica Finanziata
        context["totale_area_assenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=8).count() # Didattica Finanziata
        context["totale_area_presenze_Dirigenti"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=9).count() # Dirigenti
        context["totale_area_assenze_Dirigenti"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=9).count() # Dirigenti
        context["totale_area_presenze_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=10).count() # Edilizia
        context["totale_area_assenze_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=10).count() # Edilizia
        context["totale_area_presenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=11).count() # Editoria - Web TV
        context["totale_area_assenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=11).count() # Editoria - Web TV
        context["totale_area_presenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=12).count() # Ente Bilaterale
        context["totale_area_assenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=12).count() # Ente Bilaterale
        context["totale_area_presenze_FAD"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=13).count() # FAD
        context["totale_area_assenze_FAD"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=13).count() # FAD
        context["totale_area_presenze_Front_Office"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=14).count() # Front Office
        context["totale_area_assenze_Front_Office"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=14).count() # Front Office
        context["totale_area_presenze_Generale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=15).count() # Generale
        context["totale_area_assenze_Generale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=15).count() # Generale
        context["totale_area_presenze_Industria_4"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=16).count() # Industria 4.0
        context["totale_area_assenze_Industria_4"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=16).count() # Industria 4.0
        context["totale_area_presenze_Marketing"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=17).count() # Marketing
        context["totale_area_assenze_Marketing"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=17).count() # Marketing
        context["totale_area_presenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=18).count() # Piattaforme Moodle
        context["totale_area_assenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=18).count() # Piattaforme Moodle
        context["totale_area_presenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=19).count() # Processi e Automazioni
        context["totale_area_assenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=19).count() # Processi e Automazioni
        context["totale_area_presenze_Progettazione"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=20).count() # Progettazione
        context["totale_area_assenze_Progettazione"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=2).count() # Progettazione
        context["totale_area_presenze_Pulizie"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=21).count() # Pulizie
        context["totale_area_assenze_Pulizie"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=21).count() # Pulizie
        context["totale_area_presenze_Recruiting"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=22).count() # Recruiting
        context["totale_area_assenze_Recruiting"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=22).count() # Recruiting
        context["totale_area_presenze_Responsabile"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=23).count() # Responsabile
        context["totale_area_assenze_Responsabile"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=23).count() # Responsabile
        context["totale_area_presenze_Responsabile_Sede"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=24).count() # Responsabile Sede
        context["totale_area_assenze_Responsabile_Sede"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=24).count() # Responsabile Sede
        context["totale_area_presenze_Risorse_Umane"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=25).count() # Risorse Umane
        context["totale_area_assenze_Risorse_Umane"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=25).count() # Risorse Umane
        context["totale_area_presenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=30).count() # Scuola PSB C
        context["totale_area_assenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=30).count() # Scuola PSB C
        context["totale_area_presenze_Servizio_Civile"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=26).count() # Servizio Civile
        context["totale_area_assenze_Servizio_Civile"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=26).count() # Servizio Civile
        context["totale_area_presenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=27).count() # Sicurezza Edilizia
        context["totale_area_assenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=27).count() # Sicurezza Edilizia
        context["totale_area_presenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
        context["totale_area_assenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
        context["totale_area_presenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=29).count() # Ufficio Tecnico
        context["totale_area_assenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=29).count() # Ufficio Tecnico

        context["data"] = today
        try:
            if request.method == "GET" and (request.GET.get("data") == None) or (request.GET.get("data") == "") :
                data = self.request.GET.get("data") or today
                today = datetime.now().date()
                context["totale_entrate"] = queryset.filter(giorno=today,checked_in=True).count()    
                context["totale_assenze"] = queryset.filter(giorno=today,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = queryset.filter(giorno=today,checked_in=False,in_permesso=True).count()
                context["totale_area_presenze_amm"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_assenze_amm"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_presenze_APL"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=2).count() # APL
                context["totale_area_assenze_APL"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=2).count() # APL
                context["totale_area_presenze_AR_VR"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_assenze_AR_VR"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_presenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_assenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_presenze_Commerciale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_assenze_Commerciale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_presenze_Customer_Service"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_assenze_Customer_Service"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_presenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_assenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_presenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_assenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_presenze_Dirigenti"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_assenze_Dirigenti"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_presenze_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_assenze_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_presenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_assenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_presenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_assenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_presenze_FAD"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=13).count() # FAD
                context["totale_area_assenze_FAD"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=13).count() # FAD
                context["totale_area_presenze_Front_Office"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=14).count() # Front Office
                context["totale_area_assenze_Front_Office"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=14).count() # Front Office
                context["totale_area_presenze_Generale"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=15).count() # Generale
                context["totale_area_assenze_Generale"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=15).count() # Generale
                context["totale_area_presenze_Industria_4"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_assenze_Industria_4"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_presenze_Marketing"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=17).count() # Marketing
                context["totale_area_assenze_Marketing"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=17).count() # Marketing
                context["totale_area_presenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_assenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_presenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_assenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_presenze_Progettazione"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=20).count() # Progettazione
                context["totale_area_assenze_Progettazione"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=2).count() # Progettazione
                context["totale_area_presenze_Pulizie"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_assenze_Pulizie"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_presenze_Recruiting"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_assenze_Recruiting"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_presenze_Responsabile"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_assenze_Responsabile"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_presenze_Responsabile_Sede"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_assenze_Responsabile_Sede"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_presenze_Risorse_Umane"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_assenze_Risorse_Umane"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_presenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_assenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_presenze_Servizio_Civile"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_assenze_Servizio_Civile"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_presenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_assenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_presenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_assenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_presenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=today,checked_in=True,id_dip_ing__area=29).count() # Ufficio Tecnico
                context["totale_area_assenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=today,checked_in=False,id_dip_ing__area=29).count() # Ufficio Tecnico

                context["data"] = today
                return render(request, self.template_name, context)
            elif request.method == "GET" and (request.GET.get("prec")):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                data = (data - timedelta(1))
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()    
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = queryset.filter(giorno=data,checked_in=False,in_permesso=True).count()
                context["totale_area_presenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_assenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_presenze_APL"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=2).count() # APL
                context["totale_area_assenze_APL"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # APL
                context["totale_area_presenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_assenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_presenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_assenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_presenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_assenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_presenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_assenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_presenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_assenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_presenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_assenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_presenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_assenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_presenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_assenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_presenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_assenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_presenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_assenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_presenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=13).count() # FAD
                context["totale_area_assenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=13).count() # FAD
                context["totale_area_presenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=14).count() # Front Office
                context["totale_area_assenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=14).count() # Front Office
                context["totale_area_presenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=15).count() # Generale
                context["totale_area_assenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=15).count() # Generale
                context["totale_area_presenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_assenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_presenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=17).count() # Marketing
                context["totale_area_assenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=17).count() # Marketing
                context["totale_area_presenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_assenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_presenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_assenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_presenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=20).count() # Progettazione
                context["totale_area_assenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # Progettazione
                context["totale_area_presenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_assenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_presenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_assenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_presenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_assenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_presenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_assenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_presenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_assenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_presenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_assenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_presenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_assenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_presenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_assenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_presenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_assenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_presenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=29).count() # Ufficio Tecnico
                context["totale_area_assenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=29).count() # Ufficio Tecnico

                context["data"] = data
            elif request.method == "GET" and (request.GET.get("succ")):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                data = (data + timedelta(1))
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()    
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = queryset.filter(giorno=data,checked_in=False,in_permesso=True).count()
                context["totale_area_presenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_assenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_presenze_APL"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=2).count() # APL
                context["totale_area_assenze_APL"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # APL
                context["totale_area_presenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_assenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_presenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_assenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_presenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_assenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_presenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_assenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_presenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_assenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_presenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_assenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_presenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_assenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_presenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_assenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_presenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_assenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_presenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_assenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_presenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=13).count() # FAD
                context["totale_area_assenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=13).count() # FAD
                context["totale_area_presenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=14).count() # Front Office
                context["totale_area_assenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=14).count() # Front Office
                context["totale_area_presenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=15).count() # Generale
                context["totale_area_assenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=15).count() # Generale
                context["totale_area_presenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_assenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_presenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=17).count() # Marketing
                context["totale_area_assenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=17).count() # Marketing
                context["totale_area_presenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_assenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_presenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_assenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_presenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=20).count() # Progettazione
                context["totale_area_assenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # Progettazione
                context["totale_area_presenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_assenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_presenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_assenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_presenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_assenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_presenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_assenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_presenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_assenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_presenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_assenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_presenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_assenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_presenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_assenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_presenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_assenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_presenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=29).count() # Ufficio Tecnico
                context["totale_area_assenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=29).count() # Ufficio Tecnico

                context["data"] = data
            elif request.method == "GET" and (request.GET.get("data") != None):
                data_object = self.request.GET.get("data")
                data = datetime.strptime(data_object, "%Y-%m-%d").date()
                context["presenze"] = Ingressidip.objects.filter(giorno=data).exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()    
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_permessi"] = queryset.filter(giorno=data,checked_in=False,in_permesso=True).count()
                context["totale_area_presenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_assenze_amm"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=1).count() # Amministrazione
                context["totale_area_presenze_APL"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=2).count() # APL
                context["totale_area_assenze_APL"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # APL
                context["totale_area_presenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_assenze_AR_VR"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=3).count() # AR/VR
                context["totale_area_presenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_assenze_Assistenza_Direzione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=4).count() # Assistenza Direzione
                context["totale_area_presenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_assenze_Commerciale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=5).count() # Commerciale
                context["totale_area_presenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_assenze_Customer_Service"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=6).count() # Customer Service
                context["totale_area_presenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_assenze_Didattica_Autofinanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=7).count() # Didattica Autofinanziata
                context["totale_area_presenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_assenze_Didattica_Finanziata"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=8).count() # Didattica Finanziata
                context["totale_area_presenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_assenze_Dirigenti"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=9).count() # Dirigenti
                context["totale_area_presenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_assenze_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=10).count() # Edilizia
                context["totale_area_presenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_assenze_Editoria_Web_TV"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=11).count() # Editoria - Web TV
                context["totale_area_presenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_assenze_Ente_Bilaterale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=12).count() # Ente Bilaterale
                context["totale_area_presenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=13).count() # FAD
                context["totale_area_assenze_FAD"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=13).count() # FAD
                context["totale_area_presenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=14).count() # Front Office
                context["totale_area_assenze_Front_Office"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=14).count() # Front Office
                context["totale_area_presenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=15).count() # Generale
                context["totale_area_assenze_Generale"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=15).count() # Generale
                context["totale_area_presenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_assenze_Industria_4"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=16).count() # Industria 4.0
                context["totale_area_presenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=17).count() # Marketing
                context["totale_area_assenze_Marketing"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=17).count() # Marketing
                context["totale_area_presenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_assenze_Piattaforme_Moodle"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=18).count() # Piattaforme Moodle
                context["totale_area_presenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_assenze_Processi_e_Automazioni"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=19).count() # Processi e Automazioni
                context["totale_area_presenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=20).count() # Progettazione
                context["totale_area_assenze_Progettazione"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=2).count() # Progettazione
                context["totale_area_presenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_assenze_Pulizie"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=21).count() # Pulizie
                context["totale_area_presenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_assenze_Recruiting"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=22).count() # Recruiting
                context["totale_area_presenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_assenze_Responsabile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=23).count() # Responsabile
                context["totale_area_presenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_assenze_Responsabile_Sede"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=24).count() # Responsabile Sede
                context["totale_area_presenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_assenze_Risorse_Umane"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=25).count() # Risorse Umane
                context["totale_area_presenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_assenze_Scuola_PSB_C"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=30).count() # Scuola PSB C
                context["totale_area_presenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_assenze_Servizio_Civile"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=26).count() # Servizio Civile
                context["totale_area_presenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_assenze_Sicurezza_Edilizia"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=27).count() # Sicurezza Edilizia
                context["totale_area_presenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_assenze_Ufficio_Associazioni_Sportive"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=28).count() # Ufficio Associazioni Sportive
                context["totale_area_presenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=True,id_dip_ing__area=29).count() # Ufficio Tecnico
                context["totale_area_assenze_Ufficio_Tecnico"] = context["presenze"].filter(giorno=data,checked_in=False,id_dip_ing__area=29).count() # Ufficio Tecnico

                context["data"] = data
                return render(request, self.template_name, context)
        except Exception as error:
            print(error)
        
        return render(request, self.template_name,context)

##### CRUD AREA

class ListaAree(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Area
    context_object_name = "aree"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/aree.html'
    form_class= AreaForm
    query = ""
    
    def get_context_data(self, **kwargs):
        context = super(ListaAree, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context

    def get_queryset(self):
        queryset = Area.objects.all().order_by("nome_area")
        if self.request.GET.get("area") or "":
            self.query = self.request.GET.get("area") or "" 
        if self.query:
            queryset = Area.objects.filter(Q(nome_area__icontains=self.query)).order_by("nome_area")
            return queryset
        return queryset
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione:aree')
        else:
            form = self.form_class()
            return render(request, self.template_name, self.get_context_data())
    

class AreaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Area
    form_class = AreaForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/crea-nuova-area.html'
    success_url= reverse_lazy('gestione:aree')
    
    def form_valid(self, form):
        if form.is_valid():
            return super(AreaCreateView, self).form_valid(form)  

class AreaUpddateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Area
    template_name = "gestione/modifica-area.html"
    permission_required = 'gestione.change_anadipendenti'
    # context_object_name = "area"
    form_class = AreaForm
    success_url= reverse_lazy('gestione:aree')
    
    def get_context_data(self, **kwargs):
        kwargs["AreaForm"] = self.get_form()
        return super().get_context_data(**kwargs)

class AreaDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Area
    template_name = "gestione/elimina-area.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "area"
    form_class = AreaForm
    success_url= reverse_lazy('gestione:aree')


##### CRUD ISTRUZIONE


class ListaIstruzioni(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Istruzione
    context_object_name = "istruzioni"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/lista-tipo-di-istruzione.html'
    form_class = IstruzioneForm
    paginate_by = 8
    query = ""
    
    
    def get_context_data(self, **kwargs):
        context = super(ListaIstruzioni, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = Istruzione.objects.all().order_by("tipo_istruzione")
        if self.request.GET.get("istruzione") or "":
            self.query = self.request.GET.get("istruzione") or "" 
        if self.query:
            queryset = Istruzione.objects.filter(Q(tipo_istruzione__icontains=self.query)).order_by("tipo_istruzione")
            return queryset
        return queryset
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione:lista-tipo-di-istruzione')
        else:
            form = self.form_class()
            return render(request, self.template_name, self.get_context_data())
    
class IstruzioneCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Istruzione
    form_class = IstruzioneForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/aggiungi-tipo-di-istruzione.html'
    success_url= reverse_lazy('gestione:lista-tipo-di-istruzione')
    
    def form_valid(self, form):
        if form.is_valid():
            return super(IstruzioneCreateView, self).form_valid(form)  

class IstruzioneUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Istruzione
    template_name = "gestione/modifica-tipo-di-istruzione.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "istruzione"
    form_class = IstruzioneForm
    success_url= reverse_lazy('gestione:lista-tipo-di-istruzione')
    
    def get_context_data(self, **kwargs):
        kwargs["IstruzioneForm"] = self.get_form()
        return super().get_context_data(**kwargs)
    
class IstruzioneDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Istruzione
    template_name = "gestione/elimina-tipo-di-istruzione.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "istruzione"
    form_class = IstruzioneForm
    success_url= reverse_lazy('gestione:lista-tipo-di-istruzione')

##### CRUD MANSIONE


class ListaMansioni(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mansione
    context_object_name = "mansioni"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/lista-mansioni.html'
    form_class = MansioneForm
    query = ""
    
    
    def get_context_data(self, **kwargs):
        context = super(ListaMansioni, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = Mansione.objects.all().order_by("tipo_mansione")
        if self.request.GET.get("mansione") or "":
            self.query = self.request.GET.get("mansione") or "" 
        if self.query:
            queryset = Mansione.objects.filter(Q(tipo_mansione__icontains=self.query)).order_by("tipo_mansione")
            return queryset
        return queryset
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione:lista-mansioni')
        else:
            form = self.form_class()
            return render(request, self.template_name, self.get_context_data())
    
class MansioneCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Mansione
    form_class = MansioneForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/aggiungi-tipo-di-mansione.html'
    success_url= reverse_lazy('gestione:lista-mansioni')
    
    def form_valid(self, form):
        if form.is_valid():
            return super(MansioneCreateView, self).form_valid(form)  

class MansioneUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Mansione
    template_name = "gestione/modifica-mansione.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "mansione"
    form_class = MansioneForm
    success_url= reverse_lazy('gestione:lista-mansioni')
    
    def get_context_data(self, **kwargs):
        kwargs["MansioneForm"] = self.get_form()
        return super().get_context_data(**kwargs)
    
class MansioneDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Mansione
    template_name = "gestione/elimina-mansione.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "mansione"
    form_class = MansioneForm
    success_url= reverse_lazy('gestione:lista-mansioni')


##### CRUD SEDE


class ListaSedi(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Sede
    context_object_name = "sedi"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/sedi.html'
    paginate_by = 8
    form_class = SedeForm   
    query = ""
    
    
    def get_context_data(self, **kwargs):
        context = super(ListaSedi, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = Sede.objects.all().order_by("nome_sede")
        if self.request.GET.get("sede") or "":
            self.query = self.request.GET.get("sede") or "" 
        if self.query:
            queryset = Sede.objects.filter(Q(nome_sede__icontains=self.query)).order_by("nome_sede")
            return queryset
        return queryset


class SedeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Sede
    form_class = SedeForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/crea-nuova-sede.html'
    success_url= reverse_lazy('gestione:sedi')
    
    def form_valid(self, form):
        if form.is_valid():
            return super(SedeCreateView, self).form_valid(form)  

class SedeUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Sede
    template_name = "gestione/modifica-sede.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "sede"
    form_class = SedeForm
    success_url= reverse_lazy('gestione:sedi')
            
    def get_context_data(self, **kwargs):
        kwargs["SedeForm"] = self.get_form()
        return super().get_context_data(**kwargs)
    
class SedeDeleteViews(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Sede
    template_name = "gestione/delete-sede-views.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "sede"
    form_class = SedeForm
    success_url= reverse_lazy('gestione:sedi')


##### CRUD SOCIETA

class ListaSocieta2(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Societa
    context_object_name = "societas"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/societa.html'
    form_class=SocietaForm
    query = ""
    
    def get_context_data(self, **kwargs):
        context = super(ListaSocieta2, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = Societa.objects.all().order_by("nome_societa")
        if self.request.GET.get("societa") or "":
            self.query = self.request.GET.get("societa") or "" 
        if self.query:
            queryset = Societa.objects.filter(Q(nome_societa__icontains=self.query)).order_by("nome_societa")
            return queryset
        return queryset
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione:societa')
        else:
            form = self.form_class()
            return render(request, self.template_name, self.get_context_data())

class SocietaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Societa
    form_class = SocietaForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/crea-nuova-societa.html'
    success_url= reverse_lazy('gestione:societa')
    
    def form_valid(self, form):
        if form.is_valid():
            
            return super(SocietaCreateView, self).form_valid(form)  

class SocietaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Societa
    template_name = "gestione/modifica-societa.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "societa"
    form_class = SocietaForm
    success_url= reverse_lazy('gestione:societa')
    
    def get_context_data(self, **kwargs):
        kwargs["SocietaForm"] = self.get_form()
        return super().get_context_data(**kwargs)

class SocietaDeleteViews(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Societa
    template_name = "gestione/delete-societa-views.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "societa"
    form_class = SocietaForm
    success_url= reverse_lazy('gestione:societa')

##### CRUD TIPO CONTRATTO

class ListaTipoContratti(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TipoContratto
    context_object_name = "contratti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/lista-tipo-di-contratti.html'
    form_class = TipoContrattoForm
    query = ""
    
    
    def get_context_data(self, **kwargs):
        context = super(ListaTipoContratti, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = TipoContratto.objects.all().order_by("nome_contratto")
        if self.request.GET.get("contratto") or "":
            self.query = self.request.GET.get("contratto") or "" 
        if self.query:
            queryset = TipoContratto.objects.filter(Q(nome_contratto__icontains=self.query)).order_by("nome_contratto")
            return queryset
        return queryset
    
    def post(self, request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione:lista-tipo-di-contratti')
        else:
            form = self.form_class()
            return render(request, self.template_name, self.get_context_data())

class TipoContrattoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= TipoContratto
    form_class = TipoContrattoForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/aggiungi-tipo-di-contratto.html'
    success_url= reverse_lazy('gestione:lista-tipo-di-contratti')
    
    def form_valid(self, form):
        if form.is_valid():
            
            return super(TipoContrattoCreateView, self).form_valid(form)  


class TipoContrattoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= TipoContratto
    template_name = "gestione/modifica-tipo-di-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "contratto"
    form_class = TipoContrattoForm
    success_url= reverse_lazy('gestione:lista-tipo-di-contratti')
    
    def get_context_data(self, **kwargs):
        kwargs["TipoContrattoForm"] = self.get_form()
        return super().get_context_data(**kwargs)
    
    
class TipoContrattoDeleteViews(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = TipoContratto
    template_name = "gestione/elimina-tipo-di-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "contratto"
    form_class = TipoContrattoForm
    success_url= reverse_lazy('gestione:lista-tipo-di-contratti')


##### RICHIESTE ACCETTATE


class GestioneRichiestePersonale(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    models = Richieste
    paginate_by = 10
    context_object_name = "richieste"
    template_name = "gestione/richieste-accettate.html"
    permission_required = 'gestione.change_richiesteaccettate'
    query = ""
    in_permesso= ""
    rientranti= ""
    
    def get_queryset(self):
        today = datetime.now().date()
        queryset = RichiesteAccettate.objects.all().order_by("-data_creazione")
        self.query = self.request.POST.get("search-area") or ""
        if self.query == "":
            queryset = RichiesteAccettate.objects.filter(in_corso=0).order_by("-data_creazione")
            self.in_permesso = queryset.filter(in_corso=0,data_inizio_permesso__gte=today).count()
            self.rientranti = queryset.filter(in_corso=0,data_inizio_permesso__gte=today).count()
            return queryset
        elif self.query:
            queryset = RichiesteAccettate.objects.filter(in_corso=0,data_fine_permesso__gte=self.query)
            self.in_permesso = queryset.filter(in_corso=0,data_inizio_permesso=self.query).count()
            self.rientranti = queryset.filter(in_corso=0,data_fine_permesso=self.query).count()
            return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        if self.query != "":
            data=self.query
            data = datetime.strptime(data,"%Y-%m-%d").date()
            context['data'] = data
            context["in_permesso"] = self.in_permesso
            context["rientranti"] = self.rientranti
            return context
        elif self.query == "":
            queryset = RichiesteAccettate.objects.filter(in_corso=0,data_fine_permesso__gte=today)
            in_permesso = queryset.filter(in_corso=0,data_inizio_permesso=today).count()
            rientranti = queryset.filter(in_corso=0,data_fine_permesso=today).count()
            context['data'] = today
            context["in_permesso"] = in_permesso
            context["rientranti"] = rientranti
            return context
        else:
            data = self.query
            data = datetime.now().date()
            context['data'] = data
            context["in_permesso"] = self.in_permesso
            context["rientranti"] = self.rientranti
            return context


class RichiesteAccettateUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= RichiesteAccettate
    template_name = "gestione/conferma-richieste-accettate.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "object"
    form_class = RichiesteAccettateForm
    success_url= reverse_lazy('gestione:richieste-accettate')
    
    def get_context_data(self, **kwargs):
        kwargs["RichiesteAccettateForm"] = self.get_form()
        kwargs["dipendente"] = AnaDipendenti.objects.get(id_dip=self.kwargs["pk"])
        return super().get_context_data(**kwargs)
        

class ModifcaRichiesteAccettate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= RichiesteAccettate
    template_name = "gestione/modifica-richieste-accettate.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "object"
    form_class = ModificaRichiesteAccettateForm
    success_url= reverse_lazy('gestione:richieste-accettate')
    
    def get_context_data(self, **kwargs):
        kwargs["RichiesteAccettateForm"] = self.get_form()
        kwargs["dipendente"] = AnaDipendenti.objects.get(id_dip=self.kwargs["pk"])
        return super().get_context_data(**kwargs)
        
        
# CONTRATTO
@login_required
@permission_required('gestione.change_anadipendenti')
def ListaPercContratti(request):
    query = ""
    
    if request.POST.get("perc_contratto"):
        query = request.POST.get("perc_contratto")
        queryset = PercentualiContratto.objects.filter(Q(perc_contratto__icontains=query) | Q(dicitura_percentuale__icontains=query)).order_by("perc_contratto")
    elif query == "":
        queryset = PercentualiContratto.objects.all().order_by("perc_contratto")
        return render(request,'gestione/lista_percentuali_contratti.html',{'perc_contratti':queryset})
    
    return render(request,'gestione/lista_percentuali_contratti.html',{'perc_contratti':queryset})


    
class PercContrattiCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= PercentualiContratto
    form_class = OreContrattiForm   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/aggiungi-perc-contratto.html'
    success_url= reverse_lazy('gestione:lista_percentuali_contratti')
        
    def form_valid(self, form):
        if form.is_valid():
            return super(PercContrattiCreateView, self).form_valid(form)  

class PercContrattiUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= PercentualiContratto
    template_name = "gestione/modifica-perc-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "perc_contratto"
    form_class = OreContrattiForm
    success_url= reverse_lazy('gestione:lista_percentuali_contratti')
        
    def get_context_data(self, **kwargs):
        kwargs["OreContrattiForm"] = self.get_form()
        return super().get_context_data(**kwargs)
    
class PercContrattiDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = PercentualiContratto
    template_name = "gestione/elimina-perc-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "perc_contratto"
    form_class = OreContrattiForm
    success_url= reverse_lazy('gestione:lista_percentuali_contratti')
    

# #### CRUD CONTRATTI


class ListaContrattiListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contratti
    context_object_name = "contratti"
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/lista_contratti.html'
    paginate_by = 10
    form_class = ContrattiFormInsert
    query = ""
    
    
    def get_context_data(self, **kwargs):
        context = super(ListaContrattiListView, self).get_context_data(**kwargs)
        context["form"] = self.form_class()
        if self.query != "":
            data=self.query
            return context
        else:
            data = self.query
            return context
    
    def get_queryset(self):
        queryset = Contratti.objects.all().order_by("id_dip__cognome")
        if self.request.GET.get("contratto") or "":
            self.query = self.request.GET.get("contratto") or ""
        if self.query:
            queryset = Contratti.objects.filter(Q(codicecontratto__icontains=self.query)|Q(id_dip__cognome__icontains=self.query)|Q(id_dip__nome__icontains=self.query)).order_by("id_dip")
            return queryset
        return queryset

class ContrattiCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model= Contratti
    form_class = ContrattiFormInsert   
    permission_required = 'gestione.change_anadipendenti'
    template_name = 'gestione/crea-contratto.html'
    success_url= reverse_lazy('gestione:lista_contratti')
    
    def form_valid(self, form):
        dipendente = form.cleaned_data['dipendenti']
        dipendente_id = dipendente.pk
        tipo_contratto = form.cleaned_data['tipologia']
        dip = AnaDipendenti.objects.get(id_dip=dipendente_id)
        temp = form.save()
        temp.id_dipendente = AnaDipendenti.objects.get(id_dip=dipendente_id)
        contratto = TipoContratto.objects.get(nome_contratto=tipo_contratto)
        temp.codicecontratto = contratto.codice_contratto
        temp.save()
        return super().form_valid(form)  


class ContrattiUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model= Contratti
    template_name = "gestione/modifica-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "contratto"
    form_class = ContrattiFormUpdate
    success_url= reverse_lazy('gestione:lista_contratti')
    
    def get_context_data(self, **kwargs):
        kwargs["ContrattiFormUpdate"] = self.get_form()
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        tipo_contratto = form.cleaned_data['tipologia']
        temp = form.save()
        contratto = TipoContratto.objects.get(nome_contratto=tipo_contratto)
        temp.codicecontratto = contratto.codice_contratto
        temp.save()
        return super().form_valid(form)  
    
class ContrattoDeleteViews(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Contratti
    template_name = "gestione/elimina-contratto.html"
    permission_required = 'gestione.change_anadipendenti'
    context_object_name = "contratto"
    form_class = ContrattiFormInsert
    success_url= reverse_lazy('gestione:lista_contratti')
