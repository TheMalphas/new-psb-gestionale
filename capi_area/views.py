from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from .models import Richieste, AuthUser, AnaDipendenti, CapoArea, Permessi, RichiesteAccettate, Ingressidip, Cedolini
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django import forms
from django.contrib import messages
from .forms import DipendentiForm, UpdateRichiestaForm, UpdateEntrata
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

#QR
@login_required
def printQR(request):
    dips=AnaDipendenti.objects.filter(stato="attivo").order_by("cognome")
    context={'dips':dips}
    
    if request.method == 'POST':
        input_data = request.POST['dipendente']
        response = HttpResponse(content_type='image/png')
        dippo = AnaDipendenti.objects.get(id_dip=input_data)
        fl = f'{dippo}'
        response['Content-Disposition'] = f'attachment; filename= "QR - {fl}".png'
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(response)
        return response
    
    return render(request,'capi_area/makeqr.html',context=context)

@login_required
@permission_required('capi_area.change_richiesteaccettate')
def dashboardCapoarea(request):
    today=datetime.now().date()
    template_name = "capi_area/dashboard-capo-area.html"
    anadipendente = AnaDipendenti.objects.get(user_id=request.user.pk)
    capoccione = CapoArea.objects.get(id_dipendente=anadipendente.id_dip)
    squadra = AnaDipendenti.objects.filter(id_capo_area=capoccione,stato="Attivo")
    listaIdSquadra = [el.id_dip for el in squadra]
    numeroSquadra = squadra.count()
    squadraPresente = Ingressidip.objects.filter(giorno=today,id_dip_ing__in=listaIdSquadra,timestamp_scan_entrata__isnull=False)
    numeroSquadraIngressi = [ing.id_dip_ing for ing in squadraPresente]
    squadraPresenteAna = AnaDipendenti.objects.filter(id_capo_area=capoccione,stato="Attivo",id_dip__in=numeroSquadraIngressi)
    squadraPresenteNumero = squadraPresente.count()
    richieste = Richieste.objects.filter(id_dipendente_richiesta__in=listaIdSquadra)
    richiesteNumero = richieste.count()
    richiestePermesso = richieste.filter().exclude(id_permessi_richieste=6).count()
    richiesteFerie = richieste.filter(id_permessi_richieste=6).count()

    return render(request,template_name,{"capoArea":capoccione,"squadra":squadra,"numeroSquadra":numeroSquadra,"squadraPresenteAna":squadraPresenteAna,"squadraPresenteNumero":squadraPresenteNumero,"richiesteNumero":richiesteNumero,"richiestePermesso":richiestePermesso,"richiesteFerie":richiesteFerie})
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

class Capi_AreaRichiesteAllList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    models = Richieste
    context_object_name = "richieste"
    template_name = "capi_area/richieste.html"
    permission_required = 'capi_area.change_richiesteaccettate'
    paginate_by = 8
    conta = None
    queryz = None
    
    def get_queryset(self):
        try:
            capo_area = CapoArea.objects.get(id_dipendente__user=self.request.user.pk)
        except CapoArea.DoesNotExist:
            raise PermissionDenied("Non sei un Capo Area.")
        if capo_area:
            queryset = Richieste.objects.filter(id_dipendente_richiesta__id_capo_area=capo_area).order_by("-a_giorno_richiesta").order_by('-timestamp')
            self.queryz = queryset
            query = self.request.GET.get("search-area") or ""
            conta = queryset.count()
            if query:
                return queryset.filter(nominativo__icontains=query)
            return queryset


    def get_context_data(self, **kwargs):
        if self.queryz != None:
            kwargs["conta"] = self.queryz.count()
        else: kwargs["conta"] = None
        return super().get_context_data(**kwargs)

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
    permission_required = 'capi_area.change_ingressidip'
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
    permission_required = 'capi_area.change_ingressidip'
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
    permission_required = 'capi_area.change_anadipendenti'
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

class RichiestaRespinta(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model= Richieste
    template_name = "reception/richiesta-respinta.html"
    context_object_name = 'respinta'
    permission_required = 'capi_area.change_ingressidip'
