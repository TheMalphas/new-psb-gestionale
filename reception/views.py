from django.http import HttpRequest, HttpResponse, HttpResponseRedirect,FileResponse, JsonResponse, Http404
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.db.models import Q
from django.views.generic import View,TemplateView
from django.urls import reverse, reverse_lazy
from .models import Richieste, AuthUser, AnaDipendenti, AppoggioVerificaQr, BancaOrari, CapoArea, Permessi, RichiesteAccettate, Ingressidip, Ritardi_Anticipi, Area, Societa, Sede
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.db import connections
from collections import namedtuple
from django import forms
from .forms import UpdateEntrata, UpdateUscita, UpdateDoppiaEntrata, UpdateDoppiaUscita, CreaEntrata, CreaEntrataDoppia, EntrateForm, UsciteForm
from datetime import time, datetime, timedelta,date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import redirect_to_login
from django.db.models import Count
from django.conf import settings
from wsgiref.util import FileWrapper
from docxtpl import DocxTemplate
import holidays
from workalendar.europe import Italy
from cedolini import settaggio_ore as so
from io import BytesIO
import requests
import io
import os
import json
import gc
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def getDashboardCompletaPresenze(request):
    today = datetime.now().date()
    template_name = "reception/datatables.html"
    return render(request,template_name,{'data':today})


