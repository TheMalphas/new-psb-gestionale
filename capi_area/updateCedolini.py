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
from django.db.models import Count, F, Value
import qrcode
from django.core.exceptions import PermissionDenied
from io import BytesIO

def cedFunction(self,giornoC,meseC,annoC,dippo,codPerm=None):
    dip=AnaDipendenti.objects.get(id_dip=dippo)
    if giornoC == 1 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_01=8,ord_01=None)
    if giornoC == 1 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_01=8,ord_01=None)
    if giornoC == 2 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_02=8,ord_02=None)
    if giornoC == 2 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_02=8,ord_02=None)
    if giornoC == 3 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_03=8,ord_03=None)
    if giornoC == 3 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_03=8,ord_03=None)
    if giornoC == 4 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_04=8,ord_04=None)
    if giornoC == 4 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_04=8,ord_04=None)
    if giornoC == 5 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_05=8,ord_05=None)
    if giornoC == 5 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_05=8,ord_05=None)
    if giornoC == 6 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_06=8,ord_06=None)
    if giornoC == 6 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_06=8,ord_06=None)
    if giornoC == 7 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_07=8,ord_07=None)
    if giornoC == 7 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_07=8,ord_07=None)
    if giornoC == 8 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_08=8,ord_08=None)
    if giornoC == 8 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_08=8,ord_08=None)
    if giornoC == 9 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_09=8,ord_09=None)
    if giornoC == 9 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_09=8,ord_09=None)
    if giornoC == 10 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=8,ord_10=None)
    if giornoC == 10 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=8,ord_10=None)
    if giornoC == 11 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_11=8,ord_11=None)
    if giornoC == 11 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_11=8,ord_11=None)
    if giornoC == 12 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_12=8,ord_12=None)
    if giornoC == 12 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_12=8,ord_12=None)
    if giornoC == 13 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_13=8,ord_13=None)
    if giornoC == 13 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_13=8,ord_13=None)
    if giornoC == 14 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_14=8,ord_14=None)
    if giornoC == 14 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_14=8,ord_14=None)
    if giornoC == 15 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_15=8,ord_15=None)
    if giornoC == 15 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_15=8,ord_15=None)
    if giornoC == 16 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_16=8,ord_16=None)
    if giornoC == 16 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_16=8,ord_16=None)
    if giornoC == 17 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_17=8,ord_17=None)
    if giornoC == 17 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_17=8,ord_17=None)
    if giornoC == 18 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_18=8,ord_18=None)
    if giornoC == 18 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_18=8,ord_18=None)
    if giornoC == 19 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_19=8,ord_19=None)
    if giornoC == 19 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_19=8,ord_19=None)
    if giornoC == 20 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_20=8,ord_20=None)
    if giornoC == 20 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_20=8,ord_20=None)
    if giornoC == 21 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_21=8,ord_21=None)
    if giornoC == 21 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_21=8,ord_21=None)
    if giornoC == 22 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_22=8,ord_22=None)
    if giornoC == 22 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_22=8,ord_22=None)
    if giornoC == 23 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_23=8,ord_23=None)
    if giornoC == 23 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_23=8,ord_23=None)
    if giornoC == 24 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_24=8,ord_24=None)
    if giornoC == 24 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_24=8,ord_24=None)
    if giornoC == 25 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_25=8,ord_25=None)
    if giornoC == 25 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_25=8,ord_25=None)
    if giornoC == 26 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_26=8,ord_26=None)
    if giornoC == 26 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_26=8,ord_26=None)
    if giornoC == 27 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_27=8,ord_27=None)
    if giornoC == 27 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_27=8,ord_27=None)
    if giornoC == 28 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_28=8,ord_28=None)
    if giornoC == 28 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_28=8,ord_28=None)
    if giornoC == 29 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_29=8,ord_29=None)
    if giornoC == 29 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_29=8,ord_29=None)
    if giornoC == 30 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_30=8,ord_30=None)
    if giornoC == 30 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_30=8,ord_30=None)
    if giornoC == 31 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_31=8,ord_31=None)
    if giornoC == 31 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_31=8,ord_31=None)

