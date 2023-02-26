from django import forms
from .models import Richieste, AddTrasferte, AddStraordinari, TodoList
from django.utils.translation import gettext_lazy as _
from datetime import datetime,date,timedelta, time
import traceback 

class TodoListUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        exclude = ["id_lista","user","fatta","setter","gruppo","data"]
        
        CHOICES = (
            (0,'Bassa'),
            (1,'Media'),
            (2,'Alta'),
            (3,'Urgente'),
        )
        
        labels = {
            'todo':_("Oggetto"),
            'priority':_('Cambia la priorit&#224;')
        }
        
        widgets= {
            'todo': forms.TextInput(attrs={"class":"form-control","id":"todo","name":"todo"}),
            'priority': forms.Select(choices=CHOICES,attrs={"class":"form-control",'id':'priority','name':'priority'}),
        } 


class AddTrasferteFormRichiesta(forms.ModelForm):
    class Meta:
        model = AddTrasferte
        exclude = ["id_trasferte","id_dip","id_ced","ore","valore","timestamp"]
        localized_field = ('rel_giorno')
        labels = {
            'rel_giorno':_("Giornata"),
            'note':_('Motivazione')
        }
        
        widgets= {
            'rel_giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"rel_giorno","name":"rel_giorno"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }
        
    def clean_rel_giorno(self, *args, **kwargs):
        giorno = self.cleaned_data["rel_giorno"]

        today = datetime.today().date()
        if giorno < today:
            msg = "Il giorno di richiesta non può essere precedente a quello odierno."
            self.add_error("rel_giorno",msg)
            return giorno
        else: return giorno



class AddStraordinario(forms.ModelForm):
    class Meta:
        model = AddStraordinari
        exclude = ["id_trasferte","id_dip","id_ced","ore","valore","timestamp"]
        localized_fields = ('rel_giorno','rel_time_start','rel_time_end')
        labels = {
            'rel_giorno':_("Data"),
            'rel_time_start':_("Inizio"),
            'rel_time_end':_("Fine"),
            'note':_('Motivazione')
        }
        
        widgets= {
            'rel_giorno': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"rel_giorno","name":"rel_giorno"}),
            'rel_time_start':forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"rel_time_start","name":"rel_time_start"}),
            'rel_time_end':forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","id":"rel_time_end","name":"rel_time_end"}),
            'note': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }
            
    def clean_rel_giorno(self, *args, **kwargs):
        giorno = self.cleaned_data["rel_giorno"]

        today = datetime.today().date()
        if giorno < today:
            msg = "Il giorno di richiesta non può essere precedente a quello odierno."
            self.add_error("rel_giorno",msg)
            return giorno
        else: return giorno

    
    def clean(self):
        data = super().clean()
        giorno = data.get("rel_giorno")
        da_ora = data.get("rel_time_start")
        a_ora = data.get("rel_time_end")
        hour_da_ora = da_ora.hour
        minutes_da_ora = da_ora.minute
        hour_a_ora = a_ora.hour
        minutes_a_ora = a_ora.minute
        
        if hour_a_ora < hour_da_ora or (hour_a_ora < hour_da_ora and minutes_a_ora < minutes_da_ora):
            msg = "L'ora di fine non può essere precedente a quella di inizio."
            self.add_error("rel_time_start",msg)
            self.add_error("rel_time_end", msg)
        return self.cleaned_data


