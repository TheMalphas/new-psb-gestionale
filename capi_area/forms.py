from django import forms
from .models import AnaDipendenti, Richieste, Ingressidip, AuthUser
from django.utils.translation import gettext_lazy as _


class DipendentiForm(forms.ModelForm):
    class Meta:
        model = AnaDipendenti
        fields = ["id_dip"]
        exclude = [""]
        
        widgets = {
            'id_dip' : forms.Select(attrs={'type':'select','name':'dipendente', 'id':'dipendente','aria-label':'form-select-lg example','class':'form-select form-select-md mb-2 form-control'}),
}

class UpdateEntrata(forms.ModelForm):
    class Meta:
        model= Ingressidip
        fields= "__all__"


class UpdateRichiestaForm(forms.ModelForm):
    class Meta:
        model = Richieste
        fields = ['stato']

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        da_giorno_richiesta = cleaned_data.get("da_giorno_richiesta")
        a_giorno_richiesta = cleaned_data.get("a_giorno_richiesta")
        da_giorno_richiesta = str(da_giorno_richiesta)
        a_giorno_richiesta = str(a_giorno_richiesta)

        if da_giorno_richiesta < self.mock_initial_da_giorno:
            pass
        elif a_giorno_richiesta < da_giorno_richiesta:
            raise forms.ValidationError(_("Attenzione: il giorno di fine permesso non pu&#242; essere precedente a quello di inizio."))
        else:
            raise forms.ValidationError(_("Attenzione: il giorno di inizio permesso non pu&#242; essere precedente a quello gi&#224; scelto."))