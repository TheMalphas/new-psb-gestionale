from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView
from .serializers import IngressidipSerializer
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from . import models
from django.utils import timezone
from datetime import datetime,date


class IngressidipListAPIView(generics.ListCreateAPIView):
    today= datetime.now().date()
    queryset = models.Ingressidip.objects.all().order_by('id_ingresso')
    serializer_class = IngressidipSerializer

def ingressi_json(request):
    today = datetime.now().date()
    start_date = timezone.datetime(2022,1,1)
    ingressi = IngressidipSerializer(models.Ingressidip.objects.filter(giorno__range=(start_date,today)), many=True).data
    return JsonResponse(ingressi, safe=False)