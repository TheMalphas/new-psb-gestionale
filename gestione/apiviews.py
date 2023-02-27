from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from . import serializers
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from . import models
from django.utils import timezone
from datetime import datetime,date
import calendar
from datetime import datetime, time, timedelta

def contratti_json(request):
    today = datetime.now().date()
    contratti = serializers.ContrattiSerializer(models.Contratti.objects.all(), many=True).data
    return JsonResponse(contratti, safe=False)


def dipendenti_json(request):
    dipendenti = serializers.DipendentiSerializer(models.AnaDipendenti.objects.filter(stato='Attivo'), many=True).data
    return JsonResponse(dipendenti, safe=False)


def dipendenti_misc_json(request):
    dipendenti = serializers.DipendentiMiscellaneousSerializer(models.AnaDipendenti.objects.filter(stato='Attivo'), many=True).data
    return JsonResponse(dipendenti, safe=False)

