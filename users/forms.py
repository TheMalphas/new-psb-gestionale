from django import forms
from .models import Richieste
from django.utils.translation import gettext_lazy as _


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
    
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        da_giorno= cleaned_data.get("da_giorno_richiesta")
        a_giorno= cleaned_data.get("a_giorno_richiesta")
        anno_da_giorno = da_giorno.year
        mese_da_giorno = da_giorno.month
        giorno_da_giorno = da_giorno.day
        anno_a_giorno = a_giorno.year
        mese_a_giorno = a_giorno.month
        giorno_a_giorno = a_giorno.day
        
        if anno_a_giorno < anno_da_giorno or mese_a_giorno < mese_da_giorno or (mese_a_giorno < mese_da_giorno and giorno_a_giorno < giorno_da_giorno) or (giorno_a_giorno < giorno_da_giorno and mese_a_giorno == mese_da_giorno):
            msg= "Il giorno di ritorno non pu&#242; essere precedente a quello di inizio."
            self.add_error("da_giorno_richiesta",msg)
            self.add_error("a_giorno_richiesta", msg)


class CreateRichiestaOrarioForm(forms.ModelForm):
    class Meta:
        model=Richieste
        fields= ('id_permessi_richieste','da_giorno_richiesta', 'da_ora_richiesta', 'a_ora_richiesta', 'urgente', 'note_richiesta')
        exclude=['a_giorno_richiesta']
        localized_fields = ('da_ora_richiesta', 'a_ora_richiesta')
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
    def clean(self, *args, **kwargs):
        cleaned_data= super().clean()
        da_ora= cleaned_data.get("da_ora_richiesta")
        a_ora= cleaned_data.get("a_ora_richiesta")
        hour_da_ora = da_ora.hour
        minutes_da_ora = da_ora.minute
        hour_a_ora = a_ora.hour
        minutes_a_ora = a_ora.minute
        
        if hour_a_ora < hour_da_ora or (hour_a_ora < hour_da_ora and minutes_a_ora < minutes_da_ora):
            msg= "L'ora di ritorno non pu&#242; essere precedente a quello di inizio."
            self.add_error("da_ora_richiesta",msg)
            self.add_error("a_ora_richiesta", msg)