class CreateRichiestaForm(forms.ModelForm):
    class Meta:
        model=Richieste
        fields= ('id_permessi_richieste','da_giorno_richiesta', 'a_giorno_richiesta', 'urgente', 'note_richiesta')
        localized_fields = ('da_giorno_richiesta', 'a_giorno_richiesta')
        labels = {
            'id_permessi_richieste':_('Tipologia permesso'),
            'da_giorno_richiesta':_("Giorno d'inizio"),
            'a_giorno_richiesta':_('Giorno di rientro'),
            'urgente':_("Urgente?"),
            'note_richiesta':_('Vuoi lasciare altre info?')
        }
        
        widgets= {
            'id_permessi_richieste':forms.Select(attrs={"class":"form-control","id":"id_permessi_richieste","name":"permesso"}),
            'da_giorno_richiesta': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"da_giorno","name":"da_giorno_richiesta"}),
            'a_giorno_richiesta':forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"a_giorno","name":"a_giorno_richiesta"}),
            'urgente': forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-check-input","id":"urgente","name":"urgente"}),
            'note_richiesta': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        } 
    
    def clean(self):
        cleaned_data = super(CreateRichiestaForm, self).clean()
        da_giorno= cleaned_data.get("da_giorno_richiesta")
        a_giorno= cleaned_data.get("a_giorno_richiesta")
        permesso = cleaned_data.get("id_permessi_richieste")
        urgente = cleaned_data.get("urgente")

        if a_giorno < da_giorno:
            msg= "Il giorno di ritorno non può essere precedente a quello di inizio."
            self.add_error("da_giorno_richiesta",msg)
            self.add_error("a_giorno_richiesta", msg)
        
        if urgente == False:
        
            if int(permesso.id_permesso) in [1,5,13,16]:
                startDay = datetime.today().date() + timedelta(days=1)
                if startDay < da_giorno:
                    msg= "Il giorno di inizio permesso non può essere inferiore a domani."
                    self.add_error("da_giorno_richiesta",msg)
                    return startDay
                if startDay > a_giorno:
                    msg= "Il giorno di fine permesso non può essere inferiore a dopodomani."
                    self.add_error("a_giorno_richiesta",msg)
                    return a_giorno
                else:
                    return da_giorno
            elif int(permesso.id_permesso) == 9:
                startDay = datetime.today().date() + timedelta(days=5)
                if startDay < da_giorno:
                    msg= f"Il giorno di inizio permesso non può essere precedente al {startDay}."
                    self.add_error("da_giorno_richiesta",msg)
                    return startDay
                if startDay > a_giorno:
                    msg= f"Il giorno di fine permesso non può essere precedente al {startDay}."
                    self.add_error("a_giorno_richiesta",msg)
                    return a_giorno
                else:
                    return da_giorno
            elif int(permesso.id_permesso) in [6,7,8,10,12,14]:
                startDay = datetime.today().date() + timedelta(days=10)
                if startDay < da_giorno:
                    msg= f"Il giorno di inizio permesso non può essere precedente al {startDay}."
                    self.add_error("da_giorno_richiesta",msg)
                    return startDay
                if startDay > a_giorno:
                    msg= f"Il giorno di fine permesso non può essere precedente al {startDay}."
                    self.add_error("a_giorno_richiesta",msg)
                    return a_giorno
                else:
                    return da_giorno
            elif int(permesso.id_permesso) in [3,4]:
                startDay = datetime.today().date() + timedelta(days=15)
                if startDay < da_giorno:
                    msg= f"Il giorno di inizio permesso non può essere precedente al {startDay}."
                    self.add_error("da_giorno_richiesta",msg)
                    return startDay
                if startDay > a_giorno:
                    msg= f"Il giorno di fine permesso non può essere precedente al {startDay}."
                    self.add_error("a_giorno_richiesta",msg)
                    return a_giorno
                else:
                    return da_giorno
            elif int(permesso.id_permesso) == 2:
                startDay = datetime.today().date() + timedelta(days=60)
                if startDay < da_giorno:
                    msg= f"Il giorno di inizio permesso non può essere precedente al {startDay}."
                    self.add_error("da_giorno_richiesta",msg)
                    return startDay
                if startDay > a_giorno:
                    msg= f"Il giorno di fine permesso non può essere precedente al {startDay}."
                    self.add_error("a_giorno_richiesta",msg)
                    return a_giorno
                else:
                    return da_giorno

            else:
                return da_giorno
        return self.cleaned_data



class CreateRichiestaOrarioForm(forms.ModelForm):
    class Meta:
        model=Richieste
        fields= ('da_giorno_richiesta', 'da_ora_richiesta', 'a_ora_richiesta', 'urgente', 'note_richiesta')
        exclude=['id_permessi_richieste','a_giorno_richiesta']
        localized_fields = ('da_giorno_richiesta','da_ora_richiesta', 'a_ora_richiesta')
        labels = {
            'da_giorno_richiesta':_("Giorno d'interesse"),
            'da_ora_richiesta':_("Ora d'inizio"),
            'a_ora_richiesta':_("Ora di rientro"),
            'urgente':_("Urgente?"),
            'note_richiesta':_('Vuoi lasciare altre info?')
        }
        
        widgets= {
            'da_giorno_richiesta': forms.DateInput(format=('%Y-%m-%d'),attrs={"type":"date","class":"form-control","id":"da_giorno_richiestaOra","name":"da_giorno_richiesta"}),
            'da_ora_richiesta': forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"da_ora_ora","name":"da_ora_richiesta"}),
            'a_ora_richiesta':forms.TimeInput(format=('%H:%M'),attrs={"type":"time","class":"form-control","min":"09:00","max":"18:00","id":"a_ora_ora","name":"a_ora_richiesta"}),
            'urgente': forms.CheckboxInput(attrs={"type":"checkbox", "class":"form-check-input","id":"urgenteOra","name":"urgente"}),
            'note_richiesta': forms.Textarea(attrs={"class":"form-control","id":"floatingTextarea2", "rows":4, "cols":62}),
        }
    def __init__(self, *args, **kwargs):
        super(CreateRichiestaOrarioForm, self).__init__(*args, **kwargs)
        self.fields['da_ora_richiesta'].widget.attrs.update({'required': 'required',})
        self.fields['a_ora_richiesta'].widget.attrs.update({'required': 'required'})
    
    def clean(self):
        cleaned_data = self.cleaned_data
        da_giorno = cleaned_data.get("da_giorno_richiesta")
        da_ora= cleaned_data.get("da_ora_richiesta")
        a_ora= cleaned_data.get("a_ora_richiesta")
        urgente= cleaned_data.get("urgente")
        
        if a_ora < da_ora:
            msg = "L'ora di ritorno non può essere precedente a quella di inizio."
            self.add_error("da_ora_richiesta",msg)
            self.add_error("a_ora_richiesta", msg)
    
        if urgente == False:

            today = datetime.today().date()
            if da_giorno < today:
                msg = "Il giorno di richiesta non può essere precedente a quello odierno."
                self.add_error("da_giorno_richiesta",msg)