class DashboardPresenzeView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/dashboard_presenze.html"
    today = datetime.now().date()
    def get(self,request,*args,**kwargs):
        
        ingressi = Ingressidip.objects.filter(giorno=self.today).count()
        context = {"tutti":ingressi}
                
        dipInPermesso = Ingressidip.objects.filter(giorno=self.today,in_permesso=True) 
        inpermesso = dipInPermesso.count()
        context["inpermesso"] = inpermesso
        
        inferie = dipInPermesso.filter(id_permesso=6).count()
        context["inferie"] = inferie
        
        tuttiDip = AnaDipendenti.objects.filter(stato="Attivo").count()
        context["numDipendenti"] = tuttiDip
        
        dipAttivi = Ingressidip.objects.filter(giorno=self.today, entrata__isnull=False)
        attivi = dipAttivi.count()
        context["attivi"] = attivi
        
        dipAssenti = Ingressidip.objects.filter(giorno=self.today, tipo="Assente")
        assenti=dipAssenti.count()
        context["assenti"] = assenti
        
        attiviAriano = dipAttivi.filter(id_dip_ing__sede__id_sede=1).count()
        context["attiviAriano"] = attiviAriano
        
        nonBadgiatoAriano = dipAttivi.filter(id_dip_ing__sede__id_sede=1,in_permesso=False).exclude(tipo="Assente").count()
        context["nonBadgiatoAriano"] = nonBadgiatoAriano
        
        inPermessoAriano = dipInPermesso.filter(id_dip_ing__sede__id_sede=1,in_permesso=True).count()
        context["inPermessoAriano"] = inPermessoAriano
        
        inFerieAriano = dipAssenti.filter(id_dip_ing__sede__id_sede=1,id_permesso=6,tipo="Ferie").count()
        context["inFerieAriano"] = inFerieAriano
        
        assentiAriano = dipAssenti.filter(id_dip_ing__sede__id_sede=1).count()
        context["assentiAriano"] = assentiAriano
        
        attiviBagnoli = dipAttivi.filter(id_dip_ing__sede__id_sede=8).count()
        context["attiviBagnoli"] = attiviBagnoli
        
        nonBadgiatoBagnoli = dipAttivi.filter(id_dip_ing__sede__id_sede=8,in_permesso=False).exclude(tipo="Assente").count()
        context["nonBadgiatoBagnoli"] = nonBadgiatoBagnoli
        
        inPermessoBagnoli = dipInPermesso.filter(id_dip_ing__sede__id_sede=8,in_permesso=True).count()
        context["inPermessoBagnoli"] = inPermessoBagnoli
        
        inFerieBagnoli = dipAssenti.filter(id_dip_ing__sede__id_sede=8,id_permesso=6,tipo="Ferie").count()
        context["inFerieBagnoli"] = inFerieBagnoli
        
        assentiBagnoli = dipAssenti.filter(id_dip_ing__sede__id_sede=8).count()
        context["assentiBagnoli"] = assentiBagnoli

        attiviMedina = dipAttivi.filter(id_dip_ing__sede__id_sede=9).count()
        context["attiviMedina"] = attiviMedina
        
        nonBadgiatoMedina = dipAttivi.filter(id_dip_ing__sede__id_sede=9,in_permesso=False).exclude(tipo="Assente").count()
        context["nonBadgiatoMedina"] = nonBadgiatoMedina

        inPermessoMedina = dipInPermesso.filter(id_dip_ing__sede__id_sede=9,in_permesso=True).count()
        context["inPermessoMedina"] = inPermessoMedina
        
        inFerieMedina = dipAssenti.filter(id_dip_ing__sede__id_sede=9,id_permesso=6,tipo="Ferie").count()
        context["inFerieMedina"] = inFerieMedina

        assentiMedina = dipAssenti.filter(id_dip_ing__sede__id_sede=9).count()
        context["assentiMedina"] = assentiMedina

        attiviNato = dipAttivi.filter(id_dip_ing__sede__id_sede=10).count()
        context["attiviNato"] = attiviNato
        
        nonBadgiatoNato = dipAttivi.filter(id_dip_ing__sede__id_sede=10,in_permesso=False).exclude(tipo="Assente").count()
        context["nonBadgiatoNato"] = nonBadgiatoNato
        
        inPermessoNato = dipInPermesso.filter(id_dip_ing__sede__id_sede=10,in_permesso=True).count()
        context["inPermessoNato"] = inPermessoNato
        
        inFerieNato = dipAssenti.filter(id_dip_ing__sede__id_sede=10,id_permesso=6,tipo="Ferie").count()
        context["inFerieNato"] = inFerieNato
        
        assentiNato = dipAssenti.filter(id_dip_ing__sede__id_sede=10).count()
        context["assentiNato"] = assentiNato

        attiviCampi = dipAttivi.filter(id_dip_ing__sede__id_sede=13).count()
        context["attiviCampi"] = attiviCampi
        
        nonBadgiatoCampi = dipAttivi.filter(id_dip_ing__sede__id_sede=13,in_permesso=False).exclude(tipo="Assente").count()
        context["nonBadgiatoCampi"] = nonBadgiatoCampi
        
        inPermessoCampi = dipInPermesso.filter(id_dip_ing__sede__id_sede=13,in_permesso=True).count()
        context["inPermessoCampi"] = inPermessoCampi
        
        inFerieCampi = dipAssenti.filter(id_dip_ing__sede__id_sede=13,id_permesso=6,tipo="Ferie").count()
        context["inFerieCampi"] = inFerieCampi
        
        assentiCampi = dipAssenti.filter(id_dip_ing__sede__id_sede=13).count()
        context["assentiCampi"] = assentiCampi

        context["data"] = self.today
        
        return render(request,self.template_name,context)


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('homepage')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

