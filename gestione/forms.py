from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.core.validators import RegexValidator
import traceback
import re



class AddTrasferteFormGestione(forms.ModelForm):
    class Meta:
        model = AddTrasferte
        exclude = ["id_trasferte","id_dip","id_ced","ore","timestamp"]
        localized_field = ('rel_giorno')
        labels = {
            'rel_giorno':_("Giornata"),
            'valore':_("Tipo Trasferta"),
            'note':_('Motivazione')
        }
        
        CHOICES = (
            (30,30),(46,46)
        )
        
        widgets= {
            'rel_giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"rel_giorno","name":"rel_giorno"}),
            'valore': forms.Select(choices=CHOICES,attrs={"type":"date","class":"form-control","id":"rel_giorno","name":"rel_giorno"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }


class PhoneForm(forms.Form):
    phone_regex = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    phone_number = forms.CharField(validators=[RegexValidator(phone_regex, "Phone number must be in the format: 'xxx-xxx-xxxx'")])

# #Tutte le lettere minuscole 
class Lettereminuscole(forms.CharField):
    def to_python(self, value):
        return value.lower()

# #Tutte le lettere maiuscole 

class Letteremaiuscole(forms.CharField):
    def to_python(self, value):
        return value.upper()

def has_numbers(input):
    return any(char.isalpha() for char in input)

def has_numbers_plus(input):
    for char in input:
        if char.isalpha(): #or char == "+" or char == " ":
            return True

def clean_data(string: str) -> str:
    result = ''
    for char in string:
        if char in '1234567890':
            result += char
    return result

def has_alphas(input):
    return any(char.isdigit() for char in input)

def is_iban(input):
    for char in input:
        if char.isalpha() or char.isdigit():
            pass
        else:
            return True


########### FORMS PER CAPO AREA

class CapoAreaForm(forms.ModelForm):
    dipendenti = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))
    
    class Meta:
        model = CapoArea
        fields = ["sede","area","dipendenti"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
            'dipendenti':_('Dipendenti')
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

class CapoAreaUpdateForm(forms.ModelForm):    
    class Meta:
        model = CapoArea
        fields = ["sede","area"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

########### FORMS PER DIRIGENTI

class DirigentiForm(forms.ModelForm):
    dipendenti = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))
    
    class Meta:
        model = Dirigenti
        fields = ["sede","area","dipendenti"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
            'dipendenti':_('Dipendenti')
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

class DirigentiUpdateForm(forms.ModelForm):    
    class Meta:
        model = Dirigenti
        fields = ["sede","area"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

########### FORMS PER RESPONSABILI

class ResponsabiliForm(forms.ModelForm):
    dipendenti = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))
    
    class Meta:
        model = Responsabili
        fields = ["sede","area","dipendenti"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
            'dipendenti':_('Dipendenti')
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

class ResponsabiliUpdateForm(forms.ModelForm):    
    class Meta:
        model = Responsabili
        fields = ["sede","area"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

########### FORMS PER RESPONSABILISEDE

class ResponsabiliSedeForm(forms.ModelForm):
    dipendenti = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))
    class Meta:
        model = ResponsabiliSede
        fields = ["sede","area","dipendenti"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
            'dipendenti':_('Dipendenti')
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }

class ResponsabiliSedeUpdateForm(forms.ModelForm):    
    class Meta:
        model = ResponsabiliSede
        fields = ["sede","area"]
        exclude = ["id_capo","nomecompleto","id_dipendente"]
        
        labels = {
            'area':_('Area'),
            'sede':_('Sede'),
        }
        
        widgets= {
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
        }


########### FORMS PER MODIFICARE ENTRATA


