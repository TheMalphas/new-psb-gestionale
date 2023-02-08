# Generated by Django 3.2.5 on 2022-11-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnaDipendenti',
            fields=[
                ('id_dip', models.AutoField(db_column='ID_Dip', primary_key=True, serialize=False)),
                ('dip_capo_area', models.IntegerField(blank=True, db_column='Dip_Capo_Area', null=True)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=100, null=True)),
                ('cognome', models.CharField(blank=True, db_column='Cognome', max_length=100, null=True)),
                ('codice_fiscale', models.CharField(blank=True, db_column='Codice_Fiscale', max_length=17, null=True)),
                ('luogo_nascita', models.CharField(blank=True, db_column='Luogo_Nascita', max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, db_column='Provincia', max_length=2, null=True)),
                ('cap', models.CharField(blank=True, db_column='Cap', max_length=6, null=True)),
                ('data_nascita', models.DateField(blank=True, db_column='Data_Nascita', null=True)),
                ('indirizzo', models.CharField(blank=True, db_column='Indirizzo', max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=30, null=True)),
                ('cellulare', models.CharField(blank=True, db_column='Cellulare', max_length=30, null=True)),
                ('email', models.CharField(db_column='Email', max_length=75)),
                ('seconda_email', models.CharField(db_column='Seconda_Email', max_length=75)),
                ('iban', models.CharField(blank=True, db_column='IBAN', max_length=27, null=True)),
                ('p_iva', models.CharField(blank=True, db_column='P_Iva', max_length=11, null=True)),
                ('istruzione', models.IntegerField(blank=True, db_column='Istruzione', null=True)),
                ('mansione', models.CharField(blank=True, db_column='Mansione', max_length=100, null=True)),
                ('stato', models.CharField(blank=True, db_column='Stato', max_length=7, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, db_column='Data_creazione', null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Ana_Dipendenti',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nome_area', models.CharField(blank=True, max_length=29, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapoArea',
            fields=[
                ('id_capo', models.IntegerField(db_column='ID_Capo', primary_key=True, serialize=False)),
                ('nomecompleto', models.CharField(blank=True, db_column='NomeCompleto', max_length=250, null=True)),
                ('sede', models.CharField(blank=True, db_column='Sede', max_length=16, null=True)),
                ('area', models.CharField(blank=True, db_column='Area', max_length=29, null=True)),
            ],
            options={
                'db_table': 'Capo_Area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contratti',
            fields=[
                ('id_contratto', models.AutoField(db_column='ID_Contratto', primary_key=True, serialize=False)),
                ('id_societa', models.IntegerField(blank=True, db_column='ID_Societa', null=True)),
                ('codicecontratto', models.CharField(blank=True, db_column='CodiceContratto', max_length=2, null=True)),
                ('tipologia', models.CharField(blank=True, db_column='Tipologia', max_length=23, null=True)),
                ('parziale', models.CharField(blank=True, db_column='Parziale', max_length=5, null=True)),
                ('orecontrattuali', models.CharField(blank=True, db_column='OreContrattuali', max_length=3, null=True)),
                ('datainizio', models.DateField(blank=True, db_column='DataInizio', null=True)),
                ('datafine', models.DateField(blank=True, db_column='DataFine', null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
                ('id_permesso', models.IntegerField(blank=True, db_column='ID_Permesso', null=True)),
            ],
            options={
                'db_table': 'Contratti',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingressidip',
            fields=[
                ('id_ingresso', models.BigAutoField(primary_key=True, serialize=False)),
                ('in_permesso', models.IntegerField(blank=True, null=True)),
                ('nominativo', models.CharField(blank=True, max_length=150, null=True)),
                ('giorno', models.DateField(blank=True, null=True)),
                ('entrata', models.TimeField(blank=True, null=True)),
                ('uscita', models.TimeField(blank=True, null=True)),
                ('seconda_entrata', models.TimeField(blank=True, null=True)),
                ('seconda_uscita', models.TimeField(blank=True, null=True)),
                ('checked_in', models.IntegerField()),
                ('checked_out', models.IntegerField()),
            ],
            options={
                'db_table': 'IngressiDip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Istruzione',
            fields=[
                ('id_istruzione', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_istruzione', models.CharField(blank=True, max_length=23, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Istruzione',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListaSocieta',
            fields=[
                ('id_societa', models.IntegerField(db_column='ID_Societa', primary_key=True, serialize=False)),
                ('nomeente', models.CharField(blank=True, db_column='NomeEnte', max_length=100, null=True)),
                ('comuneente', models.CharField(blank=True, db_column='ComuneEnte', max_length=50, null=True)),
                ('provente', models.CharField(blank=True, db_column='ProvEnte', max_length=2, null=True)),
                ('indirizzoente', models.CharField(blank=True, db_column='IndirizzoEnte', max_length=50, null=True)),
                ('partitaivaente', models.CharField(blank=True, db_column='PartitaIvaEnte', max_length=50, null=True)),
                ('codicefiscaleente', models.CharField(blank=True, db_column='CodiceFiscaleEnte', max_length=50, null=True)),
                ('legalerapp', models.CharField(blank=True, db_column='LegaleRapp', max_length=50, null=True)),
                ('id_capo', models.IntegerField(blank=True, db_column='ID_Capo', null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Lista_Societa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permessi',
            fields=[
                ('id_permesso', models.IntegerField(db_column='ID_Permesso', primary_key=True, serialize=False)),
                ('codicepermesso', models.CharField(blank=True, db_column='CodicePermesso', max_length=3, null=True)),
                ('tipopermesso', models.CharField(blank=True, db_column='TipoPermesso', max_length=150, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Permessi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Richieste',
            fields=[
                ('id_richiesta', models.AutoField(db_column='ID_richiesta', primary_key=True, serialize=False)),
                ('nominativo', models.CharField(blank=True, max_length=250, null=True)),
                ('da_giorno_richiesta', models.DateField()),
                ('da_ora_richiesta', models.TimeField(blank=True, null=True)),
                ('a_giorno_richiesta', models.DateField()),
                ('a_ora_richiesta', models.TimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('stato', models.SmallIntegerField(blank=True, null=True)),
                ('urgente', models.BooleanField(default=0, null=True)),
                ('note_richiesta', models.TextField(blank=True, db_column='Note_richiesta', null=True)),
            ],
            options={
                'verbose_name': 'Richiesta',
                'verbose_name_plural': 'Richieste',
                'db_table': 'Richieste',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RichiesteAccettate',
            fields=[
                ('id_richieste_accettate', models.AutoField(db_column='ID_richieste_accettate', primary_key=True, serialize=False)),
                ('stato', models.SmallIntegerField(blank=True, db_column='Stato', null=True)),
                ('data_inizio_permesso', models.DateField(blank=True, null=True)),
                ('data_fine_permesso', models.DateField(blank=True, null=True)),
                ('ora_inizio_permesso', models.TimeField(blank=True, null=True)),
                ('ora_fine_permesso', models.TimeField(blank=True, null=True)),
                ('data_creazione', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Richieste_Accettate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RitardiStraordinari',
            fields=[
                ('id_ritardo', models.BigAutoField(primary_key=True, serialize=False)),
                ('ritardi', models.CharField(blank=True, max_length=50, null=True)),
                ('anticipi', models.CharField(blank=True, max_length=50, null=True)),
                ('straordinari', models.CharField(blank=True, max_length=50, null=True)),
                ('trasferte', models.CharField(blank=True, max_length=50, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Ritardi_Straordinari',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.AutoField(primary_key=True, serialize=False)),
                ('nome_sede', models.CharField(blank=True, max_length=22, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Sede',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Societa',
            fields=[
                ('id_societa', models.AutoField(primary_key=True, serialize=False)),
                ('nome_societa', models.CharField(blank=True, max_length=67, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Societa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoContratto',
            fields=[
                ('id_contratto', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contratto', models.CharField(blank=True, max_length=23, null=True)),
                ('data_creazione', models.DateTimeField(blank=True, null=True)),
                ('data_modifica', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, db_column='Note', null=True)),
            ],
            options={
                'db_table': 'Tipo_Contratto',
                'managed': False,
            },
        ),
    ]