class ListaGiorniPresenzeDip(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Ingressidip
    context_object_name= "presenze"
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/presenze_dip.html"
    paginate_by = 31
    query = ""
    
    def get(self,request,*args,**kwargs):
        my_param = kwargs.get('id_dip_ing')
        anno = datetime.now().date().year
        giorniFestivi = so.getHolidays(int(anno))
        start_date_gen = date(2023, 1, 1)
        end_date_gen = date(2023, 1, 31)
        start_date_feb = date(2023, 2, 1)
        end_date_feb = date(2023, 2, 28)
        start_date_mar = date(2023, 3, 1)
        end_date_mar = date(2023, 3, 31)
        start_date_apr = date(2023, 4, 1)
        end_date_apr = date(2023, 4, 30)
        start_date_mag = date(2023, 5, 1)
        end_date_mag = date(2023, 5, 31)
        start_date_giu = date(2023, 6, 1)
        end_date_giu = date(2023, 6, 30)
        start_date_lug = date(2023, 7, 1)
        end_date_lug = date(2023, 7, 31)
        start_date_ago = date(2023, 8, 1)
        end_date_ago = date(2023, 8, 31)
        start_date_set = date(2023, 9, 1)
        end_date_set = date(2023, 9, 30)
        start_date_ott = date(2023, 10, 1)
        end_date_ott = date(2023, 10, 31)
        start_date_nov = date(2023, 11, 1)
        end_date_nov = date(2023, 11, 30)
        start_date_dic = date(2023, 12, 1)
        end_date_dic = date(2023, 12, 31)
        oggi = datetime.now().today().date()

        querysetGen = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_gen,end_date_gen)).order_by("-giorno")
        querysetDaysGen = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysGen.append((i.giorno,i.giorno.weekday(),"Dom"))
        context = {'presenzeGen':querysetGen}
        context["weekdaysGen"] = querysetDaysGen

        querysetFeb = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_feb,end_date_feb)).order_by("-giorno")
        querysetDaysFeb = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysFeb.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeFeb'] = querysetFeb
        context["weekdaysFeb"] = querysetDaysFeb
        
        querysetMar = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_mar,end_date_mar)).order_by("-giorno")
        querysetDaysMar = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysMar.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeMar'] = querysetMar
        context["weekdaysMar"] = querysetDaysMar
        
        querysetApr = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_apr,end_date_apr)).order_by("-giorno")
        querysetDaysApr = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysApr.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeApr'] = querysetApr
        context["weekdaysApr"] = querysetDaysApr
        
        querysetMag = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_mag,end_date_mag)).order_by("-giorno")
        querysetDaysMag = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysMag.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeMag'] = querysetMag
        context["weekdaysMag"] = querysetDaysMag
                
        querysetGiu = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_giu,end_date_giu)).order_by("-giorno")
        querysetDaysGiu = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysGiu.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeGiu'] = querysetGiu
        context["weekdaysGiu"] = querysetDaysGiu
        
                        
        querysetLug = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_lug,end_date_lug)).order_by("-giorno")
        querysetDaysLug = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysLug.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeLug'] = querysetLug
        context["weekdaysLug"] = querysetDaysLug
        
                        
        querysetAgo = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_ago,end_date_ago)).order_by("-giorno")
        querysetDaysAgo = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysAgo.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeAgo'] = querysetAgo
        context["weekdaysAgo"] = querysetDaysAgo
        
                        
        querysetSet = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_set,end_date_set)).order_by("-giorno")
        querysetDaysSet = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysSet.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeSet'] = querysetSet
        context["weekdaysSet"] = querysetDaysSet
        
                        
        querysetOtt = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_ott,end_date_ott)).order_by("-giorno")
        querysetDaysOtt = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysOtt.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeOtt'] = querysetOtt
        context["weekdaysOtt"] = querysetDaysOtt
        
                        
        querysetNov = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_nov,end_date_nov)).order_by("-giorno")
        querysetDaysNov = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysNov.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeNov'] = querysetNov
        context["weekdaysNov"] = querysetDaysNov
        
                        
        querysetDic = Ingressidip.objects.filter(id_dip_ing=my_param,giorno__range=(start_date_dic,end_date_dic)).order_by("-giorno")
        querysetDaysDic = []
        for i in querysetGen:
            if i.giorno.weekday() == 0:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Lun"))
            elif i.giorno.weekday() == 1:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Mar"))
            elif i.giorno.weekday() == 2:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Mer"))
            elif i.giorno.weekday() == 3:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Gio"))
            elif i.giorno.weekday() == 4:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Ven"))
            elif i.giorno.weekday() == 5:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Sab"))
            elif i.giorno.weekday() == 6:
                querysetDaysDic.append((i.giorno,i.giorno.weekday(),"Dom"))
        context['presenzeDic'] = querysetDic
        context["weekdaysDic"] = querysetDaysDic
        context["oggi"] = oggi
                
        return render(request,self.template_name,context)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_dip_ingresso = self.kwargs.get('id_dip_ing')
        query = AnaDipendenti.objects.get(id_dip=id_dip_ingresso)
        context['dipendente'] = query.cognome

        return context


