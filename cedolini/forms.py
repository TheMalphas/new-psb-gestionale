from django import forms
from .models import AnaDipendenti, CapoArea, Richieste, Ingressidip, Area, Istruzione, Societa, Sede, TipoContratto, Cedolini as ced
from . models import AddIncForf, AddRimborsi, AddTrasferte
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory


def has_numbers(input):
    return any(char.isalpha() for char in input)

def has_numbers_plus(input):
    for char in input:
        if char.isalpha() or char == "+" or char == " ":
            return True

def has_alphas(input):
    return any(char.isdigit() for char in input)

def is_iban(input):
    for char in input:
        if char.isalpha() or char.isdigit():
            pass
        else:
            return True



class AddInc_ForfForm(forms.ModelForm):
    class Meta:
        model= AddTrasferte
        fields= "__all__"
        exclude=["id_trasferte","id_ced","timestamp_creazione"]
        
        labels={
            "inc_forf":_('Valore')
        }
        
        widgets={
            "inc_forf":forms.TextInput(attrs={"class":"form-control","name":"valore","id":"valore"})
        }
        

class AddTrasferteForm(forms.ModelForm):
    class Meta:
        model= AddTrasferte
        fields= "__all__"
        exclude=["id_trasferte","id_ced","timestamp_creazione"]
        
        DAYS = (
        (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
        (11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),
        (21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30),(31,31)
        )
        
        labels={
            "rel_giorno":_('Giorno'),
            "ore":_('Ore')
        }
        
        widgets={
            "rel_giorno":forms.Select(choices=DAYS,attrs={"class":"form-select","name":"add","id":"add"}),
            "ore":forms.TextInput(attrs={"class":"form-control","name":"ore","id":"ore"})
        }
        
        def clean(self, *args, **kwargs):
            cleaned_data= super().clean()
            giorno = cleaned_data.get("rel_giorno")
            ore = cleaned_data.get("ore")
            
            lista_mesi_non31 = ["2", "4", "6", "9", "11"]
            
            if type(giorno) != int or giorno > 31:
                msg = "I giorni possono essere solo numerici e non più grandi di 31."
                self.add_error("giorno",msg)
            
            return cleaned_data

########### FORMS PER CEDOLINI

class CreaCedoliniForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dipendente'].queryset= AnaDipendenti.objects.filter(stato="Attivo")
        self.fields['dipendente'].required=True
        self.fields['mese'].required=True
        
    class Meta:
        model= ced
        fields =["dipendente","mese"]
        exclude = ['ret','anno','add_ced','bonuses','documenti','id_ultima_modifica','id_creazione','timestamp_creazione','notes']
        
        CHOICES = (
            (1,'Gennaio'),
            (2,'Febbraio'),
            (3,'Marzo'),
            (4,'Aprile'),
            (5,'Maggio'),
            (6,'Giugno'),
            (7,'Luglio'),
            (8,'Agosto'),
            (9,'Settembre'),
            (10,'Ottobre'),
            (11,'Novembre'),
            (12,'Dicembre')
            )
        
        labels = {
            'dipendente':_('Dipendente'),
            'mese':_('Mese di'),
        }
        
        widgets= {
            'dipendente':forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}),
            'mese':forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"mese","name":"mese"}),
        }
