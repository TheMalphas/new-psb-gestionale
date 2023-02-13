from rest_framework import serializers
from .models import Ingressidip
from datetime import datetime, date
from django.http import HttpResponse, JsonResponse
# Create a model serializer

class IngressidipSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Ingressidip
        fields = ["nominativo","giorno","in_permState","entrata","uscita","seconda_entrata","seconda_uscita","anticipo","ritardo","straordinario","ingressoArea","ingressoSede","ingressoSocieta"]
        ordering = ["nominativo","giorno"]