class ListaPresenzeDip(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=AnaDipendenti
    context_object_name= "dipendenti"
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/presenze_per_dip.html"
    esclusioni = [9,23,24,26]
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
        queryset = AnaDipendenti.objects.filter(stato="Attivo").exclude(area__in=self.esclusioni).order_by("cognome")
        self.query = self.request.GET.get("dip") or ""
        if self.query:
            queryset = AnaDipendenti.objects.filter(stato="Attivo").filter(Q(nome__icontains=self.query) | Q(cognome__icontains=self.query)).order_by("cognome")
            return queryset
        return queryset

class CreaIngresso(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Ingressidip
    form_class = CreaEntrataDoppia
    context_object_name= "ingresso"
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/crea-ingresso.html"
    success_url= reverse_lazy('reception:presenze')
        
    def get_context_data(self, **kwargs):
        kwargs["CreaIngresso"] = self.get_form()
        return super().get_context_data(**kwargs)
    
class CreaIngressoDoppio(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Ingressidip
    form_class = CreaEntrataDoppia
    context_object_name= "ingresso"
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/crea-ingresso2.html"
    success_url= reverse_lazy('reception:presenze')
        
    def get_context_data(self, **kwargs):
        kwargs["CreaIngresso2"] = self.get_form()
        return super().get_context_data(**kwargs)

class DownloadReport(LoginRequiredMixin, PermissionRequiredMixin, View):
    model= Ingressidip
    permission_required = 'reception.change_ingressidip'
    template_name = "download_report"
    excludeIdList = [9,23,24,31,32]
    
    def get(self, request, *args, **kwargs):
        url = request.get_full_path()
        data = url[-10:]
        data = datetime.strptime(data, "%Y-%m-%d").date()
        datadoc = data
        datadoc = str(data) + ".docx"
        queryset = Ingressidip.objects.filter(giorno=data,id_dip_ing__stato='Attivo').exclude(id_dip_ing__area__in=self.excludeIdList).select_related("id_dip_ing").order_by("nominativo")

        context = {"presenze":queryset}
        context["totale_entrate"] = queryset.filter(giorno=data,checked_in=True).count()    
        context["totale_uscite"] = queryset.filter(giorno=data,checked_out=True).count()
        context["totale_assenze"] = queryset.filter(giorno=data,checked_in=False,in_permesso=False).count()
        context["totale_permessi"] = queryset.filter(giorno=data,checked_in=False,in_permesso=True).count()
        context["totale_assenze_area"] = queryset.filter(giorno=data, checked_in=False).count()
        context["totale_presenze_area"] = queryset.filter(giorno=data,checked_in=True).count()
        context["data"] = data.strftime("%d-%m-%Y")
        file_path = (settings.MEDIA_ROOT + '/docs/Report_Presenze.docx')
        doc = DocxTemplate(file_path)
        if doc:
            doc.render(context)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = "attachment; filename=Report_Presenze-%s" %(datadoc)
            doc.save(response)
            return response
        raise Http404


class DownloadRitardi(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'reception.change_ingressidip'
    template_name = "download_ritardi"
    
    def get(self, request, *args, **kwargs):
        url = request.get_full_path()
        data = url[-2:]
        mese = int(data)
        datadoc = data
        datadoc = str(data) + ".docx"
        query = "SELECT '1' as id, CAST(tempo AS CHAR) as tempo, LEFT(CAST(avg_tempo as CHAR),8) as avg_tempo FROM Ritardi_Anticipi WHERE mese = %s"
        ritardi = Ritardi_Anticipi.objects.raw(query, params=[mese])
        context = {'dipendenti':ritardi}
        context["month"] = mese
        context["ritardi"] = ritardi
        file_path = (settings.MEDIA_ROOT + '/docs/Ritardi_Mensili.docx')
        doc = DocxTemplate(file_path)
        if doc:
            doc.render(context)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = "attachment; filename=Ritardi_Mensili-%s" %(datadoc)
            doc.save(response)
            return response
        raise Http404

def getDipDay(self, id_dip_ing):
    richiesteDip = Richieste.objects.filter(id_dipendente_richiesta=id_dip_ing)
    richiesteAccettateDip = RichiesteAccettate.objects.raw("SELECT ID_Richiesta, nominativo, da_giorno_richiesta, da_ora_richiesta, a_giorno_richiesta a_ora_richiesta FROM Richieste JOIN Richieste_Accettate ON ID_richiesta = ID_richieste WHERE ID_dipendente_richiesta = %s", [id_dip_ing])

@login_required
@permission_required('reception.change_ingressidip')
def listaPresenze(request):
    today = datetime.now().date()
    excludeIdList = [9,23,24,31,32]
    template_name = "reception/presenze.html"

    if request.method == "POST" and request.POST.get("precedente") and request.POST.get("dipendente"):
        if request.POST.get("precedente"):
            data_object = request.POST.get("giorno")
            date = datetime.strptime(data_object, "%Y-%m-%d").date()
            date = (date - timedelta(1))
        else:
            data_object = datetime.now().date()
            date = (data_object - timedelta(1))
        dipendente = request.POST.get("dipendente")
        presenze = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').filter(Q(nominativo__icontains=dipendente)).exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=date,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=date,id_permesso=6).count()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":date})
    elif request.method == "POST" and (request.POST.get("precedente")):
        if request.POST.get("precedente"):
            data_object = request.POST.get("giorno")
            date = datetime.strptime(data_object, "%Y-%m-%d").date()
            date = (date - timedelta(1))
        else:
            data_object = datetime.now().date()
            date = (data_object - timedelta(1))
        presenze = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=date,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=date,id_permesso=6).count()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":date})
    
    elif request.method == "POST" and request.POST.get("successivo") and request.POST.get("dipendente"):
        if request.POST.get("giorno"):
            data_object = request.POST.get("giorno")
            date = datetime.strptime(data_object, "%Y-%m-%d").date()
            date = (date + timedelta(1))
        else:
            data_object = datetime.now().date()
            date = (data_object + timedelta(1))
        dipendente = request.POST.get("dipendente")
        presenze = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').filter(Q(nominativo__icontains=dipendente)).exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=date,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=date,id_permesso=6).count()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":date,"dipendente":dipendente})
    elif request.method == "POST" and request.POST.get("successivo"):
        if request.POST.get("giorno"):
            data_object = request.POST.get("giorno")
            date = datetime.strptime(data_object, "%Y-%m-%d").date()
            date = (date + timedelta(1))
        else:
            data_object = datetime.now().date()
            date = (data_object + timedelta(1))
        presenze = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=date,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=date,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=date,id_permesso=6).count()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":date})
    
    elif request.method == "POST" and request.POST.get("giorno"):
        data = request.POST.get("giorno") or today
        presenze = Ingressidip.objects.filter(giorno=today,id_dip_ing__stato='Attivo').exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=today,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=today,id_permesso=6).count()
        data = datetime.strptime(str(data), "%Y-%m-%d").date()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":data})
    
    elif request.method == "POST" and request.POST.get("dipendente"):
        dipendente = request.POST.get("dipendente")
        data_object = request.POST.get("giorno") or today
        date = datetime.strptime(str(data_object), "%Y-%m-%d").date()
        dip = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').filter(Q(nominativo__icontains=dipendente)).exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        presenze = Ingressidip.objects.filter(giorno=date,id_dip_ing__stato='Attivo').exclude(id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=today,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=today,id_permesso=6).count()
        return render(request, template_name, {"presenze":dip,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":today,"dipendente":dipendente})

    else:
        presenze = Ingressidip.objects.filter(giorno=today,id_dip_ing__stato='Attivo').exclude(in_permesso=True,id_dip_ing__area__in=excludeIdList).order_by("nominativo")
        totale_entrate = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False).count()
        totale_uscite = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=False,timestamp_scan_uscita__isnull=False).count()
        totale_assenze = presenze.filter(giorno=today,timestamp_scan_entrata__isnull=True,in_permesso=False).count()
        totale_permessi = presenze.filter(giorno=today,in_permesso=True).count()
        totale_ferie = presenze.filter(giorno=today,id_permesso=6).count()
        return render(request, template_name, {"presenze":presenze,"totale_entrate":totale_entrate,"totale_uscite":totale_uscite,"totale_assenze":totale_assenze,"totale_permessi":totale_permessi,"totale_ferie":totale_ferie,"data":today})


class EntrateQR(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Ingressidip
    permission_required = 'reception.change_ingressidip'
    template_name = "reception/entrate-qr.html"
    success_url= reverse_lazy('reception:entrate-qr')
    login_url = "/login/"
    redirect_field_name = REDIRECT_FIELD_NAME

    def checkTime(self,timer):
        datet = timer.date()
        timet = timer.time()
        now = datetime.now().today()
        checkdt = datetime.strptime(f'{str(datet)} {str(timet)}','%Y-%m-%d %H:%M:%S')
        checkNow = datetime.strptime(f'{str(now.date())} {str(now.time().hour)}:{str(now.time().minute)}:{str(now.time().second)}','%Y-%m-%d %H:%M:%S')
        nowNow = checkNow - checkdt
        nowCheck = nowNow.total_seconds()
        if nowCheck > 1800:
            del datet,timet,now,checkdt,checkNow,nowNow,nowCheck
            gc.collect()
            return True
        else: return False

    def registraPulizie(self, user, qr, request, context, *args, **kwargs):
        today = datetime.now().date()
        timestamp = datetime.now()
        
        try:
            if len(qr) == 36:
                if AppoggioVerificaQr.objects.get(uuid_qr=qr):
                    try: 
                        qr_row = AppoggioVerificaQr.objects.get(uuid_qr=qr)
                        
                        if qr_row:
                            dip = qr_row.id_dipendente
                            id_dip = dip.id_dip
                            dip = AnaDipendenti.objects.get(id_dip=id_dip)
                            cancelliere = AuthUser.objects.get(id=self.request.user.pk)
                            checkedIn = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today,checked_in=True).exists()
                            checkedOut = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today,checked_out=True).exists()
                            ingresso = Ingressidip.objects.get(id_dip_ing = id_dip, giorno=today)
                            timecheck_entrata = ingresso.timestamp_scan_entrata
                            timecheck_uscita = ingresso.timestamp_scan_uscita
                            
                            if not(checkedIn) and not(checkedOut) and not timecheck_entrata and not timecheck_uscita:
                                instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,entrata=timestamp,checked_in=True,timestamp_scan_entrata=timezone.now() + timezone.timedelta(hours=1))
                                dipendente = "dipendente"
                                entrato = "entrato"
                                context["dipendente"] = dipendente
                                context["dip"] = dip
                                context["entrato"] = entrato
                                return render(self.request,self.template_name,context)
                            
                            elif checkedIn and not(checkedOut) and timecheck_entrata and not(timecheck_uscita):
                                if checkedIn and not(checkedOut) and self.checkTime(timecheck_entrata):
                                    instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,uscita=timestamp,checked_in=False,checked_out=True,timestamp_scan_uscita=timezone.now() + timezone.timedelta(hours=1))
                                    dipendente = "dipendente"
                                    primaUscita = "primaUscita"
                                    if timestamp.hour < 17:
                                        context["dipendente"] = dipendente
                                        context["dip"] = dip
                                        context["primaUscita"] = primaUscita
                                        return render(self.request, self.template_name, context)
                                    else:
                                        secondaUscita = "secondaUscita"
                                        context["dipendente"] = dipendente
                                        context["dip"] = dip
                                        context["secondaUscita"] = secondaUscita
                                        return render(self.request, self.template_name, context)
                                else:
                                    # Warns of already registered user
                                    registratoEntrata = "registrato-entrata"
                                    context["registratoEntrata"] = registratoEntrata
                                    return render(self.request, self.template_name, context)

                            elif not(checkedIn) and checkedOut and self.checkTime(timecheck_entrata) and self.checkTime(timecheck_uscita):
                                if self.checkTime(timecheck_uscita):
                                    instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,seconda_entrata=timestamp,checked_in=True,checked_out=False,timestamp_scan_entrata=timezone.now() + timezone.timedelta(hours=1))
                                    dipendente = "dipendente"
                                    seconda_entrata = "seconda_entrata"
                                    context["dipendente"] = dipendente
                                    context["dip"] = dip
                                    context["seconda_entrata"] = seconda_entrata
                                    return render(self.request,self.template_name,context)
                                else:
                                    # Warns of already registered user
                                    registratoEntrata = "registrato-entrata"
                                    context["registratoEntrata"] = registratoEntrata
                                    del timecheck_entrata
                                    del timecheck_uscita
                                    gc.collect()
                                    return render(self.request, self.template_name, context)
                                
                            elif checkedIn and not(checkedOut) and self.checkTime(timecheck_entrata) and self.checkTime(timecheck_uscita):
                                if self.checkTime(timecheck_uscita):
                                    instance = Ingressidip.objects.filter(id_dip_ing=id_dip,giorno=today).update(registrato_da_user=cancelliere,seconda_uscita=timestamp,checked_out=True,timestamp_scan_uscita=timezone.now() + timezone.timedelta(hours=1))
                                    dipendente = "dipendente"
                                    secondaUscita = "secondaUscita"
                                    context["dipendente"] = dipendente
                                    context["dip"] = dip
                                    context["secondaUscita"] = secondaUscita
                                    return render(self.request,self.template_name,context)
                                else:
                                    # Warns of already registered user
                                    registratoUscita = "registrato-uscita"
                                    context["registratoUscita"] = registratoUscita
                                    return render(self.request, self.template_name, context)
                            
                            elif checkedIn and not(self.checkTime(timecheck_entrata)):
                                registratoEntrata = "registrato-entrata"
                                context["registratoEntrata"] = registratoEntrata
                                return render(self.request, self.template_name, context)
                            
                            elif checkedIn and checkedOut:
                                registratoUscita = "registrato-uscita"
                                context["registratoUscita"] = registratoUscita
                                return render(self.request, self.template_name, context)
                            else:
                                registratoUscita = "registrato-uscita"
                                context["registratoUscita"] = registratoUscita
                                return render(self.request,self.template_name,context)
                    except Exception as error:
                        errore= "Errore"
                        context["errore"] = errore
                        return render(self.request,self.template_name,context)   
            elif (len(qr) < 5 and len(qr) >= 1):
                if AnaDipendenti.objects.get(id_dip=qr):
                    try: 
                        id_dip_row = AnaDipendenti.objects.get(id_dip=qr)
                        id_dip = id_dip_row.id_dip
                        dip = AnaDipendenti.objects.get(id_dip=id_dip)
                        cancelliere = AuthUser.objects.get(id=self.request.user.pk)
                        checkedIn = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today,checked_in=True).exists()
                        checkedOut = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today,checked_out=True).exists()
                        ingresso = Ingressidip.objects.get(id_dip_ing = id_dip, giorno=today)
                        timecheck_entrata = ingresso.timestamp_scan_entrata
                        timecheck_uscita = ingresso.timestamp_scan_uscita
                        
                        if not(checkedIn) and not(checkedOut) and not timecheck_entrata and not timecheck_uscita:
                            instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,entrata=timestamp,checked_in=True,timestamp_scan_entrata=timezone.now() + timezone.timedelta(hours=1))
                            dipendente = "dipendente"
                            entrato = "entrato"
                            context["dipendente"] = dipendente
                            context["dip"] = dip
                            context["entrato"] = entrato
                            return render(self.request,self.template_name,context)
                        
                        elif checkedIn and not(checkedOut) and timecheck_entrata and not(timecheck_uscita):
                            if checkedIn and not(checkedOut) and self.checkTime(timecheck_entrata):
                                instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,uscita=timestamp,checked_in=False,checked_out=True,timestamp_scan_uscita=timezone.now() + timezone.timedelta(hours=1))
                                dipendente = "dipendente"
                                primaUscita = "primaUscita"
                                if timestamp.hour < 17:
                                    context["dipendente"] = dipendente
                                    context["dip"] = dip
                                    context["primaUscita"] = primaUscita
                                    return render(self.request, self.template_name, context)
                                else:
                                    secondaUscita = "secondaUscita"
                                    context["dipendente"] = dipendente
                                    context["dip"] = dip
                                    context["secondaUscita"] = secondaUscita
                                    return render(self.request, self.template_name, context)
                            else:
                                # Warns of already registered user
                                registratoEntrata = "registrato-entrata"
                                context["registratoEntrata"] = registratoEntrata
                                return render(self.request, self.template_name, context)

                        elif not(checkedIn) and checkedOut and self.checkTime(timecheck_entrata) and self.checkTime(timecheck_uscita):
                            if self.checkTime(timecheck_uscita):
                                instance = Ingressidip.objects.filter(id_dip_ing = id_dip, giorno=today).update(registrato_da_user=cancelliere,seconda_entrata=timestamp,checked_in=True,checked_out=False,timestamp_scan_entrata=timezone.now() + timezone.timedelta(hours=1))
                                dipendente = "dipendente"
                                seconda_entrata = "seconda_entrata"
                                context["dipendente"] = dipendente
                                context["dip"] = dip
                                context["seconda_entrata"] = seconda_entrata
                                return render(self.request,self.template_name,context)
                            else:
                                # Warns of already registered user
                                registratoEntrata = "registrato-entrata"
                                context["registratoEntrata"] = registratoEntrata
                                del timecheck_entrata
                                del timecheck_uscita
                                gc.collect()
                                return render(self.request, self.template_name, context)
                            
                        elif checkedIn and not(checkedOut) and self.checkTime(timecheck_entrata) and self.checkTime(timecheck_uscita):
                            if self.checkTime(timecheck_uscita):
                                instance = Ingressidip.objects.filter(id_dip_ing=id_dip,giorno=today).update(registrato_da_user=cancelliere,seconda_uscita=timestamp,checked_out=True,timestamp_scan_uscita=timezone.now() + timezone.timedelta(hours=1))
                                dipendente = "dipendente"
                                secondaUscita = "secondaUscita"
                                context["dipendente"] = dipendente
                                context["dip"] = dip
                                context["secondaUscita"] = secondaUscita
                                return render(self.request,self.template_name,context)
                            else:
                                # Warns of already registered user
                                registratoUscita = "registrato-uscita"
                                context["registratoUscita"] = registratoUscita
                                return render(self.request, self.template_name, context)
                        
                        elif checkedIn and not(self.checkTime(timecheck_entrata)):
                            registratoEntrata = "registrato-entrata"
                            context["registratoEntrata"] = registratoEntrata
                            return render(self.request, self.template_name, context)
                        
                        elif checkedIn and checkedOut:
                            registratoUscita = "registrato-uscita"
                            context["registratoUscita"] = registratoUscita
                            return render(self.request, self.template_name, context)
                        else:
                            registratoUscita = "registrato-uscita"
                            context["registratoUscita"] = registratoUscita
                            return render(self.request,self.template_name,context)
                    except Exception as error:
                        errore= "Errore"
                        context["errore"] = errore
                        return render(self.request,self.template_name,context)
            else:
                errore= "Errore"
                context["errore"] = errore
                return render(self.request,self.template_name,context)
        except Exception as error:
            errore= "Errore"
            context["errore"] = errore
            return render(self.request,self.template_name,context)
        

    def post(self, request, id_dip_ing=None, *args, **kwargs):
        ingressi = Ingressidip.objects.filter()
        context = {"ingressi":ingressi}

        try:
            qr = request.POST["qr"]     
            if request.method == "POST" and request.POST.get("qr"):
                current_user = request.user
                user = current_user.id
                self.registraPulizie(user, qr, request, context)
                return render(request, self.template_name, context)
            else: 
                return render(request, self.template_name, context)
        except Exception as err:
            print(err) 
        return render(request, self.template_name, context)

