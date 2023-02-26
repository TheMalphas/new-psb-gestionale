from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .models import Richieste, Area, AddStraordinari, AddTrasferte, AddRimborsi, AuthUser, AnaDipendenti, CapoArea, Permessi, RichiesteAccettate, Ingressidip, Cedolini, AppoggioVerificaQr, TodoList
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django import forms
from django.contrib import messages
from .forms import DipendentiForm, UpdateRichiestaForm, UpdateEntrata, TodoListCapoAreaUpdateForm
from datetime import time, datetime, timedelta,date
from django.contrib.auth.views import redirect_to_login
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.db.models import Count, F, Value
import qrcode
from django.core.exceptions import PermissionDenied
from io import BytesIO
from . import updateCedolini

#HTMX VIEWS
@login_required #DELETE
def delete_todo_capo_area(request,pk):
    template_name = 'partials/todolist_capo_area.html'
    oggetto = TodoList.objects.filter(id_lista=pk).update(fatta=1)
    capoArea = AnaDipendenti.objects.get(user_id = request.user.pk)
    listaDipendenti = AnaDipendenti.objects.filter(area=capoArea.area.id_area,stato="Attivo").values_list('user_id', flat=True)
    dipendentiUser = AuthUser.objects.filter(id__in=listaDipendenti)
    dipendentiUserInput = AuthUser.objects.filter(id__in=listaDipendenti).values_list('id','last_name','first_name').exclude(id=request.user.pk)

    todos = TodoList.objects.filter(user__in=dipendentiUser,fatta=False).order_by("data").order_by("-priority")
    user = request.user.pk

    return render(request,template_name,{'todos':todos,'dipendenti':dipendentiUserInput,'user_id':user})

#UPDATE
class UpdateTodoCapoArea(LoginRequiredMixin,UpdateView):
    model= TodoList
    form_class = TodoListCapoAreaUpdateForm
    template_name = "capi_area/update_todo_capo_area.html"
    context_object_name = "todo"
    success_url= reverse_lazy('capi_area:capi_area_todo')


@login_required #CREATE AND LIST
@permission_required('capi_area.change_richiesteaccettate')
def assegnaTodo(request):
    template_name = 'partials/todolist_capo_area.html'
    capoArea = AnaDipendenti.objects.get(user_id = request.user.pk)
    listaDipendenti = AnaDipendenti.objects.filter(area=capoArea.area.id_area,stato="Attivo").values_list('user_id', flat=True)
    dipendentiUser = AuthUser.objects.filter(id__in=listaDipendenti)
    dipendentiUserInput = AuthUser.objects.filter(id__in=listaDipendenti).values_list('id','last_name','first_name').exclude(id=request.user.pk)


    if request.POST.get('aggiungi') and request.POST.get('dipendente') and request.POST.get('dipendente') != 'Me':
        appunto = request.POST.get('aggiungi')

        if appunto != "" or appunto != None:
            dipendente = request.POST.get('dipendente')
            dip = AuthUser.objects.get(id=dipendente)
            capodip = AnaDipendenti.objects.get(user_id=request.user.pk)
            capocchia = CapoArea.objects.get(id_dipendente=capodip.id_dip)
            oggetto = TodoList.objects.get_or_create(todo=appunto,user=AuthUser.objects.get(id=dipendente),setter=CapoArea.objects.get(id_capo=capocchia.pk))
    
    elif request.POST.get('aggiungi'):
        appunto = request.POST.get('aggiungi')
        utente = AuthUser.objects.get(id=request.user.pk)
        oggetto = TodoList.objects.get_or_create(todo=appunto.title(),user=utente)
    
    todos = TodoList.objects.filter(user__in=dipendentiUser,fatta=False).order_by("data").order_by("-priority")
    user = request.user.pk
    return render(request,template_name,{'todos':todos,'dipendenti':dipendentiUserInput,'user_id':user})