def delPermCedFunctionOra(self,giornoC,meseC,annoC,dippo,oraR,oraT,codPerm=None):
    dip=AnaDipendenti.objects.get(id_dip=dippo)
    if giornoC == 1 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_01=F('perm_01')-(aggiorna),ord_01=F('ord_01')+(aggiorna))
    if giornoC == 1 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_01=F('fer_01')-(aggiorna),ord_01=F('ord_01')+(aggiorna))
    if giornoC == 2 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_02=F('perm_02')-(aggiorna),ord_02=F('ord_02')+(aggiorna))
    if giornoC == 2 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_02=F('fer_02')-(aggiorna),ord_02=F('ord_02')+(aggiorna))
    if giornoC == 3 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_03=F('perm_03')-(aggiorna),ord_03=F('ord_03')+(aggiorna))
    if giornoC == 3 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_03=F('fer_03')-(aggiorna),ord_03=F('ord_03')+(aggiorna))
    if giornoC == 4 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_04=F('perm_04')-(aggiorna),ord_04=F('ord_04')+(aggiorna))
    if giornoC == 4 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_04=F('fer_04')-(aggiorna),ord_04=F('ord_04')+(aggiorna))
    if giornoC == 5 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_05=F('perm_05')-(aggiorna),ord_05=F('ord_05')+(aggiorna))
    if giornoC == 5 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_05=F('fer_05')-(aggiorna),ord_05=F('ord_05')+(aggiorna))
    if giornoC == 6 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_06=F('perm_06')-(aggiorna),ord_06=F('ord_06')+(aggiorna))
    if giornoC == 6 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_06=F('fer_06')-(aggiorna),ord_06=F('ord_06')+(aggiorna))
    if giornoC == 7 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_07=F('perm_07')-(aggiorna),ord_07=F('ord_07')+(aggiorna))
    if giornoC == 7 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_07=F('fer_07')-(aggiorna),ord_07=F('ord_07')+(aggiorna))
    if giornoC == 8 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_08=F('perm_08')-(aggiorna),ord_08=F('ord_08')+(aggiorna))
    if giornoC == 8 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_08=F('fer_08')-(aggiorna),ord_08=F('ord_08')+(aggiorna))
    if giornoC == 9 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_09=F('perm_09')-(aggiorna),ord_09=F('ord_09')+(aggiorna))
    if giornoC == 9 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_09=F('fer_09')-(aggiorna),ord_09=F('ord_09')+(aggiorna))
    if giornoC == 10 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_10=F('perm_10')-(aggiorna),ord_09=F('ord_10')+(aggiorna))
    if giornoC == 10 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=F('fer_10')-(aggiorna),ord_10=F('ord_10')+(aggiorna))
    if giornoC == 11 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_11=F('perm_11')-(aggiorna),ord_11=F('ord_11')+(aggiorna))
    if giornoC == 11 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_11=F('fer_11')-(aggiorna),ord_11=F('ord_11')+(aggiorna))
    if giornoC == 12 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_12=F('perm_12')-(aggiorna),ord_12=F('ord_12')+(aggiorna))
    if giornoC == 12 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_12=F('fer_12')-(aggiorna),ord_12=F('ord_12')+(aggiorna))
    if giornoC == 13 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_13=F('perm_13')-(aggiorna),ord_13=F('ord_13')+(aggiorna))
    if giornoC == 13 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_13=F('fer_13')-(aggiorna),ord_13=F('ord_13')+(aggiorna))
    if giornoC == 14 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_14=F('perm_14')-(aggiorna),ord_14=F('ord_14')+(aggiorna))
    if giornoC == 14 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_14=F('fer_14')-(aggiorna),ord_14=F('ord_14')+(aggiorna))
    if giornoC == 15 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_15=F('perm_15')-(aggiorna),ord_15=F('ord_15')+(aggiorna))
    if giornoC == 15 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_15=F('fer_15')-(aggiorna),ord_15=F('ord_15')+(aggiorna))
    if giornoC == 16 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_16=F('perm_16')-(aggiorna),ord_16=F('ord_16')+(aggiorna))
    if giornoC == 16 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_16=F('fer_16')-(aggiorna),ord_16=F('ord_16')+(aggiorna))
    if giornoC == 17 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_17=F('perm_17')-(aggiorna),ord_17=F('ord_17')+(aggiorna))
    if giornoC == 17 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_17=F('fer_17')-(aggiorna),ord_17=F('ord_17')+(aggiorna))
    if giornoC == 18 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_18=F('perm_18')-(aggiorna),ord_18=F('ord_18')+(aggiorna))
    if giornoC == 18 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_18=F('fer_18')-(aggiorna),ord_18=F('ord_18')+(aggiorna))
    if giornoC == 19 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_19=F('perm_19')-(aggiorna),ord_19=F('ord_19')+(aggiorna))
    if giornoC == 19 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_19=F('fer_19')-(aggiorna),ord_19=F('ord_19')+(aggiorna))
    if giornoC == 20 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_20=F('perm_20')-(aggiorna),ord_20=F('ord_20')+(aggiorna))
    if giornoC == 20 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_20=F('fer_20')-(aggiorna),ord_20=F('ord_20')+(aggiorna))
    if giornoC == 21 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_21=F('perm_21')-(aggiorna),ord_21=F('ord_21')+(aggiorna))
    if giornoC == 21 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_21=F('fer_21')-(aggiorna),ord_21=F('ord_21')+(aggiorna))
    if giornoC == 22 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_22=F('perm_22')-(aggiorna),ord_22=F('ord_22')+(aggiorna))
    if giornoC == 22 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_22=F('fer_22')-(aggiorna),ord_22=F('ord_22')+(aggiorna))
    if giornoC == 23 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_23=F('perm_23')-(aggiorna),ord_23=F('ord_23')+(aggiorna))
    if giornoC == 23 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_23=F('fer_23')-(aggiorna),ord_23=F('ord_23')+(aggiorna))
    if giornoC == 24 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_24=F('perm_24')-(aggiorna),ord_24=F('ord_24')+(aggiorna))
    if giornoC == 24 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_24=F('fer_24')-(aggiorna),ord_24=F('ord_24')+(aggiorna))
    if giornoC == 25 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_25=F('perm_25')-(aggiorna),ord_25=F('ord_25')+(aggiorna))
    if giornoC == 25 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_25=F('fer_25')-(aggiorna),ord_25=F('ord_25')+(aggiorna))
    if giornoC == 26 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_26=F('perm_26')-(aggiorna),ord_26=F('ord_26')+(aggiorna))
    if giornoC == 26 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_26=F('fer_26')-(aggiorna),ord_26=F('ord_26')+(aggiorna))
    if giornoC == 27 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_27=F('perm_27')-(aggiorna),ord_27=F('ord_27')+(aggiorna))
    if giornoC == 27 and codPerm == 6:
        aggiorna = oraT-oraR
        print(oraT-oraR,aggiorna)
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_27=F('fer_27')-(aggiorna),ord_27=F('ord_27')+(aggiorna))
    if giornoC == 28 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_28=F('perm_28')-(aggiorna),ord_28=F('ord_28')+(aggiorna))
    if giornoC == 28 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_28=F('fer_28')-(aggiorna),ord_28=F('ord_28')+(aggiorna))
    if giornoC == 29 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_29=F('perm_29')-(aggiorna),ord_29=F('ord_29')+(aggiorna))
    if giornoC == 29 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_29=F('fer_29')-(aggiorna),ord_29=F('ord_29')+(aggiorna))
    if giornoC == 30 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_30=F('perm_30')-(aggiorna),ord_30=F('ord_30')+(aggiorna))
    if giornoC == 30 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_30=F('fer_30')-(aggiorna),ord_30=F('ord_30')+(aggiorna))
    if giornoC == 31 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_31=F('perm_31')-(aggiorna),ord_31=F('ord_31')+(aggiorna))
    if giornoC == 31 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_31=F('fer_031')-(aggiorna),ord_31=F('ord_31')+(aggiorna))

def addPermCedFunctionOra(self,giornoC,meseC,annoC,dippo,oraR,oraT,codPerm=None):
    dip=AnaDipendenti.objects.get(id_dip=dippo)
    if giornoC == 1 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_01=aggiorna,ord_01=F('ord_01')-(aggiorna))
    if giornoC == 1 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_01=aggiorna,ord_01=F('ord_01')-(aggiorna))
    if giornoC == 2 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_02=aggiorna,ord_02=F('ord_02')-(aggiorna))
    if giornoC == 2 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_02=aggiorna,ord_02=F('ord_02')-(aggiorna))
    if giornoC == 3 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_03=aggiorna,ord_03=F('ord_03')-(aggiorna))
    if giornoC == 3 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_03=aggiorna,ord_03=F('ord_03')-(aggiorna))
    if giornoC == 4 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_04=aggiorna,ord_04=F('ord_04')-(aggiorna))
    if giornoC == 4 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_04=aggiorna,ord_04=F('ord_04')-(aggiorna))
    if giornoC == 5 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_05=aggiorna,ord_05=F('ord_05')-(aggiorna))
    if giornoC == 5 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_05=aggiorna,ord_05=F('ord_05')-(aggiorna))
    if giornoC == 6 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_06=aggiorna,ord_06=F('ord_06')-(aggiorna))
    if giornoC == 6 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_06=aggiorna,ord_06=F('ord_06')-(aggiorna))
    if giornoC == 7 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_07=aggiorna,ord_07=F('ord_07')-(aggiorna))
    if giornoC == 7 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_07=aggiorna,ord_07=F('ord_07')-(aggiorna))
    if giornoC == 8 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_08=aggiorna,ord_08=F('ord_08')-(aggiorna))
    if giornoC == 8 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_08=aggiorna,ord_08=F('ord_08')-(aggiorna))
    if giornoC == 9 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_09=aggiorna,ord_09=F('ord_09')-(aggiorna))
    if giornoC == 9 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_09=aggiorna,ord_09=F('ord_09')-(aggiorna))
    if giornoC == 10 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_10=aggiorna,ord_10=F('ord_10')-(aggiorna))
    if giornoC == 10 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=aggiorna,ord_10=F('ord_10')-(aggiorna))
    if giornoC == 11 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_11=aggiorna,ord_11=F('ord_11')-(aggiorna))
    if giornoC == 11 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_11=aggiorna,ord_11=F('ord_11')-(aggiorna))
    if giornoC == 12 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_12=aggiorna,ord_12=F('ord_12')-(aggiorna))
    if giornoC == 12 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_12=aggiorna,ord_12=F('ord_12')-(aggiorna))
    if giornoC == 13 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_13=aggiorna,ord_13=F('ord_13')-(aggiorna))
    if giornoC == 13 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_13=aggiorna,ord_13=F('ord_13')-(aggiorna))
    if giornoC == 14 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_14=aggiorna,ord_14=F('ord_14')-(aggiorna))
    if giornoC == 14 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_14=aggiorna,ord_14=F('ord_14')-(aggiorna))
    if giornoC == 15 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_15=aggiorna,ord_15=F('ord_15')-(aggiorna))
    if giornoC == 15 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_15=aggiorna,ord_15=F('ord_15')-(aggiorna))
    if giornoC == 16 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_16=aggiorna,ord_16=F('ord_16')-(aggiorna))
    if giornoC == 16 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_16=aggiorna,ord_16=F('ord_16')-(aggiorna))
    if giornoC == 17 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_17=aggiorna,ord_17=F('ord_17')-(aggiorna))
    if giornoC == 17 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_17=aggiorna,ord_17=F('ord_17')-(aggiorna))
    if giornoC == 18 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_18=aggiorna,ord_18=F('ord_18')-(aggiorna))
    if giornoC == 18 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_18=aggiorna,ord_18=F('ord_18')-(aggiorna))
    if giornoC == 19 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_19=aggiorna,ord_19=F('ord_19')-(aggiorna))
    if giornoC == 19 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_19=aggiorna,ord_19=F('ord_19')-(aggiorna))
    if giornoC == 20 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_20=aggiorna,ord_20=F('ord_20')-(aggiorna))
    if giornoC == 20 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_20=aggiorna,ord_20=F('ord_20')-(aggiorna))
    if giornoC == 21 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_21=aggiorna,ord_21=F('ord_21')-(aggiorna))
    if giornoC == 21 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_21=aggiorna,ord_21=F('ord_21')-(aggiorna))
    if giornoC == 22 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_22=aggiorna,ord_22=F('ord_22')-(aggiorna))
    if giornoC == 22 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_22=aggiorna,ord_22=F('ord_22')-(aggiorna))
    if giornoC == 23 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_23=aggiorna,ord_23=F('ord_23')-(aggiorna))
    if giornoC == 23 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_23=aggiorna,ord_23=F('ord_23')-(aggiorna))
    if giornoC == 24 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_24=aggiorna,ord_24=F('ord_24')-(aggiorna))
    if giornoC == 24 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_24=aggiorna,ord_24=F('ord_24')-(aggiorna))
    if giornoC == 25 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_25=aggiorna,ord_25=F('ord_25')-(aggiorna))
    if giornoC == 25 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_25=aggiorna,ord_25=F('ord_25')-(aggiorna))
    if giornoC == 26 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_26=aggiorna,ord_26=F('ord_26')-(aggiorna))
    if giornoC == 26 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_26=aggiorna,ord_26=F('ord_26')-(aggiorna))
    if giornoC == 27 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_27=aggiorna,ord_27=F('ord_27')-(aggiorna))
    if giornoC == 27 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_27=aggiorna,ord_27=F('ord_27')-(aggiorna))
    if giornoC == 28 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_28=aggiorna,ord_28=F('ord_28')-(aggiorna))
    if giornoC == 28 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_28=aggiorna,ord_28=F('ord_28')-(aggiorna))
    if giornoC == 29 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_29=aggiorna,ord_29=F('ord_29')-(aggiorna))
    if giornoC == 29 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_29=aggiorna,ord_29=F('ord_29')-(aggiorna))
    if giornoC == 30 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_30=aggiorna,ord_30=F('ord_30')-(aggiorna))
    if giornoC == 30 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_30=aggiorna,ord_30=F('ord_30')-(aggiorna))
    if giornoC == 31 and codPerm != 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_31=aggiorna,ord_31=F('ord_31')-(aggiorna))
    if giornoC == 31 and codPerm == 6:
        aggiorna = oraT-oraR
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_31=aggiorna,ord_31=F('ord_31')-(aggiorna))

