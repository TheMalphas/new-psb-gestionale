from rest_framework import serializers
from .models import AnaDipendenti
from datetime import datetime, date
from django.http import HttpResponse, JsonResponse
# Create a model serializer

class DipendentiSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = AnaDipendenti
        fields = ['nominativo','getsocieta','getsede','getarea','capoareadi','getmansione','contratto','getinizio','getscadenza','getsesso','codice_fiscale','getcitta','getprovincia','iban','p_iva']
        ordering = ["nominativo"]

class FatDipendentiSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = AnaDipendenti
        fields = ['nominativo','contratto','getsocieta','getsede','getarea','capoareadi','data_inizio_rap','data_fine_rap','getsesso','codice_fiscale','citta_residenza','citta_domicilio','email_pers','iban','p_iva']
        ordering = ["nominativo"]