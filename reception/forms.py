from django import forms
from .models import AnaDipendenti, Richieste, Ingressidip
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta, date, time
from django.forms import ModelForm, Textarea
day = datetime.now()
today = datetime.now().date()

class CreaEntrata(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= ['nominativo','giorno','tipo_permesso','entrata','uscita','tipo']
        exclude = ['id_dip_ing','id_ingresso','id_permesso','in_permesso','registrato_da_user', 'seconda_entrata', 'seconda_uscita','checked_in','checked_out',]
        
        labels = {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'tip_permesso':_('Tipo Permesso'),
        'entrata':_('Ora di entrata'),
        'checked_in':_('Entrato/a?'),
        'uscita':_('Ora di uscita'),
        'checked_out':_('Uscito/a?'),
        'tipo':_('Segna Esterno/Assente')
    }
        CHOICES = ((0,'No'),(1,'Si'))
        TIPOLOGIA = ((None,'---'),('Assente','Assente'),('Ares','Ares'),('Ariano','Ariano'),('Medina','Medina'),('Esterno','Esterno'),('Ferie','Ferie'),('Smart','Smart'))
        PERMESSI = ((None,'---'),('1','ASSISTENZA FAMILIARI CON HANDICAP (Legge 104)'),('2','CONGEDO PER MATERNITÀ'),('3','CONGEDO PER MATRIMONIO'),('4','CONGEDO PER PATERNITÀ'),('5','CONVOCAZIONE TRIBUNALE'),('6','FERIE'),('7','FESTIVITÀ SOPPRESSE'),
                    ('8','PERMESSO NON RETRIBUITO'),('9','PERMESSO PER CONGEDO PARENTALE'),('10','PERMESSO PER RIDUZIONE ORARIO DI LAVORO (ROL)'),('11','PERMESSO RETRIBUITO - AGGIORNAMENTO PROFESSIONALE'),('12','PERMESSO RETRIBUITO - DONAZIONE DI MIDOLLO OSSEO'),
                    ('13','PERMESSO RETRIBUITO - LUTTO FAMILIARE O GRAVE INFERMITÀ'),('14','VISITA MEDICA SPECIALISTICA'),('16','PERMESSO PER MALATTIA'))
        
        widgets = {
        'nominativo': forms.TextInput(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}),
        'giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"giorno","name":"giorno"}),
        'tip_permesso': forms.Select(choices=PERMESSI,attrs={"class":"form-control","id":"tipo_permesso","name":"tipo_permesso"}),
        'entrata': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"entrata","name":"entrata"}),
        'checked_in': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"entrato","name":"entrato"}),
        'uscita': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"uscita","name":"uscita"}),
        'checked_out': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"uscita","name":"uscita"}),
        'tipo': forms.Select(choices=TIPOLOGIA,attrs={"class":"form-control","id":"tipo","name":"tipo"}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True
        if self.fields["entrata"] == "":
            self.fields["entrata"].disabled = True
            self.fields['entrata'].widget = forms.HiddenInput()
        if self.fields["uscita"] == "":
            self.fields["uscita"].disabled = True
            self.fields['uscita'].widget = forms.HiddenInput()


class CreaEntrataDoppia(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= ['nominativo','giorno','tipo_permesso','entrata','uscita','seconda_entrata', 'seconda_uscita','tipo']
        exclude = ['id_dip_ing','id_permesso','in_permesso','registrato_da_user','checked_in','checked_out',]
        
        labels = {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'tipo_permesso':_('Tipo Permesso'),
        'entrata':_('Ora di entrata'),
        'seconda_entrata':_('Seconda entrata'),
        'checked_in':_('Entrato/a?'),
        'uscita':_('Ora di uscita'),
        'seconda_uscita':_('Seconda uscita'),
        'checked_out':_('Uscito/a?'),
        'tipo':_('Segna Esterno/Assente')
    }
        CHOICES = ((0,'No'),(1,'Si'))
        TIPOLOGIA = ((None,'---'),('Assente','Assente'),('Ares','Ares'),('Ariano','Ariano'),('Medina','Medina'),('Esterno','Esterno'),('Ferie','Ferie'),('Smart','Smart'))
        PERMESSI = ((None,'---'),('1','ASSISTENZA FAMILIARI CON HANDICAP (Legge 104)'),('2','CONGEDO PER MATERNITÀ'),('3','CONGEDO PER MATRIMONIO'),('4','CONGEDO PER PATERNITÀ'),('5','CONVOCAZIONE TRIBUNALE'),('6','FERIE'),('7','FESTIVITÀ SOPPRESSE'),
                    ('8','PERMESSO NON RETRIBUITO'),('9','PERMESSO PER CONGEDO PARENTALE'),('10','PERMESSO PER RIDUZIONE ORARIO DI LAVORO (ROL)'),('11','PERMESSO RETRIBUITO - AGGIORNAMENTO PROFESSIONALE'),('12','PERMESSO RETRIBUITO - DONAZIONE DI MIDOLLO OSSEO'),
                    ('13','PERMESSO RETRIBUITO - LUTTO FAMILIARE O GRAVE INFERMITÀ'),('14','VISITA MEDICA SPECIALISTICA'),('16','PERMESSO PER MALATTIA'))
        
        widgets = {
        'nominativo': forms.TextInput(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}),
        'giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"giorno","name":"giorno"}),
        'tipo_permesso': forms.Select(choices=PERMESSI,attrs={"class":"form-control","id":"tipo_permesso","name":"tipo_permesso"}),
        'entrata': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"entrata","name":"entrata"}),
        'seconda_entrata': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"seconda_entrata","name":"seconda_entrata"}),
        'checked_in': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"entrato","name":"entrato"}),
        'uscita': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"uscita","name":"uscita"}),
        'seconda_uscita': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"seconda_uscita","name":"seconda_uscita"}),
        'checked_out': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"uscita","name":"uscita"}),
        'tipo': forms.Select(choices=TIPOLOGIA,attrs={"class":"form-control","id":"tipo","name":"tipo"}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True
        if self.fields["entrata"] == "":
            self.fields["entrata"].disabled = True
            self.fields['entrata'].widget = forms.HiddenInput()
        if self.fields["uscita"] == "":
            self.fields["uscita"].disabled = True
            self.fields['uscita'].widget = forms.HiddenInput()

class UpdateEntrata(ModelForm):
    class Meta:
        model= Ingressidip
        fields= "__all__"
        exclude = ['id_ingresso','id_dip_ing','in_permesso','registrato_da_user','seconda_entrata','seconda_uscita','checked_in','checked_out']
        
    labels= {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'tipo_permesso':_('Tipo Permesso'),
        'entrata':_('Ora di entrata'),
        'uscita':_('Ora di uscita'),
        'giorno':_('Giorno'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True
        self.fields["uscita"].disabled = True
        self.fields["uscita"].widget.attrs["readonly"] = True

    
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        checked_in = cleaned_data.get("checked_in")
        checked_out = cleaned_data.get("checked_out")

        if checked_in == "1":
            checked_in = 1
        elif checked_in == "0":
            checked_in = 0
        
        if checked_out == "1":
            checked_out = 1
        elif checked_out == "0":
            checked_out = 0

class UpdateUscita(ModelForm):
    class Meta:
        model= Ingressidip
        fields= "__all__"
        exclude = ['id_ingresso','id_dip_ing','id_permesso','in_permesso','registrato_da_user','seconda_entrata','seconda_uscita','checked_in',"checked_out"]
                
        labels = {
            'nominativo':_('Dipendente'), 
            'giorno' :_('Giorno'), 
            'tipo_permesso':_('Tipo Permesso'),
            'entrata':_('Ora di entrata'),  
            'uscita':_('Ora di uscita'),
            'giorno':_('Giorno'),
            'checked_out': _('Uscito?')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True
        self.fields["entrata"].disabled = True
        self.fields["entrata"].widget.attrs["readonly"] = True

    
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        checked_in = cleaned_data.get("checked_in")
        checked_out = cleaned_data.get("checked_out")

        if checked_in == "1":
            checked_in = 1
        elif checked_in == "0":
            checked_in = 0
        
        if checked_out == "1":
            checked_out = 1
        elif checked_out == "0":
            checked_out = 0
        

class UpdateDoppiaEntrata(ModelForm):
    class Meta:
        model= Ingressidip
        fields= "__all__"
        exclude = ['id_ingresso','id_dip_ing','id_permesso','in_permesso','registrato_da_user','checked_in','checked_out']
        
    labels= {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'tipo_permesso':_('Tipo Permesso'),
        'entrata':_('Prima entrata'),
        'uscita':_('Prima uscita'),
        'seconda_entrata':_('Seconda entrata'),
        'seconda_uscita':_('Seconda uscita'),
        'giorno':_('Giorno'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True


    
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        checked_in = cleaned_data.get("checked_in")
        checked_out = cleaned_data.get("checked_out")

        if checked_in == "1":
            checked_in = 1
        elif checked_in == "0":
            checked_in = 0
        
        if checked_out == "1":
            checked_out = 1
        elif checked_out == "0":
            checked_out = 0
            

class UpdateDoppiaUscita(ModelForm):
    class Meta:
        model= Ingressidip
        fields= "__all__"
        exclude = ['id_ingresso','id_dip_ing','id_permesso','in_permesso','registrato_da_user','checked_in','checked_out']
            
    labels= {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'tipo_permesso':_('Tipo Permesso'),
        'entrata':_('Prima entrata'),
        'uscita':_('Prima uscita'),
        'seconda_entrata':_('Seconda entrata'),
        'seconda_uscita':_('Seconda uscita'),
        'giorno':_('Giorno'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True

    
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        checked_in = cleaned_data.get("checked_in")
        checked_out = cleaned_data.get("checked_out")

        if checked_in == "1":
            checked_in = 1
        elif checked_in == "0":
            checked_in = 0
        
        if checked_out == "1":
            checked_out = 1
        elif checked_out == "0":
            checked_out = 0


# =============================================== FORM NON USATI ===============================================


class EntrateForm(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= ['nominativo','entrata','checked_in']
        exclude = ['id_ingresso','id_dip_ing','id_permesso','tipo_permesso','giorno','registrato_da_user','uscita','checked_out']
        
        labels = {
        'nominativo,':_('Dipendente'),
        'entrata':_('Ora di entrata'),
        'checked_in':_('Entrato?'),
    }
        widgets = {
        'giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"giorno","name":"giorno"}),
        'entrata': forms.TextInput(),
        'checked_in' : forms.CheckboxInput(attrs={'id':'checked_in','name':'checked_in'}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True



class UsciteForm(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= ['nominativo','uscita','checked_out']
        exclude = ['id_ingresso','id_dip_ing','id_permesso','tipo_permesso','registrato_da_user','entrata','checked_in']
        
        labels = {
        'nominativo,':_('Dipendente'),
        'uscita':_('Ora di uscita'),
        'checked_out':_('Uscito?'),
    }
        widgets = {
        'giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"giorno","name":"giorno"}),
        'uscita': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"entrata","name":"entrata"}),
        'checked_out' : forms.CheckboxInput(attrs={'id':'checked_out','name':'checked_out'}),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nominativo"].disabled = True
        self.fields["nominativo"].widget.attrs["readonly"] = True
        self.fields["giorno"].disabled = True
        self.fields["giorno"].widget.attrs["readonly"] = True

# =============================================== FINE NON USATI ===============================================
