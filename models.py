# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    stato = models.IntegerField(blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

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
    stato = models.IntegerField(blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Straordinari'


class AddTrasferte(models.Model):
    id_trasferte = models.BigAutoField(primary_key=True)
    id_dip = models.ForeignKey('AnaDipendenti', models.DO_NOTHING, db_column='id_dip', blank=True, null=True)
    id_ced = models.ForeignKey('Cedolini', models.DO_NOTHING, db_column='id_ced', blank=True, null=True)
    rel_giorno = models.DateField(blank=True, null=True)
    stato = models.IntegerField(blank=True, null=True)
    ore = models.FloatField(blank=True, null=True)
    valore = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    timestamp_creazione = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_Trasferte'


class AnaDipendenti(models.Model):
    id_dip = models.AutoField(db_column='ID_Dip', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='User_id', blank=True, null=True)  # Field name made lowercase.
    id_contratto = models.ForeignKey('Contratti', models.DO_NOTHING, db_column='id_contratto', blank=True, null=True)
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
    stato = models.CharField(db_column='Stato', max_length=7, blank=True, null=True)  # Field name made lowercase.
    data_creazione = models.DateTimeField(db_column='Data_creazione', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ana_Dipendenti'


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nome_area = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'


class CapoArea(models.Model):
    id_capo = models.AutoField(db_column='ID_Capo', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_Dipendente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Capo_Area'


class Cedolini(models.Model):
    id_cedolino = models.BigAutoField(primary_key=True)
    dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='dipendente', blank=True, null=True)
    mese = models.IntegerField(blank=True, null=True)
    anno = models.IntegerField(blank=True, null=True)
    rimborsi = models.CharField(max_length=255, blank=True, null=True)
    inc_forf = models.CharField(max_length=255, blank=True, null=True)
    bonuses = models.CharField(max_length=255, blank=True, null=True)
    documenti = models.CharField(max_length=1000, blank=True, null=True)
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


class HistoryIngressidip(models.Model):
    id_ingresso = models.BigAutoField()
    nominativo_new = models.CharField(max_length=50)
    nominativo_old = models.CharField(max_length=50)
    registrato_da_user_new = models.IntegerField(blank=True, null=True)
    registrato_da_user_old = models.IntegerField(blank=True, null=True)
    giorno_new = models.DateField(blank=True, null=True)
    giorno_old = models.DateField(blank=True, null=True)
    entrata_new = models.TimeField(blank=True, null=True)
    entrata_old = models.TimeField(blank=True, null=True)
    uscita_new = models.TimeField(blank=True, null=True)
    uscita_old = models.TimeField(blank=True, null=True)
    seconda_entrata_new = models.TimeField(blank=True, null=True)
    seconda_entrata_old = models.TimeField(blank=True, null=True)
    timestamp_scan_entrata_new = models.DateTimeField(blank=True, null=True)
    timestamp_scan_entrata_old = models.DateTimeField(blank=True, null=True)
    timestamp_scan_uscita_new = models.DateTimeField(blank=True, null=True)
    timestamp_scan_uscita_old = models.DateTimeField(blank=True, null=True)
    timestamp_modifica = models.DateTimeField(blank=True, null=True)
    tipo_old = models.CharField(max_length=50, blank=True, null=True)
    tipo_new = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'History_IngressiDip'


class Ingressidip(models.Model):
    id_ingresso = models.BigAutoField(primary_key=True)
    id_dip_ing = models.IntegerField(blank=True, null=True)
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


class IngressidipM(models.Model):
    id_ingresso = models.BigAutoField(primary_key=True)
    id_dip_ing = models.IntegerField(blank=True, null=True)
    id_permesso = models.IntegerField(blank=True, null=True)
    tipo_permesso = models.IntegerField(blank=True, null=True)
    in_permesso = models.IntegerField(blank=True, null=True)
    nominativo = models.CharField(max_length=150, blank=True, null=True)
    registrato_da_user = models.IntegerField(blank=True, null=True)
    giorno = models.DateField(blank=True, null=True)
    tempo = models.TimeField(blank=True, null=True)
    timestamp_scan = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IngressiDip_m'


class Istruzione(models.Model):
    id_istruzione = models.AutoField(primary_key=True)
    tipo_istruzione = models.CharField(unique=True, max_length=100, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Istruzione'


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


class Mansione(models.Model):
    id_mansione = models.AutoField(primary_key=True)
    tipo_mansione = models.CharField(unique=True, max_length=150, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mansione'


class Mese(models.Model):
    id_mese = models.AutoField(primary_key=True)
    mese = models.CharField(db_column='Mese', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mese'


class PercentualiContratto(models.Model):
    id_ore_contratto = models.AutoField(primary_key=True)
    dicitura_percentuale = models.CharField(max_length=50, blank=True, null=True)
    perc_contratto = models.DecimalField(max_digits=20, decimal_places=2)
    ore_contratto = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Percentuali_contratto'


class Permessi(models.Model):
    id_permesso = models.IntegerField(db_column='ID_Permesso', primary_key=True)  # Field name made lowercase.
    codicepermesso = models.CharField(db_column='CodicePermesso', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tipopermesso = models.CharField(db_column='TipoPermesso', max_length=150, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permessi'


class Responsabili(models.Model):
    id_res = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Responsabili'


class ResponsabiliSede(models.Model):
    id_res_sede = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(db_column='NomeCompleto', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='Sede', blank=True, null=True)  # Field name made lowercase.
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Responsabili_sede'


class Richieste(models.Model):
    id_richiesta = models.AutoField(db_column='ID_richiesta', primary_key=True)  # Field name made lowercase.
    id_user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='ID_user', blank=True, null=True)  # Field name made lowercase.
    id_dipendente_richiesta = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='ID_dipendente_richiesta', blank=True, null=True)  # Field name made lowercase.
    id_permessi_richieste = models.ForeignKey(Permessi, models.DO_NOTHING, db_column='ID_permessi_richieste', blank=True, null=True)  # Field name made lowercase.
    nominativo = models.CharField(max_length=250, blank=True, null=True)
    da_giorno_richiesta = models.DateField()
    da_ora_richiesta = models.TimeField(blank=True, null=True)
    a_giorno_richiesta = models.DateField()
    a_ora_richiesta = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    time_accettato = models.DateTimeField(blank=True, null=True)
    stato = models.SmallIntegerField(blank=True, null=True)
    urgente = models.SmallIntegerField(blank=True, null=True)
    note_richiesta = models.TextField(db_column='Note_richiesta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Richieste'


class RichiesteAccettate(models.Model):
    id_richieste_accettate = models.AutoField(db_column='ID_richieste_accettate', primary_key=True)  # Field name made lowercase.
    id_richieste = models.ForeignKey(Richieste, models.DO_NOTHING, db_column='ID_richieste', blank=True, null=True)  # Field name made lowercase.
    id_capoarea_richieste = models.ForeignKey(CapoArea, models.DO_NOTHING, db_column='ID_capoArea_richieste', blank=True, null=True)  # Field name made lowercase.
    stato = models.SmallIntegerField(db_column='Stato', blank=True, null=True)  # Field name made lowercase.
    data_inizio_permesso = models.DateField(blank=True, null=True)
    data_fine_permesso = models.DateField(blank=True, null=True)
    ora_inizio_permesso = models.TimeField(blank=True, null=True)
    ora_fine_permesso = models.TimeField(blank=True, null=True)
    in_corso = models.IntegerField(blank=True, null=True)
    id_creazione = models.IntegerField(blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    id_update = models.IntegerField(blank=True, null=True)
    data_update = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Richieste_Accettate'


class RitardiStraordinari(models.Model):
    id_dip = models.IntegerField()
    id_user = models.IntegerField(blank=True, null=True)
    ritardi_mensili = models.CharField(max_length=50, blank=True, null=True)
    anticipi_mensili = models.CharField(max_length=50, blank=True, null=True)
    straordinari_mensili = models.CharField(max_length=50, blank=True, null=True)
    trasferte_mensili = models.CharField(max_length=50, blank=True, null=True)
    data_creazione = models.DateTimeField(blank=True, null=True)
    data_modifica = models.DateTimeField(blank=True, null=True)
    note = models.IntegerField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

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


class Stipendi(models.Model):
    id_stipendio = models.BigAutoField(primary_key=True)
    id_mensilita = models.BigIntegerField(blank=True, null=True)
    id_dipendente = models.ForeignKey(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente', blank=True, null=True)
    id_contratto = models.IntegerField(blank=True, null=True)
    ore_lavorative = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    stipendio = models.CharField(max_length=50, blank=True, null=True)
    straordinari = models.CharField(max_length=50, blank=True, null=True)
    trasferta = models.CharField(max_length=50, blank=True, null=True)
    bonus = models.CharField(max_length=50, blank=True, null=True)
    rimborso = models.CharField(max_length=50, blank=True, null=True)
    incentivo_forf = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    modificato_da = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Stipendi'


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


class AppoggioVerificaQr(models.Model):
    uuid_qr = models.CharField(max_length=50)
    id_dipendente = models.OneToOneField(AnaDipendenti, models.DO_NOTHING, db_column='id_dipendente')

    class Meta:
        managed = False
        db_table = 'appoggio_verifica_qr'


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


class TabellaCcnl(models.Model):
    id_ccnl = models.AutoField(primary_key=True)
    tipo_contratto = models.CharField(max_length=250, blank=True, null=True)
    codice_ccnl = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabella_ccnl'


class TodoList(models.Model):
    id_lista = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user')
    todo = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    fatta = models.IntegerField(blank=True, null=True)
    setter = models.ForeignKey(CapoArea, models.DO_NOTHING, db_column='setter', blank=True, null=True)
    gruppo = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todo_list'