def delCedFunction(self,giornoC,meseC,annoC,dippo,codPerm=None):
    dip=AnaDipendenti.objects.get(id_dip=dippo)
    if giornoC == 1 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_01=None,ord_01=8)
    if giornoC == 1 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_01=None,ord_01=8)
    if giornoC == 2 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_02=None,ord_02=8)
    if giornoC == 2 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_02=None,ord_02=8)
    if giornoC == 3 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_03=None,ord_03=8)
    if giornoC == 3 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_03=None,ord_03=8)
    if giornoC == 4 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_04=None,ord_04=8)
    if giornoC == 4 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_04=None,ord_04=8)
    if giornoC == 5 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_05=None,ord_05=8)
    if giornoC == 5 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_05=None,ord_05=8)
    if giornoC == 6 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_06=None,ord_06=8)
    if giornoC == 6 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_06=None,ord_06=8)
    if giornoC == 7 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_07=None,ord_07=8)
    if giornoC == 7 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_07=None,ord_07=8)
    if giornoC == 8 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_08=None,ord_08=8)
    if giornoC == 8 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_08=None,ord_08=8)
    if giornoC == 9 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_09=None,ord_09=8)
    if giornoC == 9 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_09=None,ord_09=8)
    if giornoC == 10 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=None,ord_10=8)
    if giornoC == 10 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_10=None,ord_10=8)
    if giornoC == 11 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_11=None,ord_11=8)
    if giornoC == 11 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_11=None,ord_11=8)
    if giornoC == 12 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_12=None,ord_12=8)
    if giornoC == 12 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_12=None,ord_12=8)
    if giornoC == 13 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_13=None,ord_13=8)
    if giornoC == 13 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_13=None,ord_13=8)
    if giornoC == 14 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_14=None,ord_14=8)
    if giornoC == 14 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_14=None,ord_14=8)
    if giornoC == 15 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_15=None,ord_15=8)
    if giornoC == 15 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_15=None,ord_15=8)
    if giornoC == 16 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_16=None,ord_16=8)
    if giornoC == 16 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_16=None,ord_16=8)
    if giornoC == 17 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_17=None,ord_17=8)
    if giornoC == 17 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_17=None,ord_17=8)
    if giornoC == 18 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_18=None,ord_18=8)
    if giornoC == 18 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_18=None,ord_18=8)
    if giornoC == 19 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_19=None,ord_19=8)
    if giornoC == 19 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_19=None,ord_19=8)
    if giornoC == 20 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_20=None,ord_20=8)
    if giornoC == 20 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_20=None,ord_20=8)
    if giornoC == 21 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_21=None,ord_21=8)
    if giornoC == 21 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_21=None,ord_21=8)
    if giornoC == 22 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_22=None,ord_22=8)
    if giornoC == 22 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_22=None,ord_22=8)
    if giornoC == 23 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_23=None,ord_23=8)
    if giornoC == 23 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_23=None,ord_23=8)
    if giornoC == 24 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_24=None,ord_24=8)
    if giornoC == 24 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_24=None,ord_24=8)
    if giornoC == 25 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_25=None,ord_25=8)
    if giornoC == 25 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_25=None,ord_25=8)
    if giornoC == 26 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_26=None,ord_26=8)
    if giornoC == 26 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_26=None,ord_26=8)
    if giornoC == 27 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_27=None,ord_27=8)
    if giornoC == 27 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_27=None,ord_27=8)
    if giornoC == 28 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_28=None,ord_28=8)
    if giornoC == 28 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_28=None,ord_28=8)
    if giornoC == 29 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_29=None,ord_29=8)
    if giornoC == 29 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_29=None,ord_29=8)
    if giornoC == 30 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_30=None,ord_30=8)
    if giornoC == 30 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_30=None,ord_30=8)
    if giornoC == 31 and codPerm != 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(perm_31=None,ord_31=8)
    if giornoC == 31 and codPerm == 6:
        return Cedolini.objects.filter(dipendente=dip,mese=meseC,anno=annoC).update(fer_31=None,ord_31=8)