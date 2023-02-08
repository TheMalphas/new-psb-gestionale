from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cedolini as ced
from django.contrib.auth.decorators import permission_required, login_required
from datetime import datetime, date, timedelta
import pandas as pd
import holidays
from workalendar.europe import Italy
from . import settaggio_ore as so



@login_required
@csrf_exempt 
def setOre(request,id_cedolino):
    id=id_cedolino
    if request.POST.get('id') == "azzera":
        relMese=int(request.POST.get('name')[-7:-5])
        if str(relMese)[0:1] == "-":
            relMese = int(request.POST.get('name')[-6:-5])
        relAnno=int(request.POST.get('name')[-4:])
        print(relMese, relAnno)

        lista = so.getDay(relMese,relAnno)
        firstDay = lista[0]
        lastDay = lista[1]
        daysRange = so.getRangeDate(firstDay,lastDay)
        calendario = so.getHolidays(relAnno)
        queryRange = so.getQuery(daysRange,calendario)
        
        so.activateQueryAzzera(id)
        
    if request.POST.get('id') == "full":
        relMese=int(request.POST.get('name')[-7:-5])
        if str(relMese)[0:1] == "-":
            relMese = int(request.POST.get('name')[-6:-5])
        relAnno=int(request.POST.get('name')[-4:])

        lista = so.getDay(relMese,relAnno)
        firstDay = lista[0]
        lastDay = lista[1]
        daysRange = so.getRangeDate(firstDay,lastDay)
        calendario = so.getHolidays(relAnno)
        queryRange = so.getQuery(daysRange,calendario)
        
        so.activateQueryFull(queryRange,id)
        
    if request.POST.get('id') == "part" and request.POST.get('perc') != 'Perc':
        relMese=int(request.POST.get('name')[-7:-5])
        if str(relMese)[0:1] == "-":
            relMese = int(request.POST.get('name')[-6:-5])
        relAnno=int(request.POST.get('name')[-4:])
        perc=request.POST.get('perc')

        lista = so.getDay(relMese,relAnno)
        firstDay = lista[0]
        lastDay = lista[1]
        daysRange = so.getRangeDate(firstDay,lastDay)
        calendario = so.getHolidays(relAnno)
        queryRange = so.getQuery(daysRange,calendario)
        
        so.activateQueryPerc(queryRange,id,perc)
        
    return JsonResponse({"success":"Aggiornato"})

@login_required
@csrf_exempt
def getCedolino(request):
    cedolino = ced.objects.filter(id_cedolino=request.POST.get('id_cedolino'))
    cedolino_obj=serializers.serialize('python',cedolino)
    return JsonResponse(cedolino_obj,safe=False)

