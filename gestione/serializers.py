from rest_framework import serializers
from .models import AnaDipendenti, Contratti
from datetime import datetime, date
from django.http import HttpResponse, JsonResponse
# Create a model serializer

class ContrattiSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Contratti
        fields = ['getdipendente','getsocieta','gettipologia','getccnl','getpercentuale','datainizio','datafine']
        
class DipendentiSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = AnaDipendenti
        fields = ['nominativo','getsocieta','getsede','getarea','getmansione','contratto','codice_fiscale','getcitta','getprovincia']
        ordering = ["nominativo"]

class DipendentiMiscellaneousSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = AnaDipendenti
        fields = ['nominativo','getsocieta','getsede','getarea','getmansione','getsesso']
        ordering = ["nominativo"]

class FatDipendentiSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = AnaDipendenti
        fields = ['nominativo','contratto','getsocieta','getsede','getarea','data_inizio_rap','data_fine_rap','getsesso','codice_fiscale','citta_residenza','citta_domicilio','email_pers','iban','p_iva']
        ordering = ["nominativo"]