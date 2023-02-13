from django.apps import AppConfig
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date, timedelta
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.db.models import Q
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput, inlineformset_factory
from django.urls import reverse, reverse_lazy
from .models import Richieste, AuthUser, AnaDipendenti, CapoArea, Permessi, RichiesteAccettate, Ingressidip
from .models import Area, Istruzione, Sede, Societa, TipoContratto, Cedolini as ced
from .models import AddIncForf, AddRimborsi, AddTrasferte
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django import forms
from .forms import CreaCedoliniForm, AddInc_ForfForm, AddTrasferteForm
from datetime import time, datetime, timedelta
from django.contrib.auth.views import redirect_to_login
from django.db.models import Count
from django.contrib import messages
from django.utils import timezone

def convertMese(mes):
    mes=int(mes)
    if mes == 1:
        return "Gennaio"
    elif mes == 2:
        return 'Febbraio'
    elif mes == 3:
        return 'Marzo'
    elif mes == 4:
        return 'Aprile'
    elif mes == 5:
        return 'Maggio'
    elif mes == 6:
        return 'Giugno'
    elif mes == 7:
        return 'Luglio'
    elif mes == 8:
        return 'Agosto'
    elif mes == 9:
        return 'Settembre'
    elif mes == 10:
        return 'Ottobre'
    elif mes == 11:
        return 'Novembre'
    elif mes == 12:
        return 'Dicembre'

def invertMese(mes):
    if mes == "1":
        return 1
    elif mes == '2':
        return 2
    elif mes == '3':
        return 3
    elif mes == '4':
        return 4
    elif mes == '5':
        return 5
    elif mes == '6':
        return 6
    elif mes == '7':
        return 7
    elif mes == '8':
        return 8
    elif mes == '9':
        return 9
    elif mes == '10':
        return 10
    elif mes == '11':
        return 11
    elif mes == '12':
        return 12

# Cedolini
    
# @login_required    
# def createFerie(request,pk):
#     FerieFormSet=inlineformset_factory(ced, AddFerie,form=AddFerieForm, extra=1)
#     cedolinoObj=ced.objects.get(id_cedolino=pk)
#     formset=FerieFormSet(instance=cedolinoObj)
#     context= {'formset':formset}
#     context['pk']=cedolinoObj.id_cedolino
#     if request.method=="POST":
#         formset = FerieFormSet(request.POST,instance=cedolinoObj)
#         if formset.is_valid():
#             formset.clean()
#             formset.save()
#             return redirect('/cedolini/')
#         else:
#             print(formset.errors)
#     return render(request, 'cedolini/add_ferie.html',context)


@login_required
def createIncForf(request,pk):
    template_name = 'cedolini/add_inc_forf.html'
    cedolinoObj=ced.objects.get(id_cedolino=pk)
    AddIncForfSet=inlineformset_factory(ced, AddIncForf,form=AddInc_ForfForm, extra=1, max_num=1)
    formset=AddIncForfSet(instance=cedolinoObj)
    context= {'formset':formset}
    context['pk']=cedolinoObj.id_cedolino
    if request.method=="POST":
        formset = AddIncForfSet(request.POST,instance=cedolinoObj)
        if formset.is_valid():
            formset.save()
            return redirect('cedolini:cedolino',pk=cedolinoObj.id_cedolino)
        else:
            print(formset.errors)
    print("hello")
    return render(request, template_name,context)


class CedoliniList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ced 
    paginate_by = 8
    context_object_name= "cedolini"
    permission_required = 'gestione.change_anadipendenti'
    template_name = "cedolini/cedolini.html"
    annoglob = ""
    meseglob = ""
    
    def get_context_data(self, **kwargs):
        context = super(CedoliniList,self).get_context_data(**kwargs)
        annoData = self.annoglob
        meseData = convertMese(self.meseglob)
        context["anno"] = annoData
        context["mese"] = meseData
        return context
    
    def get_queryset(self):
        year = datetime.now().year
        self.annoglob = str(year)
        dip = self.request.GET.get("dipendente") or ""
        mesex = self.request.GET.get("mesex") or ""
        month = datetime.now().month
        
        if mesex == "" or mesex == None:
            mesex = month
            self.meseglob = mesex
        elif mesex != "" or mesex != None:
            mesex = invertMese(mesex)
            self.meseglob = mesex
        
        try:
            if mesex == month and (dip == None or dip == ""):
                queryset = ced.objects.filter(anno=year,mese=mesex).order_by('dipendente__cognome')
                return queryset
            
            elif (mesex != "" or mesex != None) and dip == "":
                mesex=self.request.GET.get("mesex")
                queryset = ced.objects.filter(anno=year,mese=mesex).order_by('dipendente__cognome')
                return queryset
            
            elif mesex == "" and dip != "":
                queryset = ced.objects.filter(anno=year,mese=mesex).filter(Q(dipendente__nome__icontains=dip) | Q(dipendente__cognome__icontains=dip)).order_by('dipendente__cognome')
                return queryset
            
            elif (mesex != "" or mesex != None) and (dip != "" or dip != None):
                queryset = ced.objects.filter(anno=year,mese=mesex).filter(Q(dipendente__nome__icontains=dip) | Q(dipendente__cognome__icontains=dip)).order_by('dipendente__cognome')
                return queryset
        except Exception as error:
            print(error)

class CedolinoDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model= ced
    context_object_name = "cedolino"
    template_name = "cedolini/cedolino.html"
    permission_required = 'gestione.change_anadipendenti'
    mese = ""
    
    def get_object(self):
        id_ced = self.kwargs.get("id_cedolino")
        cedo=ced.objects.get(id_cedolino=id_ced)
        mese=cedo.mese
        self.mese= convertMese(mese)
        return get_object_or_404(ced, id_cedolino=id_ced)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cedolino = ced.objects.get(id_cedolino=self.object.pk)
        context['mese'] = convertMese(cedolino.mese)
        context['cedolinoobj'] = cedolino
        return context
    
    def handle_no_permission(self):
        return redirect('cedolini/cedolini')

        
class Stipendi(LoginRequiredMixin, PermissionRequiredMixin,View):
    template_name= "cedolini/stipendi.html"
    permission_required = 'gestione.change_anadipendenti'
    
    def get(self, request, *args, **kwargs):
        none = None
        context = {'cedolino':none}

        return render(request, self.template_name, context)


class CreaCedolino(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model= ced
    form_class = CreaCedoliniForm
    template_name = 'cedolini/crea-cedolino.html'
    permission_required = 'gestione.change_anadipendenti'
    success_url= reverse_lazy('cedolini:stipendi')
    success_message = 'Cedolino creato.'
    error_message = "Errore nella creazione del cedolino."

    
    def post(self,request,*args,**kwargs):
        year=datetime.now().year
        mes=request.POST.get("mese")
        mesi = [1,2,3,4,5,6,7,8,9,10,11,12]
        errors = []
        # CREA TUTTI I CEDOLINI
        if request.method == "POST" and request.POST.get("tutti") == "":
            mes = request.POST.get("mese")
            dips = AnaDipendenti.objects.filter(stato="Attivo")
            for dip in dips:
                print("DIPE",dip)
                try:
                    if not(ced.objects.filter(dipendente=dip,mese=mes,anno=year)):
                        try:
                            ced.objects.create(dipendente=dip,mese=mes,anno=year,id_creazione=self.request.user.pk,timestamp_creazione=timezone.now())  
                        except Exception as err:
                            errors.append(err)
                    else: 
                        mese = convertMese(mes)
                        msg = f'I cedolini del mese di {mese} sono già stati creati, torna indietro e scegli un altro mese.'
                        messages.add_message(request, messages.INFO, msg)
                        return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
                except Exception as err:
                    errors.append(err)
                    mese = convertMese(mes)
                    msg= f'I cedolini del mese di {mese} sono stati creati per tutti i dipendenti.'
                    messages.add_message(request, messages.INFO, msg)
                    print("ERRORS",errors)
                    return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
        # CREA CEDOLINO SINGOLO
        elif request.method == "POST" and request.POST.get("singolo") == "":
            mes=request.POST.get("mese")
            dip = AnaDipendenti.objects.get(id_dip=request.POST.get("dipendente"))
            if not(ced.objects.filter(dipendente=dip.id_dip,anno=year,mese=mes).exists()):
                # OK
                try:
                    dipe=AnaDipendenti.objects.get(id_dip=dip.id_dip)
                    ced.objects.create(dipendente=dipe,mese=mes,anno=year,id_creazione=self.request.user.pk,timestamp_creazione=timezone.now())
                    mese = convertMese(mes)
                    msg= f'Cedolino per il mese di {mese} del dipendente {dip}, creato con successo.'
                    messages.add_message(request, messages.INFO, msg)
                    return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
                # ERRORE
                except:
                    mese = convertMese(mes)
                    msg= f'I cedolini del mese di {mese} sono già stati creati, torna indietro e scegli un altro mese.'
                    messages.add_message(request, messages.INFO, msg)
                    return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
            else:
                    mese = convertMese(mes)
                    msg= f'Il cedolino del mese di {mese} per il dip {dip}, è stato già creato.'
                    messages.add_message(request, messages.INFO, msg)
                    return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
        # CREA CEDOLINI PER TUTTO L'ANNO
        elif request.method=="POST" and request.POST.get("anno_intero") == "":
            dips = AnaDipendenti.objects.filter(stato="Attivo")
            print("DIPS",dips,dips.count())
            for el in mesi:
                for dip in dips:
                    print("DIP",dip)
                    try:
                        if not(ced.objects.filter(dipendente=dip,mese=el,anno=year).exists()):
                            try:
                                ced.objects.create(dipendente=dip,mese=el,anno=year,id_creazione=self.request.user.pk,timestamp_creazione=timezone.now())
                            except Exception as err:
                                errors.append(err)
                        else: 
                            mese = convertMese(mes)
                            msg= f'I cedolini dell`anno in corso sono stati già creati per tutti i dipendenti Attivi, utilizza il tool per la creazione per singolo dipendente.'
                            messages.add_message(request, messages.INFO, msg)
                            print("here_else",request.POST)
                            return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
                    except Exception as err:
                            errors.append(err)
            return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})
        # ELSE     
        else: 
            mese = convertMese(mes)
            msg= f'I cedolini del mese di {mese} sono già stati creati, torna indietro e scegli un altro mese.'
            messages.add_message(request, messages.INFO, msg)

            return render(request,"cedolini/crea-cedolino.html",{'form':self.form_class})


    def sample_view(request):
        current_user = request.user
        return current_user.id
    
    
    def form_valid(self, form):
        year = datetime.now().year
        form.instance.anno = int(year)
        form.instance.id_creazione=self.request.user.pk
        
        try: 
            temp = form.save()
            if form.is_valid():
                return super(CreaCedolino).form_valid(form)       
        except Exception as error:
            print(error)
        return redirect('cedolini:stipendi')
    