@login_required
@csrf_exempt
def saveCedolino(request,id_cedolino):
    id=id_cedolino
    print(id_cedolino)
    tipo=request.POST.get('type','')
    value=request.POST.get('value','')
    value=float(value)
    cedolino=ced.objects.get(id_cedolino=id)
    if tipo == 'ord_01':
        cedolino.ord_01=value
    if tipo == 'ord_02':
        cedolino.ord_02=value
    if tipo == 'ord_03':
        cedolino.ord_03=value
    if tipo == 'ord_04':
        cedolino.ord_04=value
    if tipo == 'ord_05':
        cedolino.ord_05=value
    if tipo == 'ord_06':
        cedolino.ord_06=value
    if tipo == 'ord_07':
        cedolino.ord_07=value
    if tipo == 'ord_08':
        cedolino.ord_08=value
    if tipo == 'ord_09':
        cedolino.ord_09=value
    if tipo == 'ord_10':
        cedolino.ord_10=value
    if tipo == 'ord_11':
        cedolino.ord_11=value
    if tipo == 'ord_12':
        cedolino.ord_12=value
    if tipo == 'ord_13':
        cedolino.ord_13=value
    if tipo == 'ord_14':
        cedolino.ord_14=value
    if tipo == 'ord_15':
        cedolino.ord_15=value
    if tipo == 'ord_16':
        cedolino.ord_16=value
    if tipo == 'ord_17':
        cedolino.ord_17=value
    if tipo == 'ord_18':
        cedolino.ord_18=value
    if tipo == 'ord_19':
        cedolino.ord_19=value
    if tipo == 'ord_20':
        cedolino.ord_20=value
    if tipo == 'ord_21':
        cedolino.ord_21=value
    if tipo == 'ord_22':
        cedolino.ord_22=value
    if tipo == 'ord_23':
        cedolino.ord_23=value
    if tipo == 'ord_24':
        cedolino.ord_24=value
    if tipo == 'ord_25':
        cedolino.ord_25=value
    if tipo == 'ord_26':
        cedolino.ord_26=value
    if tipo == 'ord_27':
        cedolino.ord_27=value
    if tipo == 'ord_28':
        cedolino.ord_28=value
    if tipo == 'ord_29':
        cedolino.ord_29=value
    if tipo == 'ord_30':
        cedolino.ord_30=value
    if tipo == 'ord_31':
        cedolino.ord_31=value
    if tipo == 'fer_01':
        cedolino.fer_01=value
    if tipo == 'fer_02':
        cedolino.fer_02=value
    if tipo == 'fer_03':
        cedolino.fer_03=value
    if tipo == 'fer_04':
        cedolino.fer_04=value
    if tipo == 'fer_05':
        cedolino.fer_05=value
    if tipo == 'fer_06':
        cedolino.fer_06=value
    if tipo == 'fer_07':
        cedolino.fer_07=value
    if tipo == 'fer_08':
        cedolino.fer_08=value
    if tipo == 'fer_09':
        cedolino.fer_09=value
    if tipo == 'fer_10':
        cedolino.fer_10=value
    if tipo == 'fer_11':
        cedolino.fer_11=value
    if tipo == 'fer_12':
        cedolino.fer_12=value
    if tipo == 'fer_13':
        cedolino.fer_13=value
    if tipo == 'fer_14':
        cedolino.fer_14=value
    if tipo == 'fer_15':
        cedolino.fer_15=value
    if tipo == 'fer_16':
        cedolino.fer_16=value
    if tipo == 'fer_17':
        cedolino.fer_17=value
    if tipo == 'fer_18':
        cedolino.fer_18=value
    if tipo == 'fer_19':
        cedolino.fer_19=value
    if tipo == 'fer_20':
        cedolino.fer_20=value
    if tipo == 'fer_21':
        cedolino.fer_21=value
    if tipo == 'fer_22':
        cedolino.fer_22=value
    if tipo == 'fer_23':
        cedolino.fer_23=value
    if tipo == 'fer_24':
        cedolino.fer_24=value
    if tipo == 'fer_25':
        cedolino.fer_25=value
    if tipo == 'fer_26':
        cedolino.fer_26=value
    if tipo == 'fer_27':
        cedolino.fer_27=value
    if tipo == 'fer_28':
        cedolino.fer_28=value
    if tipo == 'fer_29':
        cedolino.fer_29=value
    if tipo == 'fer_30':
        cedolino.fer_30=value
    if tipo == 'fer_31':
        cedolino.fer_31=value
    if tipo == 'mal_01':
        cedolino.mal_01=value
    if tipo == 'mal_02':
        cedolino.mal_02=value
    if tipo == 'mal_03':
        cedolino.mal_03=value
    if tipo == 'mal_04':
        cedolino.mal_04=value
    if tipo == 'mal_05':
        cedolino.mal_05=value
    if tipo == 'mal_06':
        cedolino.mal_06=value
    if tipo == 'mal_07':
        cedolino.mal_07=value
    if tipo == 'mal_08':
        cedolino.mal_08=value
    if tipo == 'mal_09':
        cedolino.mal_09=value
    if tipo == 'mal_10':
        cedolino.mal_10=value
    if tipo == 'mal_11':
        cedolino.mal_11=value
    if tipo == 'mal_12':
        cedolino.mal_12=value
    if tipo == 'mal_13':
        cedolino.mal_13=value
    if tipo == 'mal_14':
        cedolino.mal_14=value
    if tipo == 'mal_15':
        cedolino.mal_15=value
    if tipo == 'mal_16':
        cedolino.mal_16=value
    if tipo == 'mal_17':
        cedolino.mal_17=value
    if tipo == 'mal_18':
        cedolino.mal_18=value
    if tipo == 'mal_19':
        cedolino.mal_19=value
    if tipo == 'mal_20':
        cedolino.mal_20=value
    if tipo == 'mal_21':
        cedolino.mal_21=value
    if tipo == 'mal_22':
        cedolino.mal_22=value
    if tipo == 'mal_23':
        cedolino.mal_23=value
    if tipo == 'mal_24':
        cedolino.mal_24=value
    if tipo == 'mal_25':
        cedolino.mal_25=value
    if tipo == 'mal_26':
        cedolino.mal_26=value
    if tipo == 'mal_27':
        cedolino.mal_27=value
    if tipo == 'mal_28':
        cedolino.mal_28=value
    if tipo == 'mal_29':
        cedolino.mal_29=value
    if tipo == 'mal_30':
        cedolino.mal_30=value
    if tipo == 'mal_31':
        cedolino.mal_31=value
    if tipo == 'perm_01':
        cedolino.perm_01=value
    if tipo == 'perm_02':
        cedolino.perm_02=value
    if tipo == 'perm_03':
        cedolino.perm_03=value
    if tipo == 'perm_04':
        cedolino.perm_04=value
    if tipo == 'perm_05':
        cedolino.perm_05=value
    if tipo == 'perm_06':
        cedolino.perm_06=value
    if tipo == 'perm_07':
        cedolino.perm_07=value
    if tipo == 'perm_08':
        cedolino.perm_08=value
    if tipo == 'perm_09':
        cedolino.perm_09=value
    if tipo == 'perm_10':
        cedolino.perm_10=value
    if tipo == 'perm_11':
        cedolino.perm_11=value
    if tipo == 'perm_12':
        cedolino.perm_12=value
    if tipo == 'perm_13':
        cedolino.perm_13=value
    if tipo == 'perm_14':
        cedolino.perm_14=value
    if tipo == 'perm_15':
        cedolino.perm_15=value
    if tipo == 'perm_16':
        cedolino.perm_16=value
    if tipo == 'perm_17':
        cedolino.perm_17=value
    if tipo == 'perm_18':
        cedolino.perm_18=value
    if tipo == 'perm_19':
        cedolino.perm_19=value
    if tipo == 'perm_20':
        cedolino.perm_20=value
    if tipo == 'perm_21':
        cedolino.perm_21=value
    if tipo == 'perm_22':
        cedolino.perm_22=value
    if tipo == 'perm_23':
        cedolino.perm_23=value
    if tipo == 'perm_24':
        cedolino.perm_24=value
    if tipo == 'perm_25':
        cedolino.perm_25=value
    if tipo == 'perm_26':
        cedolino.perm_26=value
    if tipo == 'perm_27':
        cedolino.perm_27=value
    if tipo == 'perm_28':
        cedolino.perm_28=value
    if tipo == 'perm_29':
        cedolino.perm_29=value
    if tipo == 'perm_30':
        cedolino.perm_30=value
    if tipo == 'perm_31':
        cedolino.perm_31=value
    if tipo == 'stra_01':
        cedolino.stra_01=value
    if tipo == 'stra_02':
        cedolino.stra_02=value
    if tipo == 'stra_03':
        cedolino.stra_03=value
    if tipo == 'stra_04':
        cedolino.stra_04=value
    if tipo == 'stra_05':
        cedolino.stra_05=value
    if tipo == 'stra_06':
        cedolino.stra_06=value
    if tipo == 'stra_07':
        cedolino.stra_07=value
    if tipo == 'stra_08':
        cedolino.stra_08=value
    if tipo == 'stra_09':
        cedolino.stra_09=value
    if tipo == 'stra_10':
        cedolino.stra_10=value
    if tipo == 'stra_11':
        cedolino.stra_11=value
    if tipo == 'stra_12':
        cedolino.stra_12=value
    if tipo == 'stra_13':
        cedolino.stra_13=value
    if tipo == 'stra_14':
        cedolino.stra_14=value
    if tipo == 'stra_15':
        cedolino.stra_15=value
    if tipo == 'stra_16':
        cedolino.stra_16=value
    if tipo == 'stra_17':
        cedolino.stra_17=value
    if tipo == 'stra_18':
        cedolino.stra_18=value
    if tipo == 'stra_19':
        cedolino.stra_19=value
    if tipo == 'stra_20':
        cedolino.stra_20=value
    if tipo == 'stra_21':
        cedolino.stra_21=value
    if tipo == 'stra_22':
        cedolino.stra_22=value
    if tipo == 'stra_23':
        cedolino.stra_23=value
    if tipo == 'stra_24':
        cedolino.stra_24=value
    if tipo == 'stra_25':
        cedolino.stra_25=value
    if tipo == 'stra_26':
        cedolino.stra_26=value
    if tipo == 'stra_27':
        cedolino.stra_27=value
    if tipo == 'stra_28':
        cedolino.stra_28=value
    if tipo == 'stra_29':
        cedolino.stra_29=value
    if tipo == 'stra_30':
        cedolino.stra_30=value
    if tipo == 'stra_31':
        cedolino.stra_31=value
    if tipo == 'strafes_01':
        cedolino.strafes_01=value
    if tipo == 'strafes_02':
        cedolino.strafes_02=value
    if tipo == 'strafes_03':
        cedolino.strafes_03=value
    if tipo == 'strafes_04':
        cedolino.strafes_04=value
    if tipo == 'strafes_05':
        cedolino.strafes_05=value
    if tipo == 'strafes_06':
        cedolino.strafes_06=value
    if tipo == 'strafes_07':
        cedolino.strafes_07=value
    if tipo == 'strafes_08':
        cedolino.strafes_08=value
    if tipo == 'strafes_09':
        cedolino.strafes_09=value
    if tipo == 'strafes_10':
        cedolino.strafes_10=value
    if tipo == 'strafes_11':
        cedolino.strafes_11=value
    if tipo == 'strafes_12':
        cedolino.strafes_12=value
    if tipo == 'strafes_13':
        cedolino.strafes_13=value
    if tipo == 'strafes_14':
        cedolino.strafes_14=value
    if tipo == 'strafes_15':
        cedolino.strafes_15=value
    if tipo == 'strafes_16':
        cedolino.strafes_16=value
    if tipo == 'strafes_17':
        cedolino.strafes_17=value
    if tipo == 'strafes_18':
        cedolino.strafes_18=value
    if tipo == 'strafes_19':
        cedolino.strafes_19=value
    if tipo == 'strafes_20':
        cedolino.strafes_20=value
    if tipo == 'strafes_21':
        cedolino.strafes_21=value
    if tipo == 'strafes_22':
        cedolino.strafes_22=value
    if tipo == 'strafes_23':
        cedolino.strafes_23=value
    if tipo == 'strafes_24':
        cedolino.strafes_24=value
    if tipo == 'strafes_25':
        cedolino.strafes_25=value
    if tipo == 'strafes_26':
        cedolino.strafes_26=value
    if tipo == 'strafes_27':
        cedolino.strafes_27=value
    if tipo == 'strafes_28':
        cedolino.strafes_28=value
    if tipo == 'strafes_29':
        cedolino.strafes_29=value
    if tipo == 'strafes_30':
        cedolino.strafes_30=value
    if tipo == 'strafes_31':
        cedolino.strafes_31=value
    
    cedolino.save()
    
    return JsonResponse({"success":"Aggiornato"})