@login_required
@permission_required('capi_area.change_richiesteaccettate')
def listaTodoCapoArea(request):
    capoArea = AnaDipendenti.objects.get(user_id = request.user.pk)
    listaDipendenti = AnaDipendenti.objects.filter(area=capoArea.area.id_area,stato="Attivo").values_list('user_id', flat=True)
    dipendentiUser = AuthUser.objects.filter(id__in=listaDipendenti).values_list('id',flat=True)
    dipendentiUserInput = AuthUser.objects.filter(id__in=listaDipendenti).values_list('id','last_name','first_name').exclude(id=request.user.pk)

    template_name='capi_area/capi_area_todo.html'
    todos = TodoList.objects.filter(user__in=dipendentiUser,fatta=False).order_by("data").order_by("-priority")
    context = {'todos':todos}
    context["dipendenti"] = dipendentiUserInput
    context["user_id"] = request.user.pk
    return render(request,template_name,context)


@login_required
@permission_required('capi_area.change_richiesteaccettate')
def dashboardCapoarea(request):
    today=datetime.now().date()
    template_name = "capi_area/dashboard-capo-area.html"
    anadipendente = AnaDipendenti.objects.get(user_id=request.user.pk)
    capoccione = CapoArea.objects.get(id_dipendente=anadipendente.id_dip)
    squadra = AnaDipendenti.objects.filter(area=capoccione.area,stato="Attivo")
    listaIdSquadra = [el.id_dip for el in squadra]
    numeroSquadra = len(listaIdSquadra)
    squadraPresente = Ingressidip.objects.filter(giorno=today,id_dip_ing__in=listaIdSquadra,timestamp_scan_entrata__isnull=False)
    numeroSquadraIngressi = [ing.id_dip_ing.id_dip for ing in squadraPresente]
    squadraPresenteAna = AnaDipendenti.objects.filter(sede=capoccione.area,stato="Attivo",id_dip__in=numeroSquadraIngressi)
    squadraPresenteNumero = squadraPresente.count()
    richieste = Richieste.objects.filter(id_dipendente_richiesta__in=listaIdSquadra)
    richiesteNumero = richieste.count()
    richiestePermesso = richieste.filter().exclude(id_permessi_richieste=6).count()
    richiesteStraordinari = AddStraordinari.objects.filter(id_dip__in=listaIdSquadra,stato=False).count()

    return render(request,template_name,{"capoArea":capoccione,"squadra":squadra,"numeroSquadra":numeroSquadra,"squadraPresenteAna":squadraPresenteAna,"squadraPresenteNumero":squadraPresenteNumero,"richiesteNumero":richiesteNumero,"richiestePermesso":richiestePermesso,"richiesteStraordinari":richiesteStraordinari})

