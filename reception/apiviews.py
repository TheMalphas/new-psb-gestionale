from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from .serializers import IngressidipSerializer
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from . import models
from django.utils import timezone
from datetime import datetime,date
import calendar


class IngressidipListAPIView(generics.ListCreateAPIView):
    today= datetime.now().date()
    queryset = models.Ingressidip.objects.filter(giorno = today).order_by('id_ingresso')
    serializer_class = IngressidipSerializer

def ingressi_json(request):
    today = datetime.now().date()
    ingressi = IngressidipSerializer(models.Ingressidip.objects.filter(giorno=today), many=True).data
    return JsonResponse(ingressi, safe=False)

def ingressi_json_mese(request):
    anno = datetime.now().date().year
    mese = datetime.now().date().month
    calendario = calendar.monthrange(anno, mese)
    start_date = timezone.datetime(anno,mese,calendario[0])
    end_date = timezone.datetime(anno,mese,calendario[1])
    ingressi = IngressidipSerializer(models.Ingressidip.objects.filter(giorno__range=[start_date,end_date]), many=True).data
    return JsonResponse(ingressi, safe=False)