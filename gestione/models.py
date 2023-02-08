# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from decimal import *
from datetime import date, time, datetime, timedelta
from calendar import monthrange
from django.utils import timezone
import pytz
import math
from django.db import connection
from django.core.signals import setting_changed, request_finished, request_started
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils.timezone import localtime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import re
import random
from capi_area import updateCedolini


class AddIncForf(models.Model):
    id_inc_forf = models.BigAutoField(primary_key=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    inc_forf = models.FloatField(db_column='Inc_Forf', blank=True, null=True)  # Field name made lowercase.
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Inc_Forf'


class AddRimborsi(models.Model):
    id_rimborsi = models.BigAutoField(primary_key=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    rel_giorno = models.IntegerField(blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Rimborsi'


class AddTrasferte(models.Model):
    id_trasferte = models.BigAutoField(primary_key=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    rel_giorno = models.IntegerField(blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Trasferte'

class AnaDipendenti(models.Model):
    id_dip = models.AutoField(db_column='ID_Dip', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    id_stipendio = models.IntegerField(blank=True, null=True)
    dip_capo_area = models.IntegerField(db_column='Dip_Capo_Area', blank=True, null=True)  # Field name made lowercase.
    id_capo_area = models.ForeignKey('CapoArea', models.DO_NOTHING, db_column='ID_Capo_Area', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    cognome = models.CharField(db_column='Cognome', max_length=100)  # Field name made lowercase.
    sesso = models.ForeignKey('Sesso', models.DO_NOTHING, db_column='Sesso', blank=True, null=True)  # Field name made lowercase.
    codice_fiscale = models.CharField(db_column='Codice_Fiscale', max_length=17, blank=True, null=True)  # Field name made lowercase.
    luogo_nascita = models.CharField(db_column='Luogo_Nascita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia_nascita = models.CharField(db_column='Provincia_Nascita', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data_nascita = models.DateField(db_column='Data_Nascita', blank=True, null=True)  # Field name made lowercase.
    citta_domicilio = models.CharField(db_column='Citta_Domicilio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indirizzo_domicilio = models.CharField(db_column='Indirizzo_Domicilio', max_length=150, blank=True, null=True)  # Field name made lowercase.
    provincia_domicilio = models.CharField(db_column='Provincia_Domicilio', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cap_domicilio = models.CharField(db_column='Cap_Domicilio', max_length=6, blank=True, null=True)  # Field name made lowercase.
    citta_residenza = models.CharField(db_column='Citta_Residenza', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indirizzo_residenza = models.CharField(db_column='Indirizzo_Residenza', max_length=150, blank=True, null=True)  # Field name made lowercase.
    provincia_residenza = models.CharField(db_column='Provincia_Residenza', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cap_residenza = models.CharField(db_column='Cap_Residenza', max_length=6, blank=True, null=True)  # Field name made lowercase.
    asl = models.CharField(db_column='ASL', max_length=75, blank=True, null=True)  # Field name made lowercase.
    cellulare = models.CharField(db_column='Cellulare', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cell_alternativo = models.CharField(db_column='Cell_Alternativo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email_pers = models.CharField(db_column='Email_Pers', max_length=75, blank=True, null=True)  # Field name made lowercase.
    email_lav = models.CharField(db_column='Email_Lav', max_length=75, blank=True, null=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=27, blank=True, null=True)  # Field name made lowercase.
    p_iva = models.CharField(db_column='P_Iva', max_length=11, blank=True, null=True)  # Field name made lowercase.
    societa = models.ForeignKey('Societa', models.DO_NOTHING, db_column='Societa', blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey('Area', models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    istruzione = models.ForeignKey('Istruzione', models.DO_NOTHING, db_column='Istruzione', blank=True, null=True)  # Field name made lowercase.
    tipo_contratto = models.ForeignKey('TipoContratto', models.DO_NOTHING, db_column='Tipo_Contratto', blank=True, null=True)  # Field name made lowercase.
    mansione = models.ForeignKey('Mansione', models.DO_NOTHING, db_column='Mansione', blank=True, null=True)  # Field name made lowercase.
    data_inizio_rap = models.DateField(db_column='Data_inizio_rap', blank=True, null=True)  # Field name made lowercase.
    data_fine_rap = models.DateField(db_column='Data_fine_rap', blank=True, null=True)  # Field name made lowercase.
    stato = models.CharField(db_column='Stato', max_length=7, blank=True, null=True)  # Field name made lowercase.
    data_creazione = models.DateTimeField(db_column='Data_creazione',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ana_Dipendenti'
        ordering = ['cognome']
    
    @property
    def nominativo(self):
        return f'{(self.cognome).title()} {(self.nome).title()}'
    
    def __str__(self):
        return f"{self.cognome} {self.nome}"


@receiver(pre_save, sender=AnaDipendenti)
def upper_fields(sender, instance, *args, **kwargs):
    instance.nome = (instance.nome.upper())
    instance.cognome = (instance.cognome.upper())
    if instance.codice_fiscale:
        instance.codice_fiscale = (instance.codice_fiscale.upper())
    if instance.provincia_nascita:
        instance.provincia_nascita = (instance.provincia_nascita.upper())
    if instance.provincia_domicilio:
        instance.provincia_domicilio = (instance.provincia_domicilio.upper())
    if instance.provincia_residenza:
        instance.provincia_residenza = (instance.provincia_residenza.upper())
    if instance.iban:
        instance.iban = (instance.iban.upper()).replace(" ","")
    if instance.email_pers:
        instance.email_pers = (instance.email_pers.lower()).replace(" ","")
    if instance.email_lav:
        instance.email_lav = (instance.email_lav.lower()).replace(" ","")

class AnadipControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.IntegerField(blank=True, null=True)
    row = models.BigIntegerField(blank=True, null=True)
    table = models.CharField(max_length=150, blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    full_row = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anadip_control'

@receiver(post_save, sender=AnaDipendenti)
def anadipcontrol_post_save_receiver(sender, instance, created, *args, **kwargs):
    full_row_instance = ""

    if instance.id_dip:
        full_row_instance += "id_dip:" + str(instance.id_dip) + ","
    if instance.user:
        full_row_instance += "user:" + str(instance.user) + ","
    if instance.dip_capo_area:
        full_row_instance += "dip_capo_area:" + str(instance.dip_capo_area) + ","
    if instance.id_stipendio:
        full_row_instance += "id_stipendio:" + str(instance.id_stipendio) + ","
    if instance.nome:
        full_row_instance += "nome:" + str(instance.nome) + ","
    if instance.cognome:
        full_row_instance += "cognome:" + str(instance.cognome) + ","
    if instance.codice_fiscale:
        full_row_instance += "codice_fiscale:" + str(instance.codice_fiscale) + ","
    if instance.luogo_nascita:
        full_row_instance += "luogo_nascita:" + str(instance.luogo_nascita) + ","
    if instance.provincia_nascita:
        full_row_instance += "provincia_nascita:" + str(instance.provincia_nascita) + ","
    if instance.data_nascita:
        full_row_instance += "data_nascita:" + str(instance.data_nascita) + ","
    if instance.citta_domicilio:
        full_row_instance += "citta_domicilio:" + str(instance.citta_domicilio) + ","
    if instance.indirizzo_domicilio:
        full_row_instance += "indirizzo_domicilio:" + str(instance.indirizzo_domicilio) + ","
    if instance.provincia_domicilio:
        full_row_instance += "provincia_domicilio:" + str(instance.provincia_domicilio) + ","
    if instance.cap_domicilio:
        full_row_instance += "cap_domicilio:" + str(instance.cap_domicilio) + ","
    if instance.citta_residenza:
        full_row_instance += "citta_residenza:" + str(instance.citta_residenza) + ","
    if instance.indirizzo_residenza:
        full_row_instance += "indirizzo_residenza:" + str(instance.indirizzo_residenza) + ","
    if instance.provincia_residenza:
        full_row_instance += "provincia_residenza:" + str(instance.provincia_residenza) + ","
    if instance.cap_residenza:
        full_row_instance += "cap_residenza:" + str(instance.cap_residenza) + ","
    if instance.cellulare:
        full_row_instance += "cellulare:" + str(instance.cellulare) + ","
    if instance.cell_alternativo:
        full_row_instance += "cell_alternativo:" + str(instance.cell_alternativo) + ","
    if instance.email_pers:
        full_row_instance += "email_pers:" + str(instance.email_pers) + ","
    if instance.email_lav:
        full_row_instance += "email_lav:" + str(instance.email_lav) + ","
    if instance.iban:
        full_row_instance += "iban:" + str(instance.iban) + ","
    if instance.societa:
        full_row_instance += "societa:" + str(instance.societa) + ","
    if instance.sede:
        full_row_instance += "sede:" + str(instance.sede) + ","
    if instance.area:
        full_row_instance += "area:" + str(instance.area) + ","
    if instance.istruzione:
        full_row_instance += "istruzione:" + str(instance.istruzione) + ","
    if instance.mansione:
        full_row_instance += "mansione:" + str(instance.mansione) + ","
    if instance.data_inizio_rap:
        full_row_instance += "data_inizio_rap:" + str(instance.data_inizio_rap) + ","
    if instance.data_fine_rap:
        full_row_instance += "data_fine_rap:" + str(instance.data_fine_rap) + ","
    if instance.stato:
        full_row_instance += "stato:" + str(instance.stato) + ","
    if instance.data_creazione:
        full_row_instance += "data_creazione:" + str(instance.data_creazione) + ","
    if instance.note:
        full_row_instance += "note:" + str(instance.note)

    if created:
        new_row = AnadipControl.objects.create(row = instance.pk, table = sender, action =  "created", timestamp = timezone.now(), full_row  = full_row_instance)
    else: 
        new_row = AnadipControl.objects.create(row = instance.pk, table = sender, action =  "updated", timestamp = timezone.now(), full_row  = full_row_instance)

@receiver(pre_delete, sender=AnaDipendenti)
def anadipcontrol_post_save_receiver(sender, instance, *args, **kwargs):
    full_row_instance = ""

    if instance.id_dip:
        full_row_instance += "id_dip:" + str(instance.id_dip) + ","
    if instance.user:
        full_row_instance += "user:" + str(instance.user) + ","
    if instance.dip_capo_area:
        full_row_instance += "dip_capo_area:" + str(instance.dip_capo_area) + ","
    if instance.id_capo_area:
        full_row_instance += "id_capo_area:" + str(instance.id_capo_area) + ","
    if instance.id_stipendio:
        full_row_instance += "id_stipendio:" + str(instance.id_stipendio) + ","
    if instance.nome:
        full_row_instance += "nome:" + str(instance.nome) + ","
    if instance.cognome:
        full_row_instance += "cognome:" + str(instance.cognome) + ","
    if instance.codice_fiscale:
        full_row_instance += "codice_fiscale:" + str(instance.codice_fiscale) + ","
    if instance.luogo_nascita:
        full_row_instance += "luogo_nascita:" + str(instance.luogo_nascita) + ","
    if instance.provincia_nascita:
        full_row_instance += "provincia_nascita:" + str(instance.provincia_nascita) + ","
    if instance.data_nascita:
        full_row_instance += "data_nascita:" + str(instance.data_nascita) + ","
    if instance.citta_domicilio:
        full_row_instance += "citta_domicilio:" + str(instance.citta_domicilio) + ","
    if instance.indirizzo_domicilio:
        full_row_instance += "indirizzo_domicilio:" + str(instance.indirizzo_domicilio) + ","
    if instance.provincia_domicilio:
        full_row_instance += "provincia_domicilio:" + str(instance.provincia_domicilio) + ","
    if instance.cap_domicilio:
        full_row_instance += "cap_domicilio:" + str(instance.cap_domicilio) + ","
    if instance.citta_residenza:
        full_row_instance += "citta_residenza:" + str(instance.citta_residenza) + ","
    if instance.indirizzo_residenza:
        full_row_instance += "indirizzo_residenza:" + str(instance.indirizzo_residenza) + ","
    if instance.provincia_residenza:
        full_row_instance += "provincia_residenza:" + str(instance.provincia_residenza) + ","
    if instance.cap_residenza:
        full_row_instance += "cap_residenza:" + str(instance.cap_residenza) + ","
    if instance.cellulare:
        full_row_instance += "cellulare:" + str(instance.cellulare) + ","
    if instance.cell_alternativo:
        full_row_instance += "cell_alternativo:" + str(instance.cell_alternativo) + ","
    if instance.email_pers:
        full_row_instance += "email_pers:" + str(instance.email_pers) + ","
    if instance.email_lav:
        full_row_instance += "email_lav:" + str(instance.email_lav) + ","
    if instance.iban:
        full_row_instance += "iban:" + str(instance.iban) + ","
    if instance.societa:
        full_row_instance += "societa:" + str(instance.societa) + ","
    if instance.sede:
        full_row_instance += "sede:" + str(instance.sede) + ","
    if instance.area:
        full_row_instance += "area:" + str(instance.area) + ","
    if instance.istruzione:
        full_row_instance += "istruzione:" + str(instance.istruzione) + ","
    if instance.mansione:
        full_row_instance += "mansione:" + str(instance.mansione) + ","
    if instance.data_inizio_rap:
        full_row_instance += "data_inizio_rap:" + str(instance.data_inizio_rap) + ","
    if instance.data_fine_rap:
        full_row_instance += "data_fine_rap:" + str(instance.data_fine_rap) + ","
    if instance.stato:
        full_row_instance += "stato:" + str(instance.stato) + ","
    if instance.data_creazione:
        full_row_instance += "data_creazione:" + str(instance.data_creazione) + ","
    if instance.note:
        full_row_instance += "note:" + str(instance.note)
        
    new_row = AnadipControl.objects.create(row = instance.pk, table = sender, action =  "deleted", timestamp = timezone.now(), full_row  = full_row_instance)


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nome_area = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'
        ordering = ["nome_area"]

    def __str__(self):
        return self.nome_area
    
@receiver(pre_save, sender=Area)
def area_post_save_receiver(sender, instance, *args, **kwargs):
    instance.nome_area = (instance.nome_area.upper())
    
class BancaOrari(models.Model):
    id_banca_dati = models.BigAutoField(db_column='Id_banca_dati', primary_key=True)  # Field name made lowercase.
    id_dip = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='Id_dip', blank=True, null=True)  # Field name made lowercase.
    id_ingresso = models.ForeignKey('Ingressidip', models.DO_NOTHING, db_column='Id_Ingresso', blank=True, null=True)  # Field name made lowercase.
    tempo = models.TimeField(db_column='Tempo', blank=True, null=True)  # Field name made lowercase.
    giorno = models.DateField(db_column='Giorno', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Banca_Orari'

class CapoArea(models.Model):
    id_capo = models.AutoField(db_column='ID_Capo', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dipendente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Capo_Area'
    
    def __str__(self):
        return self.id_dipendente


class Cedolini(models.Model):
    id_cedolino = models.BigAutoField(primary_key=True)
    dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='dipendente', blank=True, null=True)
    add_rimborsi = models.ForeignKey(AddRimborsi, models.DO_NOTHING, db_column='add_rimborsi', blank=True, null=True)
    add_trasferte = models.ForeignKey(AddTrasferte, models.DO_NOTHING, db_column='add_trasferte', blank=True, null=True)
    add_inc_forf = models.ForeignKey(AddIncForf, models.DO_NOTHING, db_column='add_inc_forf', blank=True, null=True)
    mese = models.IntegerField(blank=True, null=True)
    anno = models.IntegerField(blank=True, null=True)
    ord_01 = models.FloatField(blank=True, null=True)
    ord_02 = models.FloatField(blank=True, null=True)
    ord_03 = models.FloatField(blank=True, null=True)
    ord_04 = models.FloatField(blank=True, null=True)
    ord_05 = models.FloatField(blank=True, null=True)
    ord_06 = models.FloatField(blank=True, null=True)
    ord_07 = models.FloatField(blank=True, null=True)
    ord_08 = models.FloatField(blank=True, null=True)
    ord_09 = models.FloatField(blank=True, null=True)
    ord_10 = models.FloatField(blank=True, null=True)
    ord_11 = models.FloatField(blank=True, null=True)
    ord_12 = models.FloatField(blank=True, null=True)
    ord_13 = models.FloatField(blank=True, null=True)
    ord_14 = models.FloatField(blank=True, null=True)
    ord_15 = models.FloatField(blank=True, null=True)
    ord_16 = models.FloatField(blank=True, null=True)
    ord_17 = models.FloatField(blank=True, null=True)
    ord_18 = models.FloatField(blank=True, null=True)
    ord_19 = models.FloatField(blank=True, null=True)
    ord_20 = models.FloatField(blank=True, null=True)
    ord_21 = models.FloatField(blank=True, null=True)
    ord_22 = models.FloatField(blank=True, null=True)
    ord_23 = models.FloatField(blank=True, null=True)
    ord_24 = models.FloatField(blank=True, null=True)
    ord_25 = models.FloatField(blank=True, null=True)
    ord_26 = models.FloatField(blank=True, null=True)
    ord_27 = models.FloatField(blank=True, null=True)
    ord_28 = models.FloatField(blank=True, null=True)
    ord_29 = models.FloatField(blank=True, null=True)
    ord_30 = models.FloatField(blank=True, null=True)
    ord_31 = models.FloatField(blank=True, null=True)
    fer_01 = models.FloatField(blank=True, null=True)
    fer_02 = models.FloatField(blank=True, null=True)
    fer_03 = models.FloatField(blank=True, null=True)
    fer_04 = models.FloatField(blank=True, null=True)
    fer_05 = models.FloatField(blank=True, null=True)
    fer_06 = models.FloatField(blank=True, null=True)
    fer_07 = models.FloatField(blank=True, null=True)
    fer_08 = models.FloatField(blank=True, null=True)
    fer_09 = models.FloatField(blank=True, null=True)
    fer_10 = models.FloatField(blank=True, null=True)
    fer_11 = models.FloatField(blank=True, null=True)
    fer_12 = models.FloatField(blank=True, null=True)
    fer_13 = models.FloatField(blank=True, null=True)
    fer_14 = models.FloatField(blank=True, null=True)
    fer_15 = models.FloatField(blank=True, null=True)
    fer_16 = models.FloatField(blank=True, null=True)
    fer_17 = models.FloatField(blank=True, null=True)
    fer_18 = models.FloatField(blank=True, null=True)
    fer_19 = models.FloatField(blank=True, null=True)
    fer_20 = models.FloatField(blank=True, null=True)
    fer_21 = models.FloatField(blank=True, null=True)
    fer_22 = models.FloatField(blank=True, null=True)
    fer_23 = models.FloatField(blank=True, null=True)
    fer_24 = models.FloatField(blank=True, null=True)
    fer_25 = models.FloatField(blank=True, null=True)
    fer_26 = models.FloatField(blank=True, null=True)
    fer_27 = models.FloatField(blank=True, null=True)
    fer_28 = models.FloatField(blank=True, null=True)
    fer_29 = models.FloatField(blank=True, null=True)
    fer_30 = models.FloatField(blank=True, null=True)
    fer_31 = models.FloatField(blank=True, null=True)
    mal_01 = models.FloatField(blank=True, null=True)
    mal_02 = models.FloatField(blank=True, null=True)
    mal_03 = models.FloatField(blank=True, null=True)
    mal_04 = models.FloatField(blank=True, null=True)
    mal_05 = models.FloatField(blank=True, null=True)
    mal_06 = models.FloatField(blank=True, null=True)
    mal_07 = models.FloatField(blank=True, null=True)
    mal_08 = models.FloatField(blank=True, null=True)
    mal_09 = models.FloatField(blank=True, null=True)
    mal_10 = models.FloatField(blank=True, null=True)
    mal_11 = models.FloatField(blank=True, null=True)
    mal_12 = models.FloatField(blank=True, null=True)
    mal_13 = models.FloatField(blank=True, null=True)
    mal_14 = models.FloatField(blank=True, null=True)
    mal_15 = models.FloatField(blank=True, null=True)
    mal_16 = models.FloatField(blank=True, null=True)
    mal_17 = models.FloatField(blank=True, null=True)
    mal_18 = models.FloatField(blank=True, null=True)
    mal_19 = models.FloatField(blank=True, null=True)
    mal_20 = models.FloatField(blank=True, null=True)
    mal_21 = models.FloatField(blank=True, null=True)
    mal_22 = models.FloatField(blank=True, null=True)
    mal_23 = models.FloatField(blank=True, null=True)
    mal_24 = models.FloatField(blank=True, null=True)
    mal_25 = models.FloatField(blank=True, null=True)
    mal_26 = models.FloatField(blank=True, null=True)
    mal_27 = models.FloatField(blank=True, null=True)
    mal_28 = models.FloatField(blank=True, null=True)
    mal_29 = models.FloatField(blank=True, null=True)
    mal_30 = models.FloatField(blank=True, null=True)
    mal_31 = models.FloatField(blank=True, null=True)
    perm_01 = models.FloatField(blank=True, null=True)
    perm_02 = models.FloatField(blank=True, null=True)
    perm_03 = models.FloatField(blank=True, null=True)
    perm_04 = models.FloatField(blank=True, null=True)
    perm_05 = models.FloatField(blank=True, null=True)
    perm_06 = models.FloatField(blank=True, null=True)
    perm_07 = models.FloatField(blank=True, null=True)
    perm_08 = models.FloatField(blank=True, null=True)
    perm_09 = models.FloatField(blank=True, null=True)
    perm_10 = models.FloatField(blank=True, null=True)
    perm_11 = models.FloatField(blank=True, null=True)
    perm_12 = models.FloatField(blank=True, null=True)
    perm_13 = models.FloatField(blank=True, null=True)
    perm_14 = models.FloatField(blank=True, null=True)
    perm_15 = models.FloatField(blank=True, null=True)
    perm_16 = models.FloatField(blank=True, null=True)
    perm_17 = models.FloatField(blank=True, null=True)
    perm_18 = models.FloatField(blank=True, null=True)
    perm_19 = models.FloatField(blank=True, null=True)
    perm_20 = models.FloatField(blank=True, null=True)
    perm_21 = models.FloatField(blank=True, null=True)
    perm_22 = models.FloatField(blank=True, null=True)
    perm_23 = models.FloatField(blank=True, null=True)
    perm_24 = models.FloatField(blank=True, null=True)
    perm_25 = models.FloatField(blank=True, null=True)
    perm_26 = models.FloatField(blank=True, null=True)
    perm_27 = models.FloatField(blank=True, null=True)
    perm_28 = models.FloatField(blank=True, null=True)
    perm_29 = models.FloatField(blank=True, null=True)
    perm_30 = models.FloatField(blank=True, null=True)
    perm_31 = models.FloatField(blank=True, null=True)
    stra_01 = models.FloatField(blank=True, null=True)
    stra_02 = models.FloatField(blank=True, null=True)
    stra_03 = models.FloatField(blank=True, null=True)
    stra_04 = models.FloatField(blank=True, null=True)
    stra_05 = models.FloatField(blank=True, null=True)
    stra_06 = models.FloatField(blank=True, null=True)
    stra_07 = models.FloatField(blank=True, null=True)
    stra_08 = models.FloatField(blank=True, null=True)
    stra_09 = models.FloatField(blank=True, null=True)
    stra_10 = models.FloatField(blank=True, null=True)
    stra_11 = models.FloatField(blank=True, null=True)
    stra_12 = models.FloatField(blank=True, null=True)
    stra_13 = models.FloatField(blank=True, null=True)
    stra_14 = models.FloatField(blank=True, null=True)
    stra_15 = models.FloatField(blank=True, null=True)
    stra_16 = models.FloatField(blank=True, null=True)
    stra_17 = models.FloatField(blank=True, null=True)
    stra_30 = models.FloatField(blank=True, null=True)
    stra_29 = models.FloatField(blank=True, null=True)
    stra_18 = models.FloatField(blank=True, null=True)
    stra_19 = models.FloatField(blank=True, null=True)
    stra_20 = models.FloatField(blank=True, null=True)
    stra_21 = models.FloatField(blank=True, null=True)
    stra_22 = models.FloatField(blank=True, null=True)
    stra_23 = models.FloatField(blank=True, null=True)
    stra_24 = models.FloatField(blank=True, null=True)
    stra_25 = models.FloatField(blank=True, null=True)
    stra_26 = models.FloatField(blank=True, null=True)
    stra_27 = models.FloatField(blank=True, null=True)
    stra_28 = models.FloatField(blank=True, null=True)
    stra_31 = models.FloatField(blank=True, null=True)
    strafes_01 = models.FloatField(blank=True, null=True)
    strafes_02 = models.FloatField(blank=True, null=True)
    strafes_03 = models.FloatField(blank=True, null=True)
    strafes_04 = models.FloatField(blank=True, null=True)
    strafes_05 = models.FloatField(blank=True, null=True)
    strafes_06 = models.FloatField(blank=True, null=True)
    strafes_07 = models.FloatField(blank=True, null=True)
    strafes_08 = models.FloatField(blank=True, null=True)
    strafes_09 = models.FloatField(blank=True, null=True)
    strafes_10 = models.FloatField(blank=True, null=True)
    strafes_11 = models.FloatField(blank=True, null=True)
    strafes_12 = models.FloatField(blank=True, null=True)
    strafes_13 = models.FloatField(blank=True, null=True)
    strafes_14 = models.FloatField(blank=True, null=True)
    strafes_15 = models.FloatField(blank=True, null=True)
    strafes_16 = models.FloatField(blank=True, null=True)
    strafes_17 = models.FloatField(blank=True, null=True)
    strafes_18 = models.FloatField(blank=True, null=True)
    strafes_19 = models.FloatField(blank=True, null=True)
    strafes_20 = models.FloatField(blank=True, null=True)
    strafes_21 = models.FloatField(blank=True, null=True)
    strafes_22 = models.FloatField(blank=True, null=True)
    strafes_23 = models.FloatField(blank=True, null=True)
    strafes_24 = models.FloatField(blank=True, null=True)
    strafes_25 = models.FloatField(blank=True, null=True)
    strafes_26 = models.FloatField(blank=True, null=True)
    strafes_27 = models.FloatField(blank=True, null=True)
    strafes_28 = models.FloatField(blank=True, null=True)
    strafes_29 = models.FloatField(blank=True, null=True)
    strafes_30 = models.FloatField(blank=True, null=True)
    strafes_31 = models.FloatField(blank=True, null=True)
    tras_01 = models.CharField(max_length=3, blank=True, null=True)
    tras_02 = models.CharField(max_length=3, blank=True, null=True)
    tras_03 = models.CharField(max_length=3, blank=True, null=True)
    tras_04 = models.CharField(max_length=3, blank=True, null=True)
    tras_05 = models.CharField(max_length=3, blank=True, null=True)
    tras_06 = models.CharField(max_length=3, blank=True, null=True)
    tras_07 = models.CharField(max_length=3, blank=True, null=True)
    tras_08 = models.CharField(max_length=3, blank=True, null=True)
    tras_09 = models.CharField(max_length=3, blank=True, null=True)
    tras_10 = models.CharField(max_length=3, blank=True, null=True)
    tras_11 = models.CharField(max_length=3, blank=True, null=True)
    tras_12 = models.CharField(max_length=3, blank=True, null=True)
    tras_13 = models.CharField(max_length=3, blank=True, null=True)
    tras_14 = models.CharField(max_length=3, blank=True, null=True)
    tras_15 = models.CharField(max_length=3, blank=True, null=True)
    tras_16 = models.CharField(max_length=3, blank=True, null=True)
    tras_17 = models.CharField(max_length=3, blank=True, null=True)
    tras_18 = models.CharField(max_length=3, blank=True, null=True)
    tras_19 = models.CharField(max_length=3, blank=True, null=True)
    tras_20 = models.CharField(max_length=3, blank=True, null=True)
    tras_21 = models.CharField(max_length=3, blank=True, null=True)
    tras_22 = models.CharField(max_length=3, blank=True, null=True)
    tras_23 = models.CharField(max_length=3, blank=True, null=True)
    tras_24 = models.CharField(max_length=3, blank=True, null=True)
    tras_25 = models.CharField(max_length=3, blank=True, null=True)
    tras_26 = models.CharField(max_length=3, blank=True, null=True)
    tras_27 = models.CharField(max_length=3, blank=True, null=True)
    tras_28 = models.CharField(max_length=3, blank=True, null=True)
    tras_29 = models.CharField(max_length=3, blank=True, null=True)
    tras_30 = models.CharField(max_length=3, blank=True, null=True)
    tras_31 = models.CharField(max_length=3, blank=True, null=True)
    rimborsi = models.CharField(max_length=255, blank=True, null=True)
    inc_forf = models.CharField(max_length=255, blank=True, null=True)
    bonuses = models.CharField(max_length=255, blank=True, null=True)
    documenti = models.TextField(blank=True, null=True)
    id_ultima_modifica = models.IntegerField(blank=True, null=True)
    timestamp_modifica = models.DateTimeField(blank=True, null=True)
    id_creazione = models.IntegerField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cedolini'
        
    def __str__(self):
        return f'LUL di {self.dipendente} mese {self.mese}, anno {self.anno}'


@receiver(post_save, sender=AnaDipendenti)
def cedolini_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        yeary = datetime.now().date().year
        monthy = datetime.now().date().month
        dataStart = datetime.now().date()
        monthStart=dataStart.month
        for el in range(monthy, 13):
            try:
                dipen = AnaDipendenti.objects.get(id_dip=instance.id_dip)
                if not(Cedolini.objects.filter(dipendente=dipen,mese=el,anno=yeary)):
                    Cedolini.objects.create(dipendente=dipen,mese=el,anno=yeary,timestamp_creazione=timezone.now())
                else:
                    print("MAGARI NO")
                    pass
            except Exception as err:
                print(err)


class Contratti(models.Model):
    id_contratto = models.AutoField(db_column='ID_Contratto', primary_key=True)  # Field name made lowercase.
    id_dip = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dip', blank=True, null=True)  # Field name made lowercase.
    id_societa = models.ForeignKey('ListaSocieta', models.DO_NOTHING, db_column='ID_Societa', blank=True, null=True)  # Field name made lowercase.
    tipologia = models.ForeignKey('TipoContratto', models.DO_NOTHING, db_column='Tipologia', blank=True, null=True)  # Field name made lowercase.
    codicecontratto = models.CharField(db_column='CodiceContratto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percentuale = models.ForeignKey('PercentualiContratto', models.DO_NOTHING, db_column='Percentuale', blank=True, null=True)  # Field name made lowercase.
    datainizio = models.DateField(db_column='DataInizio', blank=True, null=True)  # Field name made lowercase.
    datafine = models.DateField(db_column='DataFine', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Contratti'
        ordering = ["codicecontratto"]


class Dirigenti(models.Model):
    id_dir = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dirigenti'
        
    def __str__(self):
        return self.nomecompleto


class Istruzione(models.Model):
    id_istruzione = models.AutoField(primary_key=True)
    tipo_istruzione = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Istruzione'
        
    def __str__(self):
        return self.tipo_istruzione
    
@receiver(pre_save, sender=Istruzione)
def tipo_istruzione_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.tipo_istruzione = (instance.tipo_istruzione.upper())

class Ingressidip(models.Model):
    id_ingresso = models.AutoField(primary_key=True)
    id_dip_ing = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dip_ing', blank=True, null=True)
    id_permesso = models.ForeignKey('Richieste', models.DO_NOTHING, db_column='id_permesso', blank=True, null=True)
    tipo_permesso = models.ForeignKey('Permessi', models.DO_NOTHING, db_column='tipo_permesso', blank=True, null=True)
    in_permesso = models.IntegerField(blank=True, null=True)
    nominativo = models.CharField(max_length=150, blank=True, null=True)
    registrato_da_user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='registrato_da_user', blank=True, null=True)
    giorno = models.DateField(blank=True, null=True)
    entrata = models.TimeField(blank=True, null=True)
    uscita = models.TimeField(blank=True, null=True)
    seconda_entrata = models.TimeField(blank=True, null=True)
    seconda_uscita = models.TimeField(blank=True, null=True)
    checked_in = models.SmallIntegerField(default=0,blank=True, null=True)
    checked_out = models.SmallIntegerField(default=0,blank=True, null=True)
    timestamp_scan_entrata = models.DateTimeField(blank=True, null=True)
    timestamp_scan_uscita = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'IngressiDip'


    @property
    def ritardo(self):
        orariolav = datetime.strptime("09:05:00", '%H:%M:%S').time()
        orariolavpulizie = datetime.strptime("07:05:00", '%H:%M:%S').time()
        if self.entrata and self.entrata > orariolav  and self.id_dip_ing.area != 21:
            ritardo = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), orariolav)
            return ritardo
        if self.entrata and self.entrata > orariolavpulizie:
            ritardo = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), orariolavpulizie)
            return ritardo
    
    def sum_ritardo(self):
        queryset = Ingressidip.objects.all()
        return sum([self.ritardo for self.ritardo in queryset()])
    
    @property
    def anticipo(self):
        orariolav = datetime.strptime("07:00:00", '%H:%M:%S').time()
        orariolavpulizie = datetime.strptime("07:00:00", '%H:%M:%S').time()

        if self.entrata and self.entrata < orariolav and self.id_dip_ing.area != 21:
            anticipo = datetime.combine(date.today(), orariolav) - datetime.combine(date.today(), self.entrata)
            return anticipo
        elif self.entrata and self.entrata < orariolavpulizie:
            anticipo = datetime.combine(date.today(), orariolavpulizie) - datetime.combine(date.today(), self.entrata)
            return anticipo

    
    @property
    def straordinario(self):
        orariolav = datetime.strptime("09:00:00", '%H:%M:%S').time()
        orariolavfine = datetime.strptime("18:00:00", '%H:%M:%S').time()
        straordinario = 0
        if self.entrata and self.entrata < orariolav and self.seconda_uscita and self.seconda_uscita > orariolavfine:
            straE = datetime.combine(date.today(), orariolav) - datetime.combine(date.today(), self.entrata)
            if straE.total_seconds() > 1800:
                straordinario = straE
                straU = datetime.combine(date.today(), self.seconda_uscita) - datetime.combine(date.today(), orariolavfine)
                if straU.total_seconds() > 1800:
                    straordinario = straordinario + timedelta(seconds=straE.total_seconds())
                    if self.seconda_entrata and self.seconda_uscita:
                        checkEntrata = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), self.uscita)
                        checkUscita = datetime.combine(date.today(), self.seconda_entrata) - datetime.combine(date.today(), self.seconda_uscita)
                        timeLavoro = checkEntrata.total_seconds() + checkUscita.total_seconds()
                        if timeLavoro > 30600:
                            checkEntrata + timedelta(seconds=checkUscita.total_seconds())
                            return checkEntrata
                return straordinario
        if self.entrata and self.entrata < orariolav and self.uscita and self.uscita > orariolavfine:
            straE = datetime.combine(date.today(), orariolav) - datetime.combine(date.today(), self.entrata)
            if straE.total_seconds() > 1800:
                straordinario = straE
                straU = datetime.combine(date.today(), self.uscita) - datetime.combine(date.today(), orariolavfine)
                if straU.total_seconds() > 1800:
                    straordinario = straordinario + timedelta(seconds=straE.total_seconds())
            return straordinario
        elif self.entrata and self.entrata < orariolav:
            straE = datetime.combine(date.today(), orariolav) - datetime.combine(date.today(), self.entrata)
            if straE.total_seconds() > 1800:
                straordinario = straE
            return straordinario
    def __str__(self):
        def newLineNom(nom):
            
            for char in nom:
                nome = nom.replace(" ", "\n")
            return nome
        return newLineNom(self.nominativo)
    
    def save(self, *args, **kwargs):
        if self.entrata:
            self.checked_in = True
        elif self.entrata == None:
            self.checked_in = 0
        if self.uscita:
            self.checked_out = True
        elif self.uscita == None:
            self.checked_out = 0
        super(Ingressidip, self).save(*args, **kwargs)

@receiver(post_save, sender=AnaDipendenti)
def anadipcontrol_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        dataStart = datetime.now().date()
        yearStart=dataStart.year
        monthStart=dataStart.month
        dayStart=dataStart.day
        dipen=AnaDipendenti.objects.get(id_dip=instance.pk)
        def all_dates_in_year(yearStart):
            for month in range(monthStart, 13): # Month is always 1..12
                for day in range(1, monthrange(yearStart, month)[1] + 1):
                    if day < 10:
                        dayN = f'0{day}'
                        giorno = f'{yearStart}-{month}-{dayN}'
                        yield giorno
                    else:
                        giorno = f'{yearStart}-{month}-{day}'
                        yield giorno
        for giornata in all_dates_in_year(yearStart):
            name=f'{instance.nome.upper()} {instance.cognome.upper()}'
            ingresso=Ingressidip.objects.create(id_dip_ing=dipen,nominativo=name,in_permesso=False,giorno=giornata)

class ListaSocieta(models.Model):
    id_societa = models.OneToOneField('Societa', models.DO_NOTHING, db_column='ID_Societa', primary_key=True)  # Field name made lowercase.
    nomesocieta = models.CharField(db_column='NomeSocieta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comuneente = models.CharField(db_column='ComuneEnte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provente = models.CharField(db_column='ProvEnte', max_length=2, blank=True, null=True)  # Field name made lowercase.
    indirizzoente = models.CharField(db_column='IndirizzoEnte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partitaivaente = models.CharField(db_column='PartitaIvaEnte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codicefiscaleente = models.CharField(db_column='CodiceFiscaleEnte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    legalerapp = models.CharField(db_column='LegaleRapp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_capo = models.IntegerField(db_column='ID_Capo', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lista_Societa'
        ordering = ["nomesocieta"]

    
    def __str__(self):
        return self.nomesocieta


class Mansione(models.Model):
    id_mansione = models.AutoField(primary_key=True)
    tipo_mansione = models.CharField(unique=True, max_length=150, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mansione'
        ordering = ["tipo_mansione"]

    
    def __str__(self):
        return self.tipo_mansione
    
@receiver(pre_save, sender=Mansione)
def mansione_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.tipo_mansione = (instance.tipo_mansione.upper())

        
class Mese(models.Model):
    id_mese = models.AutoField(primary_key=True)
    mese = models.CharField(db_column='Mese', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mese'
    
    def __str__(self):
        return self.mese


class PercentualiContratto(models.Model):
    id_ore_contratto = models.AutoField(primary_key=True)
    dicitura_percentuale = models.CharField(max_length=50)
    perc_contratto = models.DecimalField(max_digits=20, decimal_places=2)
    ore_contratto = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Percentuali_contratto'
        ordering = ["perc_contratto"]

    def __str__(self):
        perc = f'{self.perc_contratto}%'
        if '.00' in perc:
            entuale = perc.split(".")
            return f'{entuale[0]}%'
        else: return perc

    def save(self, *args, **kwargs):
        if self.perc_contratto:
            perce = round(self.perc_contratto,2)
            ore = math.trunc((perce * 160)/100)
            self.ore_contratto = Decimal(ore)
        super(PercentualiContratto, self).save(*args, **kwargs)
        
class Permessi(models.Model):
    id_permesso = models.IntegerField(db_column='ID_Permesso', primary_key=True)  # Field name made lowercase.
    codicepermesso = models.CharField(db_column='CodicePermesso', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tipopermesso = models.CharField(db_column='TipoPermesso', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permessi'

    def __str__(self):
        return self.tipopermesso

class Responsabili(models.Model):
    id_res = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Responsabili'
        
    def __str__(self):
        return self.nomecompleto


class ResponsabiliSede(models.Model):
    id_res_sede = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Responsabili_sede'
        
    def __str__(self):
        return self.nomecompleto

class Richieste(models.Model):
    id_richiesta = models.AutoField(db_column='ID_richiesta', primary_key=True)  # Field name made lowercase.
    id_user = models.ForeignKey('AuthUser', on_delete=models.DO_NOTHING, db_column='ID_user', blank=True, null=True)  # Field name made lowercase.
    id_dipendente_richiesta = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_dipendente_richiesta', blank=True, null=True)  # Field name made lowercase.
    id_permessi_richieste = models.ForeignKey(Permessi, models.DO_NOTHING, related_name="permessi", db_column='ID_permessi_richieste', blank=True, null=True)  # Field name made lowercase.
    nominativo = models.CharField(max_length=250, blank=True, null=True)
    da_giorno_richiesta = models.DateField()
    da_ora_richiesta = models.TimeField(blank=True, null=True)
    a_giorno_richiesta = models.DateField()
    a_ora_richiesta = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_accettato = models.DateTimeField(blank=True, null=True)
    stato = models.SmallIntegerField(blank=True, null=True)
    urgente = models.BooleanField(default=0, blank=False, null=True)
    note_richiesta = models.TextField(db_column='Note_richiesta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Richieste'
        verbose_name = 'Richiesta'
        verbose_name_plural = 'Richieste'
    
    def __str__(self):
        strstamp = self.timestamp
        day = str(strstamp).split(" ")
        
        if self.stato == 0:
            return f"Richiesta di {AnaDipendenti.objects.get(user=self.id_user)} del {str(day[0])}. Respinta."
        elif self.stato == 1:
            return f" Richiesta di {AnaDipendenti.objects.get(user=self.id_user)} del {str(day[0])}. Accettata."
        else:
            return f" Richiesta di {AnaDipendenti.objects.get(user=self.id_user)} del {str(day[0])}, da revisionare."
    
    def get_absolute_url(self):
        return reverse("permessi:accetta-richieste", kwargs={"pk": self.pk})
    


class RichiesteAccettate(models.Model):
    id_richieste_accettate = models.AutoField(db_column='ID_richieste_accettate', primary_key=True)  # Field name made lowercase.
    id_richieste = models.ForeignKey(Richieste, models.DO_NOTHING, db_column='ID_richieste', blank=True, null=True)  # Field name made lowercase.
    id_capoarea_richieste = models.ForeignKey(CapoArea, models.DO_NOTHING, db_column='ID_capoArea_richieste', blank=True, null=True)  # Field name made lowercase.
    stato = models.SmallIntegerField(db_column='Stato', blank=True, null=True)  # Field name made lowercase.
    data_inizio_permesso = models.DateField(blank=True, null=True)
    data_fine_permesso = models.DateField(blank=True, null=True)
    ora_inizio_permesso = models.TimeField(blank=True, null=True)
    ora_fine_permesso = models.TimeField(blank=True, null=True)
    in_corso = models.BooleanField(default=0, blank=False, null=True)
    id_creazione = models.IntegerField(blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    id_update = models.IntegerField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Richieste_Accettate'
    
    def __unicode__(self):
        return self.id_richieste
    
@receiver(pre_save, sender=RichiesteAccettate)
def updateCedolini(sender, instance, *args, **kwargs):
    pass

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nome_sede = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sede'
        ordering = ["nome_sede"]
            
    def __str__(self):
        return self.nome_sede
    
@receiver(pre_save, sender=Sede)
def sede_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.nome_sede = (instance.nome_sede.upper())


class Sesso(models.Model):
    id_sesso = models.AutoField(primary_key=True)
    sesso = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sesso'
    
    def __str__(self):
        return self.sesso


class Societa(models.Model):
    id_societa = models.AutoField(primary_key=True)
    nome_societa = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Societa'
        ordering = ["nome_societa"]
                
    def __str__(self):
        return self.nome_societa

@receiver(pre_save, sender=Societa)
def societa_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.nome_societa = (instance.nome_societa.upper())


class TipoContratto(models.Model):
    id_contratto = models.AutoField(primary_key=True)
    nome_contratto = models.CharField(unique=True, max_length=100, blank=True, null=True)
    codice_contratto = models.CharField(max_length=2, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Tipo_Contratto'
        ordering = ["nome_contratto"]
        
    def __str__(self):
        return self.nome_contratto

@receiver(pre_save, sender=TipoContratto)
def sede_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.nome_contratto = (instance.nome_contratto.upper())

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    
    @receiver(post_save, sender=AnaDipendenti)
    def create_user(sender, instance, created, *args, **kwargs):

        def modifyUsername(username):  
            if username[3:4].isdigit():
                char = username[3:4]
                newchar = int(char) + 1
                username = username.replace(f"{str(char)}.", f"{str(newchar)}.")
                return username
            else: 
                username = username.replace(".", "2.")
            return username
        
        if created:
            usernameCheck=instance.nome[0:3].lower() + "." + instance.cognome.lower()
            item = AuthUser.objects.filter(username = usernameCheck)
            if item.exists():
                usernameCheck = modifyUsername(usernameCheck)
                try:
                    if instance.email_lav:
                        new_user = User.objects.create_user(username=usernameCheck,
                        password='Password1$',
                        first_name=instance.nome.title(),
                        last_name=instance.cognome.title(),
                        email=instance.email_lav,
                        is_staff=True)
                    elif instance.email_pers:
                        new_user = User.objects.create_user(username=usernameCheck,
                        password='Password1$',
                        first_name=instance.nome.title(),
                        last_name=instance.cognome.title(),
                        email=instance.email_pers,
                        is_staff=True)
                    id_new_user= new_user.id
                    latest_dip = AnaDipendenti.objects.all().values_list('id_dip', flat=True).order_by('-id_dip').first()
                    AnaDipendenti.objects.filter(id_dip = latest_dip).update(user=id_new_user)
                    userAccount = new_user.username
                    message = f'Di seguito le credenziali per accedere al tuo account aziendale:\n username: {userAccount}\n password: Password1$\n'
                    recipient = [new_user.email]
                    # send_mail(
                    #     'Benvenuto in PSB',
                    #     message,
                    #     settings.EMAIL_HOST_USER,
                    #     recipient
                    # )
                except: 
                    randNum = random.randint(0,999)
                    usernameCheck = instance.nome[0:3].lower() + str(randNum) +  "." + instance.cognome.lower()
                    modifyUsername(usernameCheck)
                    new_user = User.objects.create_user(username=usernameCheck,
                    password='Password1$',
                    first_name=instance.nome.title(),
                    last_name=instance.cognome.title(),
                    email=instance.email,
                    is_staff=True)
                    id_new_user= new_user.id
                    latest_dip = AnaDipendenti.objects.all().values_list('id_dip', flat=True).order_by('-id_dip').first()
                    AnaDipendenti.objects.filter(id_dip = latest_dip).update(user=id_new_user)
                    userAccount = new_user.username
                    message = f'Di seguito le credenziali per accedere al tuo account aziendale:\n username: {userAccount}\n password: Password1$\n'
                    recipient = [new_user.email]
                    # send_mail(
                    #     'Benvenuto in PSB',
                    #     message,
                    #     settings.EMAIL_HOST_USER,
                    #     [recipient]
                    # )
            else:
                if instance.email_lav:
                    new_user = User.objects.create_user(username=usernameCheck,
                    password='Password1$',
                    first_name=instance.nome.title(),
                    last_name=instance.cognome.title(),
                    email=instance.email_lav,
                    is_staff=True)
                elif instance.email_pers:
                    new_user = User.objects.create_user(username=usernameCheck,
                    password='Password1$',
                    first_name=instance.nome.title(),
                    last_name=instance.cognome.title(),
                    email=instance.email_pers,
                    is_staff=True)
                id_new_user= new_user.id
                latest_dip = AnaDipendenti.objects.all().values_list('id_dip', flat=True).order_by('-id_dip').first()
                AnaDipendenti.objects.filter(id_dip = latest_dip).update(user=id_new_user)
                userAccount = new_user.username
                message = f'Di seguito le credenziali per accedere al tuo account aziendale:\n username: {userAccount}\n password: Password1$\n'
                recipient = [new_user.email]
                # send_mail(
                #     'Benvenuto in PSB',
                #     message,
                #     settings.EMAIL_HOST_USER,
                #     recipient
                # )

        
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