# GestioneRichiesteList
class DettagliPresenze(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Ingressidip
    day = datetime.now()
    today = datetime.now().date()
    yesterday = (day - timedelta(1)).date()
    tomorrow = (day + timedelta(1)).date()
    paginate_by = 10
    presenze = Ingressidip.objects.filter(giorno=today).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
    context = {"presenze" : presenze}
    permission_required = 'capi_area.change_richiesteaccettate'
    template_name = "capi_area/dettagli-presenze.html"

    def getDipDay(self, id_dip_ing):
        richiesteDip = Richieste.objects.filter(id_dipendente_richiesta=id_dip_ing)
        richiesteAccettateDip = RichiesteAccettate.objects.raw("SELECT ID_Richiesta, nominativo, da_giorno_richiesta, da_ora_richiesta, a_giorno_richiesta a_ora_richiesta FROM Richieste JOIN Richieste_Accettate ON ID_richiesta = ID_richieste WHERE ID_dipendente_richiesta = %s", [id_dip_ing])
        return richiesteAccettateDip
    
    def get(self, request, *args, **kwargs):
        day = datetime.now()
        today = datetime.now().date()
        queryset = Ingressidip.objects.filter(giorno=today).select_related("id_dip_ing").order_by("nominativo").order_by("-entrata")
        context= {"presenze":queryset}
        data = day
        
        try:
            if request.method == "GET" and (request.GET.get("data") != ""):
                data = self.request.GET.get("data") or today
                context["presenze"] = Ingressidip.objects.filter(giorno=data).order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()    
                context["totale_uscite"] = queryset.filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_assenze_area"] = queryset.filter(giorno=data, checked_in=False).count()
                context["totale_presenze_area"] = queryset.filter(giorno=data,checked_in=True).count()
                context["data"] = data
                return render(request, self.template_name, context)
            elif request.method == "GET" and (request.GET.get("prec")):
                data = (data - timedelta(1)).date()
                context["presenze"] = Ingressidip.objects.filter(giorno=data).order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = queryset.filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_assenze_area"] = queryset.filter(giorno=data, checked_in=False).count()
                context["totale_presenze_area"] = queryset.filter(giorno=data,checked_in=True).count()
                context["data"] = data
            elif request.method == "GET" and (request.GET.get("succ")):
                data = (data + timedelta(1)).date()
                context["presenze"] = Ingressidip.objects.filter(giorno=data).order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = queryset.filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_assenze_area"] = queryset.filter(giorno=data, checked_in=False).count()
                context["totale_presenze_area"] = queryset.filter(giorno=data,checked_in=True).count()
                context["data"] = data
            else: 
                data = self.request.GET.get("data") or today
                context["presenze"] = Ingressidip.objects.filter(giorno=data).order_by("nominativo")
                context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()
                context["totale_uscite"] = queryset.filter(giorno=data,checked_out=True).count()
                context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
                context["totale_assenze_area"] = queryset.filter(giorno=data, checked_in=False).count()
                context["totale_presenze_area"] = queryset.filter(giorno=data,checked_in=True).count()
                context["data"] = data
                return render(request, self.template_name, context)
        except Exception as error:
            print(error)
        
        return render(request, self.template_name,context)

@login_required
@permission_required("capi_area.change_richiesteaccettate")
def capiAreaRichiesteAllList(request):
    template_name = "capi_area/richieste.html"
    today = datetime.now().date()
    tenDays = (today + timedelta(9))
    monthDays = (today + timedelta(30))
    
    
    try:
        capo_area = CapoArea.objects.get(id_dipendente__user=request.user.pk)
        area = Area.objects.get(id_area=capo_area.area)
        richieste = Richieste.objects.filter(id_dipendente_richiesta__area=capo_area.area,da_giorno_richiesta__lte=monthDays).order_by("-a_giorno_richiesta")
        daRevisionare = Richieste.objects.filter(id_dipendente_richiesta__area=capo_area.area,stato=None).order_by("-a_giorno_richiesta").count()
        accettate = Richieste.objects.filter(id_dipendente_richiesta__area=capo_area.area,stato=1,da_giorno_richiesta__lte=tenDays).order_by("-a_giorno_richiesta").count()
        rifiutate = Richieste.objects.filter(id_dipendente_richiesta__area=capo_area.area,stato=0,da_giorno_richiesta__lte=tenDays).order_by("-a_giorno_richiesta").count()
        if request.method == "POST" and request.POST.get("dipendente"):
            query = request.POST.get("dipendente")
            queryset = richieste.filter(nominativo__icontains=query).order_by("-a_giorno_richiesta")
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate,'area':area.nome_area})
        elif request.method == "POST" and request.POST.get("daRevisionare"):
            queryset = richieste.filter(stato=None).order_by("-a_giorno_richiesta")
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate,'area':area.nome_area})
        elif request.method == "POST" and request.POST.get("accettate"):
            queryset = richieste.filter(stato=1).order_by("-a_giorno_richiesta")
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate,'area':area.nome_area})
        elif request.method == "POST" and request.POST.get("rifiutate"):
            queryset = richieste.filter(stato=0).order_by("-a_giorno_richiesta")
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate,'area':area.nome_area})
        else:
            return render(request,template_name,{'richieste':richieste,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate,'area':area.nome_area})
    except CapoArea.DoesNotExist:
        raise PermissionDenied("Non sei un Capo Area.")
    

