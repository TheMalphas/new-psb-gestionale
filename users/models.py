# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
import math
from decimal import *
from django.utils import timezone


class AddIncForf(models.Model):
    id_inc_forf = models.BigAutoField(primary_key=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    id_dip = models.ForeignKey('AnaDipendenti', models.DO_NOTHING, db_column='id_dip', blank=True, null=True)
    inc_forf = models.FloatField(db_column='Inc_Forf', blank=True, null=True)  # Field name made lowercase.
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Inc_Forf'


class AddRimborsi(models.Model):
    id_rimborsi = models.BigAutoField(primary_key=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    id_dip = models.ForeignKey('AnaDipendenti', models.DO_NOTHING, db_column='id_dip', blank=True, null=True)
    rel_giorno = models.DateField(blank=True, null=True)
    stato = models.IntegerField(default=0,blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Rimborsi'


class AddStraordinari(models.Model):
    id_straordinari = models.BigAutoField(primary_key=True)
    id_dip = models.ForeignKey('AnaDipendenti', models.DO_NOTHING, db_column='id_dip', blank=True, null=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    rel_giorno = models.DateField(blank=True, null=True)
    rel_time_start = models.TimeField(blank=True, null=True)
    rel_time_end = models.TimeField(blank=True, null=True)
    stato = models.IntegerField(default=0,blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Straordinari'


class AddTrasferte(models.Model):
    id_trasferte = models.BigAutoField(primary_key=True)
    id_dip = models.ForeignKey('AnaDipendenti', models.DO_NOTHING, db_column='id_dip', blank=True, null=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    rel_giorno = models.DateField(blank=True, null=True)
    stato = models.IntegerField(default=0,blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Trasferte'



class AnaDipendenti(models.Model):
    id_dip = models.AutoField(db_column='ID_Dip', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    id_stipendio = models.IntegerField(blank=True, null=True)
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
    iban = models.CharField(db_column='IBAN', max_length=34, blank=True, null=True)  # Field name made lowercase.
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
    data_creazione = models.DateTimeField(db_column='Data_creazione', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Ana_Dipendenti'

class AppoggioVerificaQr(models.Model):
    uuid_qr = models.CharField(primary_key=True, max_length=50)
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente')

    class Meta:
        managed = False
        db_table = 'appoggio_verifica_qr'
        unique_together = (('uuid_qr', 'id_dipendente'),)

class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nome_area = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'

    def __str__(self):
        return self.nome_area

class CapoArea(models.Model):
    id_capo = models.IntegerField(db_column='ID_Capo', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.CharField(db_column='Sede', max_length=16, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=29, blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dipendente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Capo_Area'


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
    tras2_01 = models.CharField(max_length=3, blank=True, null=True)
    tras2_02 = models.CharField(max_length=3, blank=True, null=True)
    tras2_03 = models.CharField(max_length=3, blank=True, null=True)
    tras2_04 = models.CharField(max_length=3, blank=True, null=True)
    tras2_05 = models.CharField(max_length=3, blank=True, null=True)
    tras2_06 = models.CharField(max_length=3, blank=True, null=True)
    tras2_07 = models.CharField(max_length=3, blank=True, null=True)
    tras2_08 = models.CharField(max_length=3, blank=True, null=True)
    tras2_09 = models.CharField(max_length=3, blank=True, null=True)
    tras2_10 = models.CharField(max_length=3, blank=True, null=True)
    tras2_11 = models.CharField(max_length=3, blank=True, null=True)
    tras2_12 = models.CharField(max_length=3, blank=True, null=True)
    tras2_13 = models.CharField(max_length=3, blank=True, null=True)
    tras2_14 = models.CharField(max_length=3, blank=True, null=True)
    tras2_15 = models.CharField(max_length=3, blank=True, null=True)
    tras2_16 = models.CharField(max_length=3, blank=True, null=True)
    tras2_17 = models.CharField(max_length=3, blank=True, null=True)
    tras2_18 = models.CharField(max_length=3, blank=True, null=True)
    tras2_19 = models.CharField(max_length=3, blank=True, null=True)
    tras2_20 = models.CharField(max_length=3, blank=True, null=True)
    tras2_21 = models.CharField(max_length=3, blank=True, null=True)
    tras2_22 = models.CharField(max_length=3, blank=True, null=True)
    tras2_23 = models.CharField(max_length=3, blank=True, null=True)
    tras2_24 = models.CharField(max_length=3, blank=True, null=True)
    tras2_25 = models.CharField(max_length=3, blank=True, null=True)
    tras2_26 = models.CharField(max_length=3, blank=True, null=True)
    tras2_27 = models.CharField(max_length=3, blank=True, null=True)
    tras2_28 = models.CharField(max_length=3, blank=True, null=True)
    tras2_29 = models.CharField(max_length=3, blank=True, null=True)
    tras2_30 = models.CharField(max_length=3, blank=True, null=True)
    tras2_31 = models.CharField(max_length=3, blank=True, null=True)
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



class Contratti(models.Model):
    id_contratto = models.AutoField(db_column='ID_Contratto', primary_key=True)  # Field name made lowercase.
    id_dip = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dip', blank=True, null=True)  # Field name made lowercase.
    id_societa = models.ForeignKey('ListaSocieta', models.DO_NOTHING, db_column='ID_Societa', blank=True, null=True)  # Field name made lowercase.
    tipologia = models.ForeignKey('TipoContratto', models.DO_NOTHING, db_column='Tipologia', blank=True, null=True)  # Field name made lowercase.
    ccnl = models.ForeignKey('TabellaCcnl', models.DO_NOTHING, db_column='ccnl', blank=True, null=True)
    codicecontratto = models.CharField(db_column='CodiceContratto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percentuale = models.ForeignKey('PercentualiContratto', models.DO_NOTHING, db_column='Percentuale', blank=True, null=True)  # Field name made lowercase.
    trasferte_fisse = models.IntegerField(blank=True, null=True)
    trasferte_fisse_tipo = models.CharField(max_length=2, blank=True, null=True)
    datainizio = models.DateField(db_column='DataInizio', blank=True, null=True)  # Field name made lowercase.
    datafine = models.DateField(db_column='DataFine', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contratti'


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

class Ingressidip(models.Model):
    id_ingresso = models.BigAutoField(primary_key=True)
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
    checked_in = models.IntegerField()
    checked_out = models.IntegerField()
    timestamp_scan_entrata = models.DateTimeField(blank=True, null=True)
    timestamp_scan_uscita = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IngressiDip'


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


class ListaSocieta(models.Model):
    id_societa = models.IntegerField(db_column='ID_Societa', primary_key=True)  # Field name made lowercase.
    nomeente = models.CharField(db_column='NomeEnte', max_length=100, blank=True, null=True)  # Field name made lowercase.
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

class Mansione(models.Model):
    id_mansione = models.AutoField(primary_key=True)
    tipo_mansione = models.CharField(unique=True, max_length=150, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mansione'

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
    stato = models.SmallIntegerField(blank=True, null=True)
    urgente = models.BooleanField(default=0, blank=False, null=True)
    note_richiesta = models.TextField(db_column='Note_richiesta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Richieste'
        verbose_name = 'Richiesta'
        verbose_name_plural = 'Richieste'
    
    def __str__(self):
        if self.id_permessi_richieste is not None:
            return f'{(self.id_permessi_richieste.tipopermesso).title()}'
        else: return "Permesso Orario"

    def get_absolute_url(self):
        return reverse("permessi:mie-richieste", kwargs={"pk": self.pk})


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

class RitardiStraordinari(models.Model):
    id_ritardo = models.BigAutoField(primary_key=True)
    id_dip_ingresso = models.ForeignKey(Ingressidip, models.DO_NOTHING, db_column='id_dip_ingresso')
    id_user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    ritardi = models.CharField(max_length=50, blank=True, null=True)
    anticipi = models.CharField(max_length=50, blank=True, null=True)
    straordinari = models.CharField(max_length=50, blank=True, null=True)
    trasferte = models.CharField(max_length=50, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ritardi_Straordinari'

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nome_sede = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sede'
            
    def __str__(self):
        return self.nome_sede

class Sesso(models.Model):
    id_sesso = models.AutoField(primary_key=True)
    sesso = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sesso'


class Societa(models.Model):
    id_societa = models.AutoField(primary_key=True)
    nome_societa = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Societa'
                
    def __str__(self):
        return self.nome_societa


class TabellaCcnl(models.Model):
    id_ccnl = models.AutoField(primary_key=True)
    tipo_contratto = models.CharField(max_length=250, blank=True, null=True)
    codice_ccnl = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabella_ccnl'


class TipoContratto(models.Model):
    id_contratto = models.AutoField(primary_key=True)
    nome_contratto = models.CharField(unique=True, max_length=100, blank=True, null=True)
    codice_contratto = models.CharField(max_length=10, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Contratto'
        ordering = ["nome_contratto"]
        
    def __str__(self):
        return self.nome_contratto


class TodoList(models.Model):
    id_lista = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user')
    todo = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    fatta = models.IntegerField(default=0,blank=True, null=True)
    setter = models.ForeignKey(CapoArea, models.DO_NOTHING, db_column='setter', blank=True, null=True)
    gruppo = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todo_list'
    
    def save(self, *args, **kwargs):
            self.todo = str(self.todo).title()
            super(TodoList, self).save(*args, **kwargs)
        
        

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
