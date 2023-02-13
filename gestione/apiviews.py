from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from .serializers import DipendentiSerializer
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from . import models
from django.utils import timezone
from datetime import datetime,date
import calendar

def dipendenti_json(request):
    dipendenti = DipendentiSerializer(models.AnaDipendenti.objects.filter(stato='Attivo'), many=True).data
    return JsonResponse(dipendenti, safe=False)
