from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

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

class DipendentiForm(forms.ModelForm):
    class Meta:
        model = AnaDipendenti
        fields = "__all__"
        exclude = ["user","dip_capo_area","id_capo_area","id_stipendio","id_societa","data_creazione"]

        STATO = (('Attivo','Attivo'),('Cessato','Cessato'),('Sospeso','Sospeso'))
        
        labels = {
            'cognome':_("Cognome"),
            'nome':_('Nome'),
            'sesso':_("Sesso"),
            'codice_fiscale':_("Codice Fiscale"),
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
            'cellulare':_('Cellulare'),
            'cell_alternativo':_('Cell. Alternativo'),
            'email_pers':_('Email Personale'),
            'email_lav':_('Email Lavorativa'),
            'iban':_('IBAN'),
            'p_iva':_('Partita IVA'),
            'societa':_('Società'),
            'area':_('Area'),
            'istruzione':_('Tipo di istruzione'),
            'societacontratto':_('Società Contrattuale'),
            'tipo_contratto':_('Tipologia di contratto'),
            'mansione':_('Mansione'),
            'data_inizio_rap':_('Data Inizio Rapporto'),
            'data_fine_rap':_('Data Fine Rapporto'),
            'stato':_('Stato'),
            }
        
        widgets= {
            'sesso':forms.Select(attrs={"class":"form-control","id":"sesso","name":"sesso"}),
            'codice_fiscale': forms.TextInput(attrs={"class":"form-control","id":"codice_fiscale","name":"codice_fiscale"}),
            'luogo_nascita': forms.TextInput(attrs={"class":"form-control","id":"luogo_nascita","name":"luogo_nascita"}),
            'provincia_nascita': forms.TextInput(attrs={"class":"form-control","id":"provincia_nascita","name":"provincia_nascita"}),
            'data_nascita': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"da_nascita","name":"da_nascita"}),
            'citta_domicilio': forms.TextInput(attrs={"class":"form-control","id":"citta_domicilio","name":"citta_domicilio"}),
            'indirizzo_domicilio': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_domicilio","name":"indirizzo_domicilio"}),
            'provincia_domicilio': forms.TextInput(attrs={"class":"form-control","id":"provincia_domicilio","name":"provincia_domicilio"}),
            'cap_domicilio': forms.TextInput(attrs={"class":"form-control","id":"cap_domicilio","name":"cap_domicilio"}),
            'citta_residenza': forms.TextInput(attrs={"class":"form-control","id":"citta_residenza","name":"citta_residenza"}),
            'indirizzo_residenza': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_residenza","name":"indirizzo_residenza"}),
            'provincia_residenza': forms.TextInput(attrs={"class":"form-control","id":"provincia_residenza","name":"provincia_residenza"}),
            'cap_residenza': forms.TextInput(attrs={"class":"form-control","id":"cap_residenza","name":"cap_residenza"}),
            'asl': forms.TextInput(attrs={"class":"form-control","id":"asl","name":"asl"}),
            'cellulare': forms.TextInput(attrs={"class":"form-control","id":"cellulare","name":"cellulare"}),
            'cell_alternativo': forms.TextInput(attrs={"class":"form-control","id":"cell_alternativo","name":"cell_alternativo"}),
            'email_pers': forms.TextInput(attrs={"class":"form-control","id":"email_pers","name":"email_pers"}),
            'email_lav': forms.TextInput(attrs={"class":"form-control","id":"email_lav","name":"email_lav"}),
            'iban': forms.TextInput(attrs={"class":"form-control","id":"iban","name":"iban"}),
            'p_iva': forms.TextInput(attrs={"class":"form-control","id":"p_iva","name":"p_iva"}),
            'societa':forms.Select(attrs={"class":"form-control","id":"societa","name":"societa",'rows': 2, 'cols': 20}),
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'istruzione':forms.Select(attrs={"class":"form-control","id":"istruzione","name":"istruzione"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
            'tipo_contratto':forms.Select(attrs={"class":"form-control","id":"tipocontratto","name":"tipocontratto"}),
            'mansione':forms.Select(attrs={"class":"form-control","id":"mansione","name":"mansione"}),
            'data_inizio_rap': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_inizio_rap","name":"data_inizio_rap"}),
            'data_fine_rap': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_fine_rap","name":"data_fine_rap"}),
            'stato': forms.Select(choices=STATO,attrs={'class': 'form-select'}),
            'note': forms.TextInput(attrs={"class":"form-control","id":"note","name":"note"}),
        }
    
    def __init__(self, *args, **kwargs):
        super(DipendentiForm, self).__init__(*args, **kwargs)
        self.fields['cognome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['nome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['codice_fiscale'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'})
        self.fields['provincia_domicilio'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['provincia_nascita'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['societa'].queryset = self.fields['societa'].queryset.order_by('nome_societa')
        self.fields['area'].queryset = self.fields['area'].queryset.order_by('nome_area')
        self.fields['sede'].queryset = self.fields['sede'].queryset.order_by('nome_sede')
        self.fields['istruzione'].queryset = self.fields['istruzione'].queryset.order_by('tipo_istruzione')
        self.fields['tipo_contratto'].queryset = self.fields['tipo_contratto'].queryset.order_by('nome_contratto')
        self.fields['mansione'].queryset = self.fields['mansione'].queryset.order_by('tipo_mansione')
        
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        nome= cleaned_data.get("nome")
        cognome= cleaned_data.get("cognome")
        email_pers= cleaned_data.get("email_pers")
        email_lav= cleaned_data.get("email_lav")
        codice_fiscale= cleaned_data.get("codice_fiscale")
        provincia_nascita= cleaned_data.get("provincia_nascita")
        provincia_domicilio= cleaned_data.get("provincia_domicilio")
        provincia_residenza= cleaned_data.get("provincia_residenza")
        cap= cleaned_data.get("cap")
        cellulare= cleaned_data.get("cellulare")
        cell_alternativo= cleaned_data.get("cell_alternativo")
        iban= cleaned_data.get("iban")

        if codice_fiscale:
            if len(codice_fiscale) > 16:
                msg = "Il codice fiscale è troppo lungo."
                self.add_error("codice_fiscale",msg)
            elif len(codice_fiscale) < 16:
                msg = "Il codice fiscale è troppo breve."
                self.add_error("codice_fiscale",msg)
                
            if AnaDipendenti.objects.filter(codice_fiscale=codice_fiscale).exists():            
                msg = "Questo Codice Fiscale è già in piattaforma."
                self.add_error("codice_fiscale",msg)    
                         
        if email_pers:
            if AnaDipendenti.objects.filter(email_pers=email_pers).exists(): 
                msg= "Questa email già esiste in piattaforma."
                self.add_error("email_pers",msg)

        if email_lav:
            if AnaDipendenti.objects.filter(email_lav=email_lav).exclude(codice_fiscale=codice_fiscale).exists(): 
                msg= "Questa email già esiste in piattaforma."
                self.add_error("email_lav",msg)
                          
        if provincia_nascita:
            if not(has_numbers(provincia_nascita)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
                
        if provincia_domicilio:
            if not(has_numbers(provincia_domicilio)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
            
        if provincia_residenza:
            if not(has_numbers(provincia_residenza)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
        if cap:
            if not(has_alphas(cap)):
                msg = "Il cap non può contenere lettere o caratteri non numerici."
                self.add_error['cap',msg]
        if cellulare:
            if not(clean_data(cellulare)):
                msg = "Il numero di cellulare non può contenere non numeri ad esclusione del '+'."
                self.add_error['cellulare',msg]
        if cell_alternativo:
            if not(clean_data(cell_alternativo)):
                msg = "Il numero di cellulare non può contenere non numeri ad esclusione del '+'."
                self.add_error['cell_alternativo',msg]
        if iban:        
            if len(iban) > 34:
                msg = "L'IBAN non può contenere caratteri speciali, ne essere più lungo di 34 caratteri."
                self.add_error['iban',msg]


class UpdateDipendentiForm(forms.ModelForm):
    class Meta:
        model = AnaDipendenti
        fields = "__all__"
        exclude = ["user","dip_capo_area","id_capo_area","id_stipendio","id_societa","data_creazione"]

        STATO = (('Attivo','Attivo'),('Cessato','Cessato'),('Sospeso','Sospeso'))
        
        labels = {
            'cognome':_("Cognome"),
            'nome':_('Nome'),
            'sesso':_("Sesso"),
            'codice_fiscale':_("Codice Fiscale"),
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
            'cellulare':_('Cellulare'),
            'cell_alternativo':_('Cell. Alternativo'),
            'email_pers':_('Email Personale'),
            'email_lav':_('Email Lavorativa'),
            'iban':_('IBAN'),
            'p_iva':_('Partita IVA'),
            'societa':_('Società'),
            'area':_('Area'),
            'istruzione':_('Tipo di istruzione'),
            'societacontratto':_('Società Contrattuale'),
            'tipo_contratto':_('Tipologia di contratto'),
            'mansione':_('Mansione'),
            'data_inizio_rap':_('Data Inizio Rapporto'),
            'data_fine_rap':_('Data Fine Rapporto'),
            'stato':_('Stato'),
            }
        
        widgets= {
            'sesso':forms.Select(attrs={"class":"form-control","id":"sesso","name":"sesso"}),
            'codice_fiscale': forms.TextInput(attrs={"class":"form-control","id":"codice_fiscale","name":"codice_fiscale"}),
            'luogo_nascita': forms.TextInput(attrs={"class":"form-control","id":"luogo_nascita","name":"luogo_nascita"}),
            'provincia_nascita': forms.TextInput(attrs={"class":"form-control","id":"provincia_nascita","name":"provincia_nascita"}),
            'data_nascita': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"da_nascita","name":"da_nascita"}),
            'citta_domicilio': forms.TextInput(attrs={"class":"form-control","id":"citta_domicilio","name":"citta_domicilio"}),
            'indirizzo_domicilio': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_domicilio","name":"indirizzo_domicilio"}),
            'provincia_domicilio': forms.TextInput(attrs={"class":"form-control","id":"provincia_domicilio","name":"provincia_domicilio"}),
            'cap_domicilio': forms.TextInput(attrs={"class":"form-control","id":"cap_domicilio","name":"cap_domicilio"}),
            'citta_residenza': forms.TextInput(attrs={"class":"form-control","id":"citta_residenza","name":"citta_residenza"}),
            'indirizzo_residenza': forms.TextInput(attrs={"class":"form-control","id":"indirizzo_residenza","name":"indirizzo_residenza"}),
            'provincia_residenza': forms.TextInput(attrs={"class":"form-control","id":"provincia_residenza","name":"provincia_residenza"}),
            'cap_residenza': forms.TextInput(attrs={"class":"form-control","id":"cap_residenza","name":"cap_residenza"}),
            'asl': forms.TextInput(attrs={"class":"form-control","id":"asl","name":"asl"}),
            'cellulare': forms.TextInput(attrs={"class":"form-control","id":"cellulare","name":"cellulare"}),
            'cell_alternativo': forms.TextInput(attrs={"class":"form-control","id":"cell_alternativo","name":"cell_alternativo"}),
            'email_pers': forms.TextInput(attrs={"class":"form-control","id":"email_pers","name":"email_pers"}),
            'email_lav': forms.TextInput(attrs={"class":"form-control","id":"email_lav","name":"email_lav"}),
            'iban': forms.TextInput(attrs={"class":"form-control","id":"iban","name":"iban"}),
            'p_iva': forms.TextInput(attrs={"class":"form-control","id":"p_iva","name":"p_iva"}),
            'societa':forms.Select(attrs={"class":"form-control","id":"societa","name":"societa",'rows': 2, 'cols': 20}),
            'area':forms.Select(attrs={"class":"form-control","id":"area","name":"area"}),
            'istruzione':forms.Select(attrs={"class":"form-control","id":"istruzione","name":"istruzione"}),
            'sede':forms.Select(attrs={"class":"form-control","id":"sede","name":"sede"}),
            'tipo_contratto':forms.Select(attrs={"class":"form-control","id":"tipocontratto","name":"tipocontratto"}),
            'mansione':forms.Select(attrs={"class":"form-control","id":"mansione","name":"mansione"}),
            'data_inizio_rap': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_inizio_rap","name":"data_inizio_rap"}),
            'data_fine_rap': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"data_fine_rap","name":"data_fine_rap"}),
            'stato': forms.Select(choices=STATO,attrs={'class': 'form-select'}),
            'note': forms.TextInput(attrs={"class":"form-control","id":"note","name":"note"}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UpdateDipendentiForm, self).__init__(*args, **kwargs)
        self.fields['cognome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['nome'].widget.attrs.update({'required': 'required','pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['codice_fiscale'].widget.attrs.update({'required': 'required','pattern':'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'})
        self.fields['provincia_domicilio'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['provincia_nascita'].widget.attrs.update({'pattern':'^[A-Za-z][a-zA-Z\' ]*$'})
        self.fields['societa'].queryset = self.fields['societa'].queryset.order_by('nome_societa')
        self.fields['area'].queryset = self.fields['area'].queryset.order_by('nome_area')
        self.fields['sede'].queryset = self.fields['sede'].queryset.order_by('nome_sede')
        self.fields['istruzione'].queryset = self.fields['istruzione'].queryset.order_by('tipo_istruzione')
        self.fields['tipo_contratto'].queryset = self.fields['tipo_contratto'].queryset.order_by('nome_contratto')
        self.fields['mansione'].queryset = self.fields['mansione'].queryset.order_by('tipo_mansione')
        
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        nome= cleaned_data.get("nome")
        cognome= cleaned_data.get("cognome")
        email_pers= cleaned_data.get("email_pers")
        email_lav= cleaned_data.get("email_lav")
        codice_fiscale= cleaned_data.get("codice_fiscale")
        provincia_nascita= cleaned_data.get("provincia_nascita")
        provincia_domicilio= cleaned_data.get("provincia_domicilio")
        provincia_residenza= cleaned_data.get("provincia_residenza")
        cap= cleaned_data.get("cap")
        cellulare= cleaned_data.get("cellulare")
        cell_alternativo= cleaned_data.get("cell_alternativo")
        iban= cleaned_data.get("iban")

        if codice_fiscale:
            if len(codice_fiscale) > 16:
                msg = "Il codice fiscale è troppo lungo."
                self.add_error("codice_fiscale",msg)
            elif len(codice_fiscale) < 16:
                msg = "Il codice fiscale è troppo breve."
                self.add_error("codice_fiscale",msg)
                
        if provincia_nascita:
            if not(has_numbers(provincia_nascita)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
                
        if provincia_domicilio:
            if not(has_numbers(provincia_domicilio)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
            
        if provincia_residenza:
            if not(has_numbers(provincia_residenza)):
                msg = "La provincia non può contenere numeri o caratteri non alfanumerici."
                self.add_error['provincia',msg]
        if cap:
            if not(has_alphas(cap)):
                msg = "Il cap non può contenere lettere o caratteri non numerici."
                self.add_error['cap',msg]
        if cellulare:
            if not(clean_data(cellulare)):
                msg = "Il numero di cellulare non può contenere non numeri ad esclusione del '+'."
                self.add_error['cellulare',msg]
        if cell_alternativo:
            if not(clean_data(cell_alternativo)):
                msg = "Il numero di cellulare non può contenere non numeri ad esclusione del '+'."
                self.add_error['cell_alternativo',msg]
        if iban:        
            if len(iban) > 34:
                msg = "L'IBAN non può contenere caratteri speciali, ne essere più lungo di 34 caratteri."
                self.add_error['iban',msg]

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
            'nome_Area':_("Nome Area"),
            'note':_('Note'),
            }
        widgets= {
            'nome_Area' : forms.TextInput(),
            'note' : forms.Textarea()
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
            'tipo_istruzione' : forms.TextInput(),
            'note' : forms.Textarea()
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
            'tipo_mansione' : forms.TextInput(),
            'note' : forms.Textarea()
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
            'nome_sede' : forms.TextInput(),
            'note' : forms.Textarea()
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
            'nome_societa' : forms.TextInput(),
            'note' : forms.Textarea()
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
            'nome_contratto' : forms.TextInput(),            
            'note' : forms.Textarea()
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
            'perc_contratto' : forms.TextInput(),
            'note' : forms.Textarea()
        }


class ContrattiFormInsert(forms.ModelForm):
    dipendente = forms.ModelChoiceField(queryset=AnaDipendenti.objects.filter(stato='Attivo'),widget=forms.Select(attrs={"class":"form-control","id":"dipendente","name":"dipendente"}))

    class Meta:
        model = Contratti
        fields = ["dipendente","id_societa","tipologia","percentuale",'datainizio','datafine','note']
        exclude = ["id_contratto","id_dip",'codicecontratto']

        labels = {
            'dipendente':_('Dipendente'),
            'id_societa':_('Società'),
            'tipologia':_('Tipologia'),
            'percentuale':_('Percentuale'),
            'datainizio':_('Data Inizio'),
            'datafine':_('Data Fine'),
            'note':_('Note'),
            }
        
        widgets= {
            'id_societa' : forms.Select(attrs={"class":"form-control","id":"id_societa","name":"id_societa"}),
            'tipologia' : forms.Select(attrs={"class":"form-control","id":"tipologia","name":"tipologia"}),
            'percentuale' : forms.Select(attrs={"class":"form-control","id":"perc_contratto","name":"perc_contratto"}),
            'datainizio': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datainizio","name":"datainizio"}),
            'datafine': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datafine","name":"datafine"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }


class ContrattiFormUpdate(forms.ModelForm):
    class Meta:
        model = Contratti
        fields = ["id_societa","tipologia","percentuale",'datainizio','datafine','note']
        exclude = ["id_contratto","id_dip"]

        labels = {
            'id_societa':_('Società'),
            'tipologia':_('Tipologia'),
            'percentuale':_('Percentuale'),
            'datainizio':_('Data Inizio'),
            'datafine':_('Data Fine'),
            'note':_('Note'),
            }
        
        widgets= {
            'id_societa' : forms.Select(attrs={"class":"form-control","id":"id_societa","name":"id_societa"}),
            'tipologia' : forms.Select(attrs={"class":"form-control","id":"tipologia","name":"tipologia"}),
            'percentuale' : forms.Select(attrs={"class":"form-control","id":"perc_contratto","name":"perc_contratto",'floatformat':2}),
            'datainizio': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datainizio","name":"datainizio"}),
            'datafine': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"datafine","name":"datafine"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }