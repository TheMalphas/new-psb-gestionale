from django.db import models
from django.urls import reverse
from decimal import *
from datetime import date, time, datetime, timedelta
from calendar import monthrange
from django.utils import timezone
import pytz
import math
from . import models
from workalendar.europe import Italy
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
from uuid import uuid4

@receiver(post_save, sender=models.Contratti)
def cedolini_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        yeary = datetime.now().date().year
        monthy = datetime.now().date().month
        dataStart = datetime.now().date()
        monthStart=dataStart.month
        for el in range(monthy, 13):
            cal = Italy()
            try:
                dipen = models.AnaDipendenti.objects.get(id_dip=instance.id_dip)
                obj, createdObj= models.Cedolini.objects.get_or_create(dipendente=dipen,mese=el,anno=yeary)
                if createdObj:
                    models.Cedolini.objects.create(dipendente=dipen,mese=el,anno=yeary,timestamp_creazione=timezone.now())
                    if instance.trasferte_fisse:
                        if str(instance.trasferte_fisse) != '0' and instance.trasferte_fisse != None and str(instance.trasferte_fisse) != "" and (str(instance.trasferte_fisse_tipo) == "30" or str(instance.trasferte_fisse_tipo) == "46"):
                            counter = int(instance.trasferte_fisse)
                            trasferta = str(instance.trasferte_fisse_tipo)
                            if counter != 0:
                                giorno = datetime.date(yeary,el,random.randint(1,31))
                                if cal.is_working_day(giorno):
                                    trasferter = str(giorno.day)
                                    cedolino = models.Cedolini.objects.filter(dipendente=dipen,mese=el,anno=yeary)
                                    if trasferter == '1':
                                        cedolino.tras_01 = float(trasferta)
                                    if trasferter == '2':
                                        cedolino.tras_02= float(trasferta)
                                    if trasferter == '3':
                                        cedolino.tras_03= float(trasferta)
                                    if trasferter == '4':
                                        cedolino.tras_04= float(trasferta)
                                    if trasferter == '5':
                                        cedolino.tras_05= float(trasferta)
                                    if trasferter == '6':
                                        cedolino.tras_06= float(trasferta)
                                    if trasferter == '7':
                                        cedolino.tras_07= float(trasferta)
                                    if trasferter == '8':
                                        cedolino.tras_08= float(trasferta)
                                    if trasferter == '9':
                                        cedolino.tras_09= float(trasferta)
                                    if trasferter == '10':
                                        cedolino.tras_10= float(trasferta)
                                    if trasferter == '11':
                                        cedolino.tras_11= float(trasferta)
                                    if trasferter == '12':
                                        cedolino.tras_12= float(trasferta)
                                    if trasferter == '13':
                                        cedolino.tras_13= float(trasferta)
                                    if trasferter == '14':
                                        cedolino.tras_14= float(trasferta)
                                    if trasferter == '15':
                                        cedolino.tras_15= float(trasferta)
                                    if trasferter == '16':
                                        cedolino.tras_16= float(trasferta)
                                    if trasferter == '17':
                                        cedolino.tras_17= float(trasferta)
                                    if trasferter == '18':
                                        cedolino.tras_18= float(trasferta)
                                    if trasferter == '19':
                                        cedolino.tras_19= float(trasferta)
                                    if trasferter == '20':
                                        cedolino.tras_20= float(trasferta)
                                    if trasferter == '21':
                                        cedolino.tras_21= float(trasferta)
                                    if trasferter == '22':
                                        cedolino.tras_22= float(trasferta)
                                    if trasferter == '23':
                                        cedolino.tras_23= float(trasferta)
                                    if trasferter == '24':
                                        cedolino.tras_24= float(trasferta)
                                    if trasferter == '25':
                                        cedolino.tras_25= float(trasferta)
                                    if trasferter == '26':
                                        cedolino.tras_26= float(trasferta)
                                    if trasferter == '27':
                                        cedolino.tras_27= float(trasferta)
                                    if trasferter == '28':
                                        cedolino.tras_28= float(trasferta)
                                    if trasferter == '29':
                                        cedolino.tras_29= float(trasferta)
                                    if trasferter == '30':
                                        cedolino.tras_30= float(trasferta)
                                    if trasferter == '31':
                                        cedolino.tras_31= float(trasferta)
                                    counter -= 1
                else:
                    if instance.trasferte_fisse:
                        if str(instance.trasferte_fisse) != '0' and instance.trasferte_fisse != None and str(instance.trasferte_fisse) != "" and (str(instance.trasferte_fisse_tipo) == "30" or str(instance.trasferte_fisse_tipo) == "46"):
                            counter = int(instance.trasferte_fisse)
                            trasferta = str(instance.trasferte_fisse_tipo)
                            if counter != 0:
                                giorno = datetime.date(yeary,el,random.randint(1,31))
                                if cal.is_working_day(giorno):
                                    trasferter = str(giorno.day)
                                    cedolino = models.Cedolini.objects.filter(dipendente=dipen,mese=el,anno=yeary)
                                    if trasferter == '1':
                                        cedolino.tras_01 = float(trasferta)
                                    if trasferter == '2':
                                        cedolino.tras_02= float(trasferta)
                                    if trasferter == '3':
                                        cedolino.tras_03= float(trasferta)
                                    if trasferter == '4':
                                        cedolino.tras_04= float(trasferta)
                                    if trasferter == '5':
                                        cedolino.tras_05= float(trasferta)
                                    if trasferter == '6':
                                        cedolino.tras_06= float(trasferta)
                                    if trasferter == '7':
                                        cedolino.tras_07= float(trasferta)
                                    if trasferter == '8':
                                        cedolino.tras_08= float(trasferta)
                                    if trasferter == '9':
                                        cedolino.tras_09= float(trasferta)
                                    if trasferter == '10':
                                        cedolino.tras_10= float(trasferta)
                                    if trasferter == '11':
                                        cedolino.tras_11= float(trasferta)
                                    if trasferter == '12':
                                        cedolino.tras_12= float(trasferta)
                                    if trasferter == '13':
                                        cedolino.tras_13= float(trasferta)
                                    if trasferter == '14':
                                        cedolino.tras_14= float(trasferta)
                                    if trasferter == '15':
                                        cedolino.tras_15= float(trasferta)
                                    if trasferter == '16':
                                        cedolino.tras_16= float(trasferta)
                                    if trasferter == '17':
                                        cedolino.tras_17= float(trasferta)
                                    if trasferter == '18':
                                        cedolino.tras_18= float(trasferta)
                                    if trasferter == '19':
                                        cedolino.tras_19= float(trasferta)
                                    if trasferter == '20':
                                        cedolino.tras_20= float(trasferta)
                                    if trasferter == '21':
                                        cedolino.tras_21= float(trasferta)
                                    if trasferter == '22':
                                        cedolino.tras_22= float(trasferta)
                                    if trasferter == '23':
                                        cedolino.tras_23= float(trasferta)
                                    if trasferter == '24':
                                        cedolino.tras_24= float(trasferta)
                                    if trasferter == '25':
                                        cedolino.tras_25= float(trasferta)
                                    if trasferter == '26':
                                        cedolino.tras_26= float(trasferta)
                                    if trasferter == '27':
                                        cedolino.tras_27= float(trasferta)
                                    if trasferter == '28':
                                        cedolino.tras_28= float(trasferta)
                                    if trasferter == '29':
                                        cedolino.tras_29= float(trasferta)
                                    if trasferter == '30':
                                        cedolino.tras_30= float(trasferta)
                                    if trasferter == '31':
                                        cedolino.tras_31= float(trasferta)
                                    counter -= 1
            except Exception as err:
                print(err)