@login_required
@permission_required("capi_area.change_richiesteaccettate")
def capiAreaRichiesteStaordinariList(request):
    template_name = "capi_area/richieste-straordinari.html"
    today = datetime.now().date()
    tenDays = (today + timedelta(9))
    monthDays = (today + timedelta(30))
    
    try:
        anadipendente = AnaDipendenti.objects.get(user_id=request.user.pk)
        capoccione = CapoArea.objects.get(id_dipendente=anadipendente.id_dip)
        squadra = AnaDipendenti.objects.filter(area=capoccione.area,stato="Attivo")
        listaIdSquadra = [el.id_dip for el in squadra]
        richieste = AddStraordinari.objects.filter(id_dip__in=listaIdSquadra,rel_giorno__lte=monthDays)
        daRevisionare = richieste.filter(stato=False)
        accettate = richieste.filter(stato=True)
        rifiutate = richieste.filter(stato=2)
        
        if request.method == "POST" and request.POST.get("dipendente"):
            query = request.POST.get("dipendente")
            queryset = richieste.filter(Q(id_dip__nome__icontains=query) | Q(id_dip__cognome__icontains=query)).order_by("-rel_giorno")
            daRevisionare = richieste.filter(stato=False).count()
            accettate = richieste.filter(stato=True).count()
            rifiutate = richieste.filter(stato=2).count()
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate})
        
        elif request.method == "POST" and request.POST.get("daRevisionare"):
            queryset = daRevisionare.order_by("-rel_giorno")
            daRevisionare = daRevisionare.count()
            accettate = accettate.count()
            rifiutate = rifiutate.count()
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate})
        
        elif request.method == "POST" and request.POST.get("accettate"):
            queryset = accettate.order_by("-rel_giorno")
            daRevisionare = daRevisionare.count()
            accettate = accettate.count()
            rifiutate = rifiutate.count()
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate})
        
        elif request.method == "POST" and request.POST.get("rifiutate"):
            queryset = rifiutate.order_by("-rel_giorno")
            daRevisionare = daRevisionare.count()
            accettate = accettate.count()
            rifiutate = rifiutate.count()
            return render(request,template_name,{'richieste':queryset,'daRevisionare':daRevisionare,'accettate':accettate,'rifiutate':rifiutate})
        
        else:
            return render(request,template_name,{'richieste':daRevisionare,'daRevisionare':daRevisionare.count(),'accettate':accettate.count(),'rifiutate':rifiutate.count()})
    except CapoArea.DoesNotExist:
        raise PermissionDenied("Non sei un Capo Area.")
    

class Capi_AreaRichiesteAccettateList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    models = Richieste
    context_object_name = "richieste"
    template_name = "capi_area/accettate.html"
    permission_required = 'capi_area.change_richiesteaccettate'
    paginate_by = 8


    def get_queryset(self):
        capo_area = CapoArea.objects.get(id_dipendente__user=self.request.user.pk)
        queryset = Richieste.objects.filter(id_dipendente_richiesta__id_capo_area=capo_area).order_by("-a_giorno_richiesta").filter(stato=1).order_by('-timestamp')

        query = self.request.GET.get("search-area") or ""
        if query:
            return queryset.filter(nominativo__icontains=query)
        return queryset
        


class Capi_AreaRichiesteRifiutateList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    models = Richieste
    context_object_name = "richieste"
    template_name = "capi_area/rifiutate.html"
    permission_required = 'capi_area.change_richiesteaccettate'
    paginate_by = 8

    
    def get_queryset(self):
        capo_area = CapoArea.objects.get(id_dipendente__user=self.request.user.pk)
        queryset = Richieste.objects.filter(id_dipendente_richiesta__id_capo_area=capo_area).order_by("-a_giorno_richiesta").filter(stato=0).order_by('-timestamp')
        query = self.request.GET.get("search-area") or ""
        if query:
            return queryset.filter(nominativo__icontains=query)
        return queryset

class Capi_AreaRichiesteDaRevisionareList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    models = Richieste
    context_object_name = "richieste"
    template_name = "capi_area/da_revisionare.html"
    permission_required = 'capi_area.change_richiesteaccettate'
    paginate_by = 8

    
    def get_queryset(self):
        capo_area = CapoArea.objects.get(id_dipendente__user=self.request.user.pk)
        queryset = Richieste.objects.filter(id_dipendente_richiesta__id_capo_area=capo_area).order_by("-a_giorno_richiesta").filter(stato=None).order_by('-timestamp')
        query = self.request.GET.get("search-area") or ""
        if query:
            return queryset.filter(nominativo__icontains=query)
        return queryset


class AccettaRichiesta(LoginRequiredMixin,PermissionRequiredMixin,View):
    template_name = "capi_area/gestisci-richiesta.html"
    context_object_name = 'richiesta'
    permission_required = 'capi_area.change_richiesteaccettate'
    fields = ['note','stato']
    
        
    def daterange(self,start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def runAcceptQuery(self, user, id_richiesta, *args, **kwargs):
        try: 
            Richieste.objects.filter(pk=id_richiesta).update(stato=1)
            instance = Richieste.objects.get(pk=id_richiesta)
            richiestaobj = Richieste.objects.get(pk=id_richiesta)
            dipendente = instance.id_dipendente_richiesta
            initPerm = instance.da_giorno_richiesta
            finePerm = instance.a_giorno_richiesta
            oraInitPerm = instance.da_ora_richiesta
            oraFinePerm = instance.a_ora_richiesta

            if instance.id_permessi_richieste != None:
                codPerm = instance.id_permessi_richieste.id_permesso
                dipendente = Richieste.objects.filter(pk=id_richiesta).values_list('id_dipendente_richiesta',flat=True)
                dip = AnaDipendenti.objects.get(user=user)
                capoarea = CapoArea.objects.get(id_dipendente=dip.id_dip)
                annoR=initPerm.year
                meseR=initPerm.month
                giornoR=initPerm.day
                annoT=finePerm.year
                meseT=finePerm.month
                giornoT=finePerm.day
                dippo=dipendente[0]

                        
                start_date = date(annoR, meseR, giornoR)
                end_date = date(annoT, meseT, giornoT)

                for single_date in self.daterange(start_date, end_date):
                    annoC=single_date.year
                    meseC=single_date.month
                    giornoC=single_date.day
                    if instance.id_permessi_richieste:
                        updateIngresso = Ingressidip.objects.filter(giorno=single_date, id_dip_ing=dippo).update(id_permesso=id_richiesta,tipo_permesso=codPerm,in_permesso=1)
                    else: updateIngresso = Ingressidip.objects.filter(giorno=single_date, id_dip_ing=dippo).update(id_permesso=id_richiesta,in_permesso=1)
                    try:
                        updateCedolini.cedFunction(giornoC,meseC,annoC,dippo,codPerm)
                        print(f"done for {single_date} ")
                    except Exception as error:
                        print(error)
                if not(RichiesteAccettate.objects.filter(id_richieste=richiestaobj).exists()):
                    instance.time_accettato = (timezone.now() + timezone.timedelta(hours=1))
                    instance.save()
                    richiesta_accettata = RichiesteAccettate.objects.create(id_richieste=richiestaobj,
                    id_capoarea_richieste=capoarea,stato=1,data_inizio_permesso = initPerm, data_fine_permesso=finePerm,
                    ora_inizio_permesso=oraInitPerm,ora_fine_permesso=oraFinePerm,id_creazione=capoarea.id_capo,data_creazione=timezone.now() + timezone.timedelta(hours=1))
                    richiesta_accettata.save()
                    
            elif instance.id_permessi_richieste == None:
                oraR = oraInitPerm.hour
                oraT = oraFinePerm.hour
                codPerm = None
                dipendente = Richieste.objects.filter(pk=id_richiesta).values_list('id_dipendente_richiesta',flat=True)
                dip = AnaDipendenti.objects.get(user=user)
                capoarea = CapoArea.objects.get(id_dipendente=dip.id_dip)
                annoR=initPerm.year
                meseR=initPerm.month
                giornoR=initPerm.day
                annoT=finePerm.year
                meseT=finePerm.month
                giornoT=finePerm.day
                dippo=dipendente[0]

                        
                start_date = date(annoR, meseR, giornoR)
                end_date = date(annoT, meseT, giornoT)

                annoC=start_date.year
                meseC=start_date.month
                giornoC=start_date.day

                updateIngresso = Ingressidip.objects.filter(giorno=start_date, id_dip_ing=dippo).update(id_permesso=id_richiesta,tipo_permesso=codPerm,in_permesso=1)
                try:
                    updateCedolini.addPermCedFunctionOra(giornoC,meseC,annoC,dippo,oraR,oraT,codPerm)
                    print(f"done for {start_date} ")
                except Exception as error:
                    print(error)
                if not(RichiesteAccettate.objects.filter(id_richieste=richiestaobj.id_richiesta)):
                    instance.time_accettato = (timezone.now() + timezone.timedelta(hours=1))
                    instance.save()
                    richiesta_accettata = RichiesteAccettate.objects.create(id_richieste=richiestaobj,
                    id_capoarea_richieste=capoarea,stato=1,data_inizio_permesso = initPerm, data_fine_permesso=finePerm,
                    ora_inizio_permesso=oraInitPerm,ora_fine_permesso=oraFinePerm,id_creazione=capoarea.id_capo,data_creazione=timezone.now() + timezone.timedelta(hours=1))
                    richiesta_accettata.save()
        except Exception as error:
            print(error)

    def runDenyQuery(self, user, id_richiesta, *args, **kwargs):
        try:
            Richieste.objects.filter(pk=id_richiesta).update(stato=0)
            instance = Richieste.objects.get(pk=id_richiesta)
            instance = Richieste.objects.get(pk=id_richiesta)
            richiestaobj = Richieste.objects.get(pk=id_richiesta)
            dipendente = Richieste.objects.filter(pk=id_richiesta).values_list('id_dipendente_richiesta',flat=True)
            initPerm = instance.da_giorno_richiesta
            finePerm = instance.a_giorno_richiesta
            oraInitPerm = instance.da_ora_richiesta
            oraFinePerm = instance.a_ora_richiesta

            if RichiesteAccettate.objects.filter(id_richieste=richiestaobj).exists():
            
                if instance.id_permessi_richieste != None:
                    print("if deny")
                    codPerm = instance.id_permessi_richieste.id_permesso          
                    annoR=initPerm.year
                    meseR=initPerm.month
                    giornoR=initPerm.day
                    annoT=finePerm.year
                    meseT=finePerm.month
                    giornoT=finePerm.day
                    dippo=dipendente[0]

                    start_date = date(annoR, meseR, giornoR)
                    end_date = date(annoT, meseT, giornoT)
                    
                    for single_date in self.daterange(start_date, end_date):
                        annoC=single_date.year
                        meseC=single_date.month
                        giornoC=single_date.day
                        if instance.id_permessi_richieste:
                            updateIngresso = Ingressidip.objects.filter(giorno=single_date, id_dip_ing=dippo).update(id_permesso=id_richiesta,tipo_permesso=codPerm,in_permesso=1)
                        else: updateIngresso = Ingressidip.objects.filter(giorno=single_date, id_dip_ing=dippo).update(id_permesso=id_richiesta,tipo_permesso=None,in_permesso=0)
                        #dipendente = Richieste.objects.filter(pk=id_richiesta).values_list('id_dipendente_richiesta',flat=True)
                        try:
                            updateCedolini.delCedFunction(giornoC,meseC,annoC,dippo,codPerm)
                            print(f"done for {single_date} ")
                        except Exception as error:
                            print(error)
                    richieste_cancellate = RichiesteAccettate.objects.get(id_richieste=instance.id_richiesta)
                    richieste_cancellate.delete()     
                        
                
                elif instance.id_permessi_richieste == None:
                    oraR = oraInitPerm.hour
                    oraT = oraFinePerm.hour
                    codPerm = None        
                    annoR=initPerm.year
                    meseR=initPerm.month
                    giornoR=initPerm.day
                    annoT=finePerm.year
                    meseT=finePerm.month
                    giornoT=finePerm.day
                    dippo=dipendente[0]

                    start_date = date(annoR, meseR, giornoR)
                    end_date = date(annoT, meseT, giornoT)
                    
                    annoC=start_date.year
                    meseC=start_date.month
                    giornoC=start_date.day

                    updateIngresso = Ingressidip.objects.filter(giorno=start_date, id_dip_ing=dippo).update(id_permesso=None,tipo_permesso=codPerm,in_permesso=0)

                    try:
                        updateCedolini.delPermCedFunctionOra(giornoC,meseC,annoC,dippo,oraR,oraT,codPerm)
                        print(f"done for {start_date}",oraR,oraT)
                        richieste_cancellate = RichiesteAccettate.objects.get(id_richieste=instance.id_richiesta)
                        richieste_cancellate.delete()  
                    except Exception as error:
                        print(error)
            else:
                pass
        except Exception as error:
            print(error)
    

    def get(self, request, id_richiesta=None, *args, **kwargs):
        try:
            richiesta = Richieste.objects.get(pk=id_richiesta)
        except Exception as error:
            print(error)
        
        if id_richiesta is not None:
            richiesta = get_object_or_404(Richieste, id_richiesta=id_richiesta)
            context = {'richiesta':richiesta}
            
        try:
            if request.method == "GET" and request.GET.get("accept"):
                current_user = request.user
                user = current_user.id
                id_richiesta = request.GET["id"]
                self.runAcceptQuery(user,id_richiesta)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            elif request.method == "GET" and request.GET.get("deny"):
                current_user = request.user
                user = current_user.id
                id_richiesta = request.GET["id"]
                self.runDenyQuery(user,id_richiesta)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except Exception as error: 
            print(error)
            return HttpResponse("Torna indietro, qualcosa &#232; andato storto.")
        
        return render(request, self.template_name, context)


class AccettaStraordinari(LoginRequiredMixin,PermissionRequiredMixin,View):
    template_name = "capi_area/gestisci-richiesta-straordinari.html"
    context_object_name = 'richiesta'
    permission_required = 'capi_area.change_richiesteaccettate'
    fields = ['note','stato']

    def runAcceptQuery(self, user, id_straordinari, *args, **kwargs):
        try:
            instance = AddStraordinari.objects.get(pk=id_straordinari)
            dipendente = instance.id_dip
            giorno = instance.rel_giorno
            oraInit = instance.rel_time_start
            oraFine = instance.rel_time_end

            giornoC = instance.rel_giorno.day
            meseC = instance.rel_giorno.month
            annoC = instance.rel_giorno.year
            dippo = instance.id_dip
            ore = instance.ore
            
            if instance.stato == False or instance.stato == 2:
                try:
                    updateCedolini.cedStraordinari(giornoC,meseC,annoC,dippo,ore)
                except Exception as error:
                    print(error)
                    
                sameInstance = AddStraordinari.objects.filter(pk=id_straordinari).update(stato=1)
                
        except Exception as error:
            print(error)
            
    def runDenyQuery(self, user, id_straordinari, *args, **kwargs):
        try:
            instance = AddStraordinari.objects.get(pk=id_straordinari)
            dipendente = instance.id_dip
            giorno = instance.rel_giorno
            oraInit = instance.rel_time_start
            oraFine = instance.rel_time_end

            giornoC = instance.rel_giorno.day
            meseC = instance.rel_giorno.month
            annoC = instance.rel_giorno.year
            dippo = instance.id_dip
            
            if instance.stato == False or instance.stato == True:
                try:
                    updateCedolini.delCedStraordinari(giornoC,meseC,annoC,dippo)
                except Exception as error:
                    print(error)
                    
                sameInstance = AddStraordinari.objects.filter(pk=id_straordinari).update(stato=2)
                    
        except Exception as error:
            print(error)
    

    def get(self, request, id_straordinari=None, *args, **kwargs):
        try:
            richiesta = AddStraordinari.objects.get(pk=id_straordinari)
        except Exception as error:
            print(error)
        
        if id_straordinari is not None:
            richiesta = get_object_or_404(AddStraordinari, id_straordinari=id_straordinari)
            context = {'richiesta':richiesta}
        try:
            if request.method == "GET" and request.GET.get("accept"):
                current_user = request.user
                user = current_user.id
                id_straordinari = request.GET["id"]
                self.runAcceptQuery(user,id_straordinari)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            elif request.method == "GET" and request.GET.get("deny"):
                current_user = request.user
                user = current_user.id
                id_straordinari = request.GET["id"]
                self.runDenyQuery(user,id_straordinari)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        except Exception as error: 
            print(error)
            return HttpResponse("Torna indietro, qualcosa &#232; andato storto.")
        
        return render(request, self.template_name, context)

class RichiestaRespinta(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model= Richieste
    template_name = "reception/richiesta-respinta.html"
    context_object_name = 'respinta'
    permission_required = 'capi_area.change_richiesteaccettate'