class CreaEntrata(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= ['nominativo','giorno','entrata','uscita','tipo']
        exclude = ['id_dip_ing','id_ingresso','id_permesso','in_permesso','registrato_da_user', 'seconda_entrata', 'seconda_uscita','checked_in','checked_out',]
        
        labels = {
        'nominativo':_('Dipendente'),
        'giorno' :_('Giorno'), 
        'entrata':_('Ora di entrata'),
        'checked_in':_('Entrato/a?'),
        'uscita':_('Ora di uscita'),
        'checked_out':_('Uscito/a?'),
        'tipo':_('Segna Esterno/Assente')
    }
        CHOICES = ((0,'No'),(1,'Si'))
        TIPOLOGIA = ((None,'---'),('Assente','Assente'),('Esterno','Esterno'))
        
        widgets = {
        'nominativo': forms.TextInput(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}),
        'giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"giorno","name":"giorno"}),
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
        

########### FORMS PER ANAGRAFICA DIPENDENTI


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["nome_area","note"]
        exclude = ["data_creazione","data_modifica ","id_area"]
        labels = {
            'nome_area':_("Nome Area"),
            'note':_('Note'),
            }
        widgets= {
            'nome_area' : forms.TextInput(attrs={"class":"form-control","id":"nome_area","name":"nome_area"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }


class IstruzioneForm(forms.ModelForm):
    class Meta:
        model = Istruzione
        fields = ["tipo_istruzione","note"]
        exclude = ["data_creazione","data_modifica ","id_istruzione"]
        
        labels = {
            'tipo_istruzione':_("Tipo di Istruzione"),
            'note':_('Note'),
            }
        
        widgets= {
            'tipo_istruzione' : forms.TextInput(attrs={"class":"form-control","id":"tipo_istruzione","name":"tipo_istruzione"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }

class MansioneForm(forms.ModelForm):
    class Meta:
        model = Mansione
        fields = ["tipo_mansione","note"]
        exclude = ["data_creazione","data_modifica ","id_area"]
        labels = {
            'tipo_mansione':_("Tipo Mansione"),
            'note':_('Note'),
            }
        widgets= {
            'tipo_mansione' : forms.TextInput(attrs={"class":"form-control","id":"tipo_mansione","name":"tipo_mansione"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ["nome_sede","note"]
        exclude = ["data_creazione","data_modifica ","id_sede"]
        labels = {
            'nome_sede':_("Nome Sede"),
            'note':_('Note'),
            }
        widgets= {
            'nome_sede' : forms.TextInput(attrs={"class":"form-control","id":"nome_sede","name":"nome_sede"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }
        
class SocietaForm(forms.ModelForm):
    class Meta:
        model = Societa
        fields = ["nome_societa","note"]
        exclude = ["data_creazione","data_modifica ","id_societa"]
        labels = {
            'nome_societa':_("Nome Società"),
            'note':_('Note'),
            }
        widgets= {
            'nome_societa' : forms.TextInput(attrs={"class":"form-control","id":"nome_societa","name":"nome_societa"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }

class TipoContrattoForm(forms.ModelForm):
    class Meta:
        model = TipoContratto   
        fields = ["nome_contratto","note"]
        exclude = ["data_creazione","data_modifica ","id_contratto"]
        labels = {
            'nome_contratto':_("Tipo di Contratto"),
            'note':_('Note'),
            }
        widgets= {
            'nome_contratto' : forms.TextInput(attrs={"class":"form-control","id":"nome_contratto","name":"nome_contratto"}),            
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }


# CONFIRM RICHIESTE FORM

class RichiesteAccettateForm(forms.ModelForm):
    class Meta:
        model = RichiesteAccettate   
        fields = ["data_inizio_permesso","data_fine_permesso","ora_inizio_permesso","ora_fine_permesso","in_corso","note"]
        localized_fields = ('data_inizio_permesso','data_fine_permesso','ora_inizio_permesso', 'ora_fine_permesso')
        labels = {
            'data_inizio_permesso':_("Data di inizio"),
            'data_fine_permesso':_("Data di fine"),
            'ora_inizio_permesso':_("Ora di inizio"),
            'data_inizio_permesso':_("Ora di fine"),
            'in_corso':_("Segna fine permesso"),
            'note':_('Note'),
            }
        widgets= {
            'data_inizio_permesso': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_inizio_permesso","name":"data_inizio_permesso"}),
            'data_fine_permesso': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_fine_permesso","name":"data_fine_permesso"}),
            'ora_inizio_permesso': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"ora_inizio_permesso","name":"ora_inizio_permesso"}),
            'ora_fine_permesso': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"ora_fine_permesso","name":"ora_fine_permesso"}),
            'in_corso': forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-check-input","id":"in_corso","name":"in_corso"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":6,"id":"note","name":"note"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data_inizio_permesso"].disabled = True
        self.fields["data_inizio_permesso"].widget.attrs["readonly"] = True
        self.fields["data_fine_permesso"].disabled = True
        self.fields["data_fine_permesso"].widget.attrs["readonly"] = True
        self.fields["ora_inizio_permesso"].disabled = True
        self.fields['ora_inizio_permesso'].widget.attrs["readonly"] = True
        self.fields["ora_fine_permesso"].disabled = True
        self.fields['ora_fine_permesso'].widget.attrs["readonly"] = True


# CONFIRM RICHIESTE FORM

class ModificaRichiesteAccettateForm(forms.ModelForm):
    class Meta:
        model = RichiesteAccettate   
        fields = ["data_inizio_permesso","data_fine_permesso","ora_inizio_permesso","ora_fine_permesso"]
        localized_fields = ('data_inizio_permesso','data_fine_permesso','ora_inizio_permesso', 'ora_fine_permesso','in_corso','note')
        labels = {
            'data_inizio_permesso':_("Data di inizio"),
            'data_fine_permesso':_("Data di fine"),
            'ora_inizio_permesso':_("Ora di inizio"),
            'data_inizio_permesso':_("Ora di fine"),
            }
        widgets= {
            'data_inizio_permesso': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_inizio_permesso","name":"data_inizio_permesso"}),
            'data_fine_permesso': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_fine_permesso","name":"data_fine_permesso"}),
            'ora_inizio_permesso': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"ora_inizio_permesso","name":"ora_inizio_permesso"}),
            'ora_fine_permesso': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"ora_fine_permesso","name":"ora_fine_permesso"}),
        }


class OreContrattiForm(forms.ModelForm):
    class Meta:
        model = PercentualiContratto
        fields = ["dicitura_percentuale","perc_contratto","note"]
        exclude = ["id_ore_contratto","ore_contratto"]
        
        labels = {
            'dicitura_percentuale':_('Dicitura Contratto'),
            'perc_contratto':_("Percentuale Contratto"),
            'note':_('Note'),
            }
        
        widgets= {
            'dicitura_percentuale' : forms.TextInput(attrs={"class":"form-control","id":"dicitura_percentuale","name":"dicitura_percentuale"}),
            'perc_contratto' : forms.TextInput(attrs={"class":"form-control","id":"perc_contratto","name":"perc_contratto"}),
            'note' : forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"})
        }


class ContrattiFormInsert(forms.ModelForm):
    dipendente = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))

    class Meta:
        model = Contratti
        fields = ["dipendente","id_societa","ccnl","tipologia","percentuale",'datainizio','datafine','trasferte_fisse','trasferte_fisse_tipo','note']
        exclude = ["id_contratto","id_dip",'codicecontratto']

        CHOICES = (
            ('30','30'),
            ('46','46')
        )

        labels = {
            'dipendente':_('Dipendente'),
            'id_societa':_('Società'),
            'tipologia':_('Tipologia'),
            'ccnl':_('CCNL'),
            'percentuale':_('Percentuale'),
            'datainizio':_('Data Inizio'),
            'datafine':_('Data Fine'),
            'trasferte_fisse':_('Trasferte Fisse'),
            'trasferte_fisse_tipo':_('Tipo Trasferta'),
            'datafine':_('Data Fine'),
            'note':_('Note'),
            }
        
        widgets= {
            'id_societa' : forms.Select(attrs={"class":"form-control","id":"id_societa","name":"id_societa"}),
            'tipologia' : forms.Select(attrs={"class":"form-control","id":"tipologia","name":"tipologia"}),
            'ccnl' : forms.Select(attrs={"class":"form-control","id":"ccnl","name":"ccnl"}),
            'percentuale' : forms.Select(attrs={"class":"form-control","id":"percentuale","name":"percentuale"}),
            'datainizio': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datainizio","name":"datainizio"}),
            'datafine': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datafine","name":"datafine"}),
            'trasferte_fisse' : forms.TextInput(attrs={"class":"form-control","type":"number","id":"trasferte_fisse","name":"trasferte_fisse"}),
            'trasferte_fisse_tipo' : forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"trasferte_fisse_tipo","name":"trasferte_fisse_tipo"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
            }
        
        def __init__(self, *args, **kwargs):
            super(ContrattiFormInsert, self).__init__(*args, **kwargs)
            self.fields['trasferte_fisse'].widget.attrs.update({'pattern':'[0-9]+'})

class ContrattiFormUpdate(forms.ModelForm):
    class Meta:
        model = Contratti
        fields = ["id_societa","tipologia","ccnl","percentuale",'datainizio','datafine','trasferte_fisse','trasferte_fisse_tipo','note']
        exclude = ["id_contratto","id_dip",'codicecontratto']
        
        CHOICES = (
            ('30','30'),
            ('46','46')
            
        )
        
        labels = {
            'id_societa':_('Società'),
            'tipologia':_('Tipologia'),
            'ccnl':_('CCNL'),
            'percentuale':_('Percentuale'),
            'datainizio':_('Data Inizio'),
            'datafine':_('Data Fine'),
            'trasferte_fisse':_('Trasferte Fisse'),
            'trasferte_fisse_tipo':_('Tipo Trasferta'),
            'note':_('Note'),
            }
        
        widgets= {
            'id_societa' : forms.Select(attrs={"class":"form-control","id":"id_societa","name":"id_societa"}),
            'tipologia' : forms.Select(attrs={"class":"form-control","id":"tipologia","name":"tipologia"}),
            'ccnl' : forms.Select(attrs={"class":"form-control","id":"ccnl","name":"ccnl"}),
            'percentuale' : forms.Select(attrs={"class":"form-control","id":"percentuale","name":"percentuale"}),
            'datainizio': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datainizio","name":"datainizio"}),
            'datafine': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datafine","name":"datafine"}),
            'trasferte_fisse' : forms.TextInput(attrs={"class":"form-control","id":"trasferte_fisse","name":"trasferte_fisse"}),
            'trasferte_fisse_tipo' : forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"trasferte_fisse_tipo","name":"trasferte_fisse_tipo"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
            }
        
        def __init__(self, *args, **kwargs):
            super(ContrattiFormUpdate, self).__init__(*args, **kwargs)
            self.fields['trasferte_fisse'].widget.attrs.update({'pattern':'[0-9]+'})


class StatoDipendenteForm(forms.ModelForm):
    
    class Meta:
        model = AnaDipendenti
        fields = ["stato"]

        CHOICES = (
            ('Attivo','Attivo'),('Cessato','Cessato'),('Sospeso','Sospeso')
        )

        labels = {
            'stato':_("Stato")
        }
        widgets = { 
            'stato' : forms.Select(choices=CHOICES,attrs={"class":"form-select","id":"stato","name":"stato"})
        }

        
def format_phone_number(value):
    return '(+39) {}-{}-{}'.format(value[:3], value[3:6], value[6:])

class AnaDipendentiCarloForm(forms.ModelForm):
    class Meta:
        model= AnaDipendenti
        exclude = ['id_dip','user','id_stipendio','id_societa','data_creazione','created_at']
        
        CHOICES = (
            ('Attivo','Attivo'),('Cessato','Cessato'),('Sospeso','Sospeso')
        )
        
        labels = {
            'cognome':_("Cognome"),
            'nome':_('Nome'),
            'codice_fiscale':_("Codice Fiscale"),
            'stato':_("Stato"),
            'sesso':_("Sesso"),
            'luogo_nascita':_('Luogo di Nascita'),
            'provincia_nascita':_('Provincia di Nascita'),
            'data_nascita':_('Data di Nascita'),
            'citta_domicilio':_('Città di Domicilio'),
            'indirizzo_domicilio':_('Indirizzo di Domiclio'),
            'provincia_domicilio':_('Provincia di Domiclio'),
            'cap_domicilio':_('Cap Domicilio'),
            'citta_residenza':_('Città di Residenza'),
            'indirizzo_residenza':_('Indirizzo di Residenza'),
            'provincia_residenza':_('Provincia di Residenza'),
            'cap_residenza':_('Cap Residenza'),
            'asl':_('ASL'),
            'email_pers':_('Email Personale'),
            'email_lav':_('Email Lavorativa'),
            'cellulare':_('Cellulare'),
            'cell_alternativo':_('Cell. Alternativo'),
            'iban':_('IBAN'),
            'p_iva':_('Partita IVA'),
            'societa':_('Società'),
            'area':_('Area'),
            'sede':_('Sede'),
            'tipo_contratto':_('Tipologia di contratto'),
            'istruzione':_('Tipo di istruzione'),
            'mansione':_('Mansione'),
            'data_inizio_rap':_('Data Inizio Rapporto'),
            'data_fine_rap':_('Data Fine Rapporto'),
            'note':_('Note')
            }

        widgets= {
            'nome': forms.TextInput(attrs={'placeholder': 'Immetti Nome','style':'font-sitze: 13px; text-transform: capitalize'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Immetti Cognome','style':'font-sitze: 13px; text-transform: capitalize' }),
            'codice_fiscale': forms.TextInput(attrs={'style':'font-sitze: 13px; text-transform: uppercase' }),
            'stato': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"stato","name":"stato"}),
            'sesso':forms.Select(attrs={"class":"form-control",'placeholder': 'Sesso',"id":"sesso","name":"sesso"}),
            'data_nascita': forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px',"id":"data_nascita","name":"data_nascita", 'placeholder':'' }),
            'luogo_nascita': forms.TextInput(attrs={"class":"form-control","id":"luogo_nascita","name":"luogo_nascita",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'provincia_nascita': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_nascita","name":"provincia_nascita",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'citta_domicilio': forms.TextInput(attrs={"class":"form-control","id":"citta_domicilio","name":"citta_domicilio",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'indirizzo_domicilio': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_domicilio","name":"indirizzo_domicilio",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'provincia_domicilio': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_domicilio","name":"provincia_domicilio",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'cap_domicilio': forms.TextInput(attrs={"class":"form-control",'placeholder': '12345',"id":"cap_domicilio","name":"cap_domicilio"}),
            'citta_residenza': forms.TextInput(attrs={"class":"form-control","id":"citta_residenza","name":"citta_residenza",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'indirizzo_residenza': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_residenza","name":"indirizzo_residenza",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'provincia_residenza': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_residenza","name":"provincia_residenza",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'cap_residenza': forms.TextInput(attrs={"class":"form-control",'placeholder': '12345',"id":"cap_residenza","name":"cap_residenza"}),
            'asl': forms.TextInput(attrs={"class":"form-control","id":"asl","name":"asl",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'email_lav':forms.TextInput(attrs={"class":"form-control",'placeholder': "Immetti Un' email valida",'style':'font-sitze: 13px; text-transform: lowercase'}),
            'email_pers':forms.TextInput(attrs={"class":"form-control",'placeholder': "Immetti Un' email valida",'style':'font-sitze: 13px; text-transform: lowercase'}),
            'cellulare':forms.TextInput( attrs={"class":"form-control",'style': 'font-sitze: 13px',"id":"cellulare","name":"cellulare", 'placeholder':'Cellulare'}),
            'cell_alternativo':forms.TextInput( attrs={"class":"form-control",'data-mask':'000-0000000' ,'style': 'font-sitze: 13px',"id":"cell_alternativo","name":"cell_alternativo", 'placeholder':'Cellulare', }),
            'iban':forms.TextInput(attrs={"class":"form-control",'placeholder': 'Immetti Un Iban Valido','style':'font-sitze: 13px; text-transform: capitalize'}),
            'p_iva':forms.TextInput(attrs={'placeholder': 'Immetti Una Partita Iva Valida','style':'font-sitze: 13px; text-transform: capitalize'}),
            'societa':forms.Select(attrs={"class":"form-control","id":"societa","name":"societa",'rows': 2, 'cols': 20}),
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
            'istruzione':forms.Select(attrs={"class":"form-control","id":"istruzione","name":"istruzione"}),
            'tipo_contratto':forms.Select(attrs={"class":"form-control","id":"tipocontratto","name":"tipocontratto"}),
            'mansione':forms.Select(attrs={"class":"form-control","id":"mansione","name":"mansione"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"}),
            'data_fine_rap' : forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px',"id":"data_inizio_rap","name":"data_inizio_rap", 'placeholder':''}),
            'data_inizio_rap' : forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px', "id":"data_fine_rap","name":"data_fine_rap",'placeholder':''}),
            }

            # =========== WIDGET DI CONTROLLO ============== # 
            #Super FUnction#
        def __init__(self, *args, **kwargs):
            super(AnaDipendentiCarloForm, self).__init__(*args, **kwargs)
            self.fields['cognome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['nome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['codice_fiscale'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'})
            self.fields['iban'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$'})
            self.fields['provincia_domicilio'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['provincia_nascita'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['email_pers'].widget.attrs.update({'pattern':'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'})
            self.fields['email_lav'].widget.attrs.update({'pattern':'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'})
            self.fields['cellulare'].widget.attrs.update({'data-mask':'(+39) 000-0000000'})
            self.fields['sesso'].queryset = self.fields['sesso'].queryset.order_by('sesso')
            self.fields['societa'].queryset = self.fields['societa'].queryset.order_by('nome_societa')
            self.fields['area'].queryset = self.fields['area'].queryset.order_by('nome_area')
            self.fields['sede'].queryset = self.fields['sede'].queryset.order_by('nome_sede')
            self.fields['istruzione'].queryset = self.fields['istruzione'].queryset.order_by('tipo_istruzione')
            self.fields['tipo_contratto'].queryset = self.fields['tipo_contratto'].queryset.order_by('nome_contratto')
            self.fields['mansione'].queryset = self.fields['mansione'].queryset.order_by('tipo_mansione')

# ---------------------------- END // SUPER FUNCTION -------------------------------- #

#FUNZIONE PER PREVENIRE GLI USER DUPLICATI

    def clean(self):
        data = self.cleaned_data
        
        codice_fiscale = data.get('codice_fiscale')
        if codice_fiscale != None or codice_fiscale != "":
            if codice_fiscale is not None and codice_fiscale != "":
                if len(codice_fiscale) < 16:
                    msg = "Il codice fiscale è troppo breve."
                    self.add_error("codice_fiscale",msg)
                if AnaDipendenti.objects.filter(codice_fiscale=codice_fiscale).exists():            
                    msg = "Questo Codice Fiscale è già in piattaforma."
                    self.add_error("codice_fiscale",msg)
                    
        OK = False
        email_lav = data.get('email_lav')
        email_pers = data.get('email_pers')
        if email_pers == data.get('email_pers'):
            if (email_pers == None and email_lav == None) or (email_pers == "" and email_lav == ""):
                raise forms.ValidationError(f"Impossibile completare la registrazione; il dipendente deve avere almeno un'email.")
            elif (AnaDipendenti.objects.filter(email_pers=email_pers).exclude(codice_fiscale=codice_fiscale).exists()):
                raise forms.ValidationError(f"Impossibile completare la registrazione, l'email {str(email_pers)} è già registrata.")
            else: OK = True
                    
        if OK == False:
            if email_lav == data.get('email_lav'):
                if (email_lav == None and email_pers == None) or (email_lav == "" and email_pers == ""):
                    raise forms.ValidationError(f"Impossibile completare la registrazione; il dipendente deve avere almeno un'email.")
                elif (AnaDipendenti.objects.filter(email_lav=email_lav).exclude(codice_fiscale=codice_fiscale).exists()):
                    raise forms.ValidationError(f"Impossibile completare la registrazione; l'email {str(email_lav)} è già registrata.")
        
        provincia_nascita = data.get('provincia_nascita')
        if provincia_nascita is not None:
            if not has_numbers(provincia_nascita):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia', msg)
        
        provincia_domicilio = data.get('provincia_domicilio')
        if provincia_domicilio is not None:
            if not has_numbers(provincia_domicilio):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia', msg)
                
        provincia_residenza = data.get('provincia_residenza')
        if provincia_residenza is not None:
            if not has_numbers(provincia_residenza):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia_residenza', msg)

        cap = data.get('cap')
        if cap is not None:
            if len(cap) < 5:
                if not(has_alphas(cap)):
                    msg = "Il cap non può contenere lettere o caratteri non numerici."
                    self.add_error('cap',msg)
            
        cellulare = data.get("cellulare")
        if cellulare is not None:
            if not(clean_data(cellulare)):
                msg = "Il numero di cellulare non può contenere caratteri che non siano numeri."
                self.add_error('cellulare',msg)
        
        cell_alternativo = data.get("cell_alternativo")
        if cell_alternativo is not None:
            if not(clean_data(cell_alternativo)):
                msg = "Il numero di cellulare non può contenere caratteri che non siano numeri."
                self.add_error('cell_alternativo',msg)


class AnaDipendentiCarloUpdateForm(forms.ModelForm):
    class Meta:
        model= AnaDipendenti
        exclude = ['id_dip','user','id_stipendio','id_societa','data_creazione','created_at']
        
        CHOICES = (
            ('Attivo','Attivo'),('Cessato','Cessato'),('Sospeso','Sospeso')
        )
        
        labels = {
            'cognome':_("Cognome"),
            'nome':_('Nome'),
            'codice_fiscale':_("Codice Fiscale"),
            'stato':_("Stato"),
            'sesso':_("Sesso"),
            'luogo_nascita':_('Luogo di Nascita'),
            'provincia_nascita':_('Provincia di Nascita'),
            'data_nascita':_('Data di Nascita'),
            'citta_domicilio':_('Città di Domicilio'),
            'indirizzo_domicilio':_('Indirizzo di Domiclio'),
            'provincia_domicilio':_('Provincia di Domiclio'),
            'cap_domicilio':_('Cap Domicilio'),
            'citta_residenza':_('Città di Residenza'),
            'indirizzo_residenza':_('Indirizzo di Residenza'),
            'provincia_residenza':_('Provincia di Residenza'),
            'cap_residenza':_('Cap Residenza'),
            'asl':_('ASL'),
            'email_pers':_('Email Personale'),
            'email_lav':_('Email Lavorativa'),
            'cellulare':_('Cellulare'),
            'cell_alternativo':_('Cell. Alternativo'),
            'iban':_('IBAN'),
            'p_iva':_('Partita IVA'),
            'societa':_('Società'),
            'area':_('Area'),
            'sede':_('Sede'),
            'tipo_contratto':_('Tipologia di contratto'),
            'istruzione':_('Tipo di istruzione'),
            'mansione':_('Mansione'),
            'data_inizio_rap':_('Data Inizio Rapporto'),
            'data_fine_rap':_('Data Fine Rapporto'),
            'note':_('Note')
            }

        widgets= {
            'nome': forms.TextInput(attrs={'placeholder': 'Immetti Nome','style':'font-sitze: 13px; text-transform: capitalize'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Immetti Cognome','style':'font-sitze: 13px; text-transform: capitalize' }),
            'codice_fiscale': forms.TextInput(attrs={'style':'font-sitze: 13px; text-transform: uppercase' }),
            'stato': forms.Select(choices=CHOICES,attrs={"class":"form-control","id":"stato","name":"stato"}),
            'sesso':forms.Select(attrs={"class":"form-control",'placeholder': 'Sesso',"id":"sesso","name":"sesso"}),
            'data_nascita': forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px',"id":"data_nascita","name":"data_nascita", 'placeholder':'' }),
            'luogo_nascita': forms.TextInput(attrs={"class":"form-control","id":"luogo_nascita","name":"luogo_nascita"}),
            'provincia_nascita': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_nascita","name":"provincia_nascita",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'citta_domicilio': forms.TextInput(attrs={"class":"form-control","id":"citta_domicilio","name":"citta_domicilio",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'indirizzo_domicilio': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_domicilio","name":"indirizzo_domicilio",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'provincia_domicilio': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_domicilio","name":"provincia_domicilio",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'cap_domicilio': forms.TextInput(attrs={"class":"form-control",'placeholder': '12345',"id":"cap_domicilio","name":"cap_domicilio"}),
            'citta_residenza': forms.TextInput(attrs={"class":"form-control","id":"citta_residenza","name":"citta_residenza",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'indirizzo_residenza': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_residenza","name":"indirizzo_residenza",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'provincia_residenza': forms.TextInput(attrs={"class":"form-control",'placeholder': 'NA',"id":"provincia_residenza","name":"provincia_residenza",'style':'font-sitze: 13px; text-transform: uppercase'}),
            'cap_residenza': forms.TextInput(attrs={"class":"form-control",'placeholder': '12345',"id":"cap_residenza","name":"cap_residenza"}),
            'asl': forms.TextInput(attrs={"class":"form-control","id":"asl","name":"asl",'style':'font-sitze: 13px; text-transform: capitalize'}),
            'email_lav':forms.TextInput(attrs={"class":"form-control",'placeholder': "Immetti Un' email valida",'style':'font-sitze: 13px; text-transform: lowercase'}),
            'email_pers':forms.TextInput(attrs={"class":"form-control",'placeholder': "Immetti Un' email valida",'style':'font-sitze: 13px; text-transform: lowercase'}),
            'cellulare':forms.TextInput( attrs={"class":"form-control",'style': 'font-sitze: 13px',"id":"cellulare","name":"cellulare", 'placeholder':'Cellulare'}),
            'cell_alternativo':forms.TextInput( attrs={"class":"form-control",'data-mask':'000-0000000' ,'style': 'font-sitze: 13px',"id":"cell_alternativo","name":"cell_alternativo", 'placeholder':'Cellulare', }),
            'iban':forms.TextInput(attrs={"class":"form-control",'placeholder': 'Immetti Un Iban Valido','style':'font-sitze: 13px; text-transform: capitalize'}),
            'p_iva':forms.TextInput(attrs={'placeholder': 'Immetti Una Partita Iva Valida','style':'font-sitze: 13px; text-transform: capitalize'}),
            'societa':forms.Select(attrs={"class":"form-control","id":"societa","name":"societa",'rows': 2, 'cols': 20}),
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
            'istruzione':forms.Select(attrs={"class":"form-control","id":"istruzione","name":"istruzione"}),
            'tipo_contratto':forms.Select(attrs={"class":"form-control","id":"tipocontratto","name":"tipocontratto"}),
            'mansione':forms.Select(attrs={"class":"form-control","id":"mansione","name":"mansione"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"note","name":"note"}),
            'data_fine_rap' : forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px',"id":"data_inizio_rap","name":"data_inizio_rap", 'placeholder':''}),
            'data_inizio_rap' : forms.DateInput(format=('%d-%m-%Y'),attrs={"type":"date","class":"form-control",'style': 'font-sitze: 13px', "id":"data_fine_rap","name":"data_fine_rap",'placeholder':''}),
            }

            # =========== WIDGET DI CONTROLLO ============== # 
            #Super FUnction#
        def __init__(self, *args, **kwargs):
            super(AnaDipendentiCarloForm, self).__init__(*args, **kwargs)
            self.fields['cognome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['nome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['codice_fiscale'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'})
            self.fields['iban'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$'})
            self.fields['provincia_domicilio'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['provincia_nascita'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
            self.fields['email_pers'].widget.attrs.update({'pattern':'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'})
            self.fields['email_lav'].widget.attrs.update({'pattern':'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'})
            self.fields['cellulare'].widget.attrs.update({'data-mask':'(+39) 000-0000000'})
            self.fields['sesso'].queryset = self.fields['sesso'].queryset.order_by('sesso')
            self.fields['societa'].queryset = self.fields['societa'].queryset.order_by('nome_societa')
            self.fields['area'].queryset = self.fields['area'].queryset.order_by('nome_area')
            self.fields['sede'].queryset = self.fields['sede'].queryset.order_by('nome_sede')
            self.fields['istruzione'].queryset = self.fields['istruzione'].queryset.order_by('tipo_istruzione')
            self.fields['tipo_contratto'].queryset = self.fields['tipo_contratto'].queryset.order_by('nome_contratto')
            self.fields['mansione'].queryset = self.fields['mansione'].queryset.order_by('tipo_mansione')

# ---------------------------- END // SUPER FUNCTION -------------------------------- #

#FUNZIONE PER PREVENIRE GLI USER DUPLICATI

    def clean(self):
        data = self.cleaned_data
        
        # codice_fiscale = data.get('codice_fiscale')
        # if codice_fiscale != None or codice_fiscale != "":
        #     if codice_fiscale is not None and codice_fiscale != "":
        #         if len(codice_fiscale) < 16:
        #             msg = "Il codice fiscale è troppo breve."
        #             self.add_error("codice_fiscale",msg)
        #         if AnaDipendenti.objects.filter(codice_fiscale=codice_fiscale).exists():            
        #             msg = "Questo Codice Fiscale è già in piattaforma."
        #             self.add_error("codice_fiscale",msg)
                    
        # OK = False
        # email_pers = data.get('email_pers')
        # if email_pers == data.get('email_pers'):
        #     if (email_pers == None and email_lav == None) or (email_pers == "" and email_lav == ""):
        #         raise forms.ValidationError(f"Impossibile completare la registrazione; il dipendente deve avere almeno un'email.")
        #     elif (AnaDipendenti.objects.filter(email_pers=email_pers).exclude(codice_fiscale=codice_fiscale).exists()):
        #         raise forms.ValidationError(f"Impossibile completare la registrazione, l'email {str(email_pers)} è già registrata.")
        #     else: OK = True
                    
        # if OK == False:
        #     email_lav = data.get('email_lav')
        #     if email_lav == data.get('email_lav'):
        #         if (email_lav == None and email_pers == None) or (email_lav == "" and email_pers == ""):
        #             raise forms.ValidationError(f"Impossibile completare la registrazione; il dipendente deve avere almeno un'email.")
        #         elif (AnaDipendenti.objects.filter(email_lav=email_lav).exclude(codice_fiscale=codice_fiscale).exists()):
        #             raise forms.ValidationError(f"Impossibile completare la registrazione; l'email {str(email_lav)} è già registrata.")
        
        provincia_nascita = data.get('provincia_nascita')
        if provincia_nascita is not None:
            if not has_numbers(provincia_nascita):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia', msg)
        
        provincia_domicilio = data.get('provincia_domicilio')
        if provincia_domicilio is not None:
            if not has_numbers(provincia_domicilio):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia', msg)
                
        provincia_residenza = data.get('provincia_residenza')
        if provincia_residenza is not None:
            if not has_numbers(provincia_residenza):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error('provincia_residenza', msg)

        cap = data.get('cap')
        if cap is not None:
            if len(cap) < 5:
                if not(has_alphas(cap)):
                    msg = "Il cap non può contenere lettere o caratteri non numerici."
                    self.add_error('cap',msg)
            
        cellulare = data.get("cellulare")
        if cellulare is not None:
            if not(clean_data(cellulare)):
                msg = "Il numero di cellulare non può contenere caratteri che non siano numeri."
                self.add_error('cellulare',msg)
        
        cell_alternativo = data.get("cell_alternativo")
        if cell_alternativo is not None:
            if not(clean_data(cell_alternativo)):
                msg = "Il numero di cellulare non può contenere caratteri che non siano numeri."
                self.add_error('cell_alternativo',msg)
