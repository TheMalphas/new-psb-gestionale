# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import date, time, datetime, timedelta
from django.core.signals import setting_changed, request_finished, request_started
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from decimal import *
import math

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
        ordering = ['nome']
        
    def __unicode__(self):
        return self.id_dip
    
    @property
    def nominativo(self):
        return f'{(self.cognome).title()} {(self.nome).title()}'

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
        
    def __unicode__(self):
        return self.nome_area

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
    id_capo = models.IntegerField(db_column='ID_Capo', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey("Sede", models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dipendente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Capo_Area'
    
    def __str__(self):
        return self.nomecompleto


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

    @property
    def ritardo(self):
        orarioritardo = datetime.strptime("09:00:00", '%H:%M:%S').time()
        orariolav = datetime.strptime("09:05:00", '%H:%M:%S').time()
        orariolavpulizieritardo = datetime.strptime("07:00:00", '%H:%M:%S').time()
        orariolavpulizie = datetime.strptime("07:05:00", '%H:%M:%S').time()
        orariolavediliziaritardo = datetime.strptime("08:00:00", '%H:%M:%S').time()
        orariolavedilizia = datetime.strptime("08:05:00", '%H:%M:%S').time()
        
        if self.id_dip_ing.area:
            if self.id_dip_ing.area.id_area == 21:
                if self.entrata and self.entrata > orariolavpulizie:
                    ritardo = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), orariolavpulizieritardo)
                    return f'{str(ritardo)}'
            elif self.id_dip_ing.area.id_area == 10:
                if self.entrata and self.entrata > orariolavedilizia:
                    ritardo = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), orariolavediliziaritardo)
                    return f'{str(ritardo)}'
            else:
                if self.entrata and self.entrata > orariolav:
                    ritardo = datetime.combine(date.today(), self.entrata) - datetime.combine(date.today(), orarioritardo)
                    return f'{str(ritardo)}'
        
    @property
    def anticipo(self):
        orariolav = datetime.strptime("09:00:00", '%H:%M:%S').time()
        orariolavpulizie = datetime.strptime("07:00:00", '%H:%M:%S').time()
        orariolavedilizia = datetime.strptime("08:00:00", '%H:%M:%S').time()
        
        if self.id_dip_ing.area:
            if self.id_dip_ing.area.id_area == 21:
                if self.entrata and self.entrata < orariolavpulizie:
                    anticipo = datetime.combine(date.today(), orariolavpulizie) - datetime.combine(date.today(), self.entrata)
                    return f'{str(anticipo)}'
            elif self.id_dip_ing.area.id_area == 10:
                if self.entrata and self.entrata < orariolavedilizia:
                    anticipo = datetime.combine(date.today(), orariolavedilizia) - datetime.combine(date.today(), self.entrata)
                    return f'{str(anticipo)}'
            else:
                if self.entrata and self.entrata < orariolav:
                    anticipo = datetime.combine(date.today(), orariolav) - datetime.combine(date.today(), self.entrata)
                    return f'{str(anticipo)}'
    
    @property
    def straordinario(self):
        if self.id_dip_ing.area == 21:
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
                                return str(checkEntrata)
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
                return str(straordinario)
        elif self.id_dip_ing.area == 10:
            orariolav = datetime.strptime("08:00:00", '%H:%M:%S').time()
            orariolavfine = datetime.strptime("17:00:00", '%H:%M:%S').time()
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
                                return str(checkEntrata)
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
                return str(straordinario)
        else:
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
                                return str(checkEntrata)
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
                return str(straordinario)

    @property
    def in_permState(self):
        if self.in_permesso and self.id_permesso != None:
            in_permState = self.id_permesso.id_permessi_richieste
            return in_permState
        elif self.in_permesso and self.in_permesso == None:
            in_permState = f'{self.id_permesso.da_ora_richiesta} - {self.id_permesso.a_ora_richiesta}'
        elif not(self.in_permesso):
            in_permState = 'No'
            return
    
    @property
    def getarea(self):
        if self.id_dip_ing.area:
            areas = f'{self.id_dip_ing.area.nome_area}'
            ar = areas.split(" ")
            return ar[0].title()
        else: "No Area"
        
    @property
    def getsocieta(self):
        if self.id_dip_ing.societa:
            societas = f'{self.id_dip_ing.societa.nome_societa}'
            soc = societas.split(" ")
            return soc[0].title()
        else: "No Società"
    
    @property
    def getsede(self):
        if self.id_dip_ing.sede:
            sed = f'{self.id_dip_ing.sede.nome_sede}'
            sedez = sed.split(" ")
            return sedez[0].title()
        else: "No Sede"
        
    def get_data(self):
        try:
            data = {
            'id_ingresso': self.id_ingresso,
            'id_dip_ing': self.id_dip_ing.nominativo,
            'in_permesso': self.in_permesso,
            'id_permesso': self.id_permesso.id_permessi_richieste,
            'nominativo': self.nominativo,
            'entrata': self.entrata,
            'uscita': self.uscita,
            'seconda_entrata': self.seconda_entrata,
            'seconda_uscita': self.seconda_uscita,
            'checked_in': self.checked_in,
            'checked_out': self.checked_out,
            'tipo': self.tipo,
            }
            return data
        except Exception as err:
            print(err)
        
            
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
        if self.entrata:
            self.timestamp_scan_entrata = timezone.now() + timezone.timedelta(hours=1)
        if self.uscita:
            self.timestamp_scan_uscita = timezone.now() + timezone.timedelta(hours=1)
        if self.seconda_entrata:
            self.timestamp_scan_entrata = timezone.now() + timezone.timedelta(hours=1)
        if self.seconda_uscita:
            self.timestamp_scan_uscita = timezone.now() + timezone.timedelta(hours=1)
        super(Ingressidip, self).save(*args, **kwargs)

@receiver(post_save, sender=Ingressidip)
def upper_fields(sender, instance, *args, **kwargs):
    if instance.entrata != "":
        instance.checked_in = True
    if instance.uscita != "":
        instance.checked_out = True


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

class Ritardi_Anticipi(models.Model):
    tempo = models.TimeField(db_column='tempo')
    avg_tempo = models.TimeField(db_column='avg_tempo', blank=True, null=True)
    mese = models.IntegerField(db_column='mese')
    nominativo = models.CharField(db_column='nominativo', max_length=250)
    id_dipendente = models.IntegerField(db_column='id_dipendente')
    
    class Meta:
        managed = False
        db_table = 'Ritardi_Anticipi'


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
        # queryset_AnaDipendenti = AnaDipendenti.objects.get(id_dip__exact=self.id_dipendente_richiesta)
        # queryset_CapoArea = CapoArea.objects.get(id_capo__exact=queryset_AnaDipendenti)
        strstamp = self.timestamp
        day = str(strstamp).split(" ")
        
        if self.stato == 0:
            return f"Richiesta di {AnaDipendenti.objects.get(user=self.id_user)}, rifiutata da" #{RichiesteAccettate.objects.get(id_capoarea_richieste__exact=queryset_CapoArea)}."
        elif self.stato == 1:
            return f" Richiesta di {AnaDipendenti.objects.get(user=self.id_user)}, accettata da" #{RichiesteAccettate.objects.get(id_capoarea_richieste__exact=queryset_CapoArea)}."
        else:
            return f" Richiesta di {AnaDipendenti.objects.get(user=self.id_user)}, da revisionare."
    


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

@receiver(post_save, sender=RichiesteAccettate)
def change_cedolini(sender, instance, *args, **kwargs):
    if instance.entrata != "":
        instance.checked_in = True
    if instance.uscita != "":
        instance.checked_out = True

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
