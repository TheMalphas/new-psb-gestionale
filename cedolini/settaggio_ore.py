from .models import Cedolini as ced
from datetime import datetime, date, timedelta
import pandas as pd
import holidays
from workalendar.europe import Italy

def getDay(relMese,relAnno):
    if relMese == 12:
        relMeseC = 1
        relAnnoC = relAnno + 1
    else:
        relMeseC = relMese
        relAnnoC = relAnno
    obj=datetime(year=relAnno,month=relMese,day=1)
    objPlus=datetime(year=relAnnoC,month=relMeseC,day=1)
    startDay=datetime(relAnno,relMese,day=1)
    timediff=objPlus - timedelta(days=1)
    monthlastDay=timediff
    return obj, monthlastDay

def getRangeDate(firstDay,lastDay):
    deltaWeekDay = []
    delta=(lastDay.day - firstDay.day)+1
    for i in range(1,lastDay.day+1):
        weekDay = (datetime(year=firstDay.year,month=firstDay.month,day=i),datetime(year=firstDay.year,month=firstDay.month,day=i).weekday())
        deltaWeekDay.append(weekDay)
    return deltaWeekDay

def getHolidays(relAnno):
    cal = Italy().holidays(relAnno)
    
    holidaysDone = []
    
    for el in cal:
        holidaysDone.append(el[0])
    
    return holidaysDone

def getQuery(daysRange,calendario):
    queryRange = []
    for el in daysRange:
        if el[0].date() not in calendario and el[1] != 5 and el[1] != 6:
            queryRange.append(el[0].day)

    return queryRange


def activateQueryAzzera(id):
    queryRange=[1,2,3,4,5,6,7,8,9,10,
               11,12,13,14,15,16,17,18,19,20
               ,21,22,23,24,25,26,27,28,29,30,31]
    cedolino = ced.objects.filter(id_cedolino=id)
    for el in queryRange:
        if el == 1:
            cedolino.update(ord_01=None)
        if el == 2:
            cedolino.update(ord_02=None)
        if el == 3:
            cedolino.update(ord_03=None)
        if el == 4:
            cedolino.update(ord_04=None)
        if el == 5:
            cedolino.update(ord_05=None)
        if el == 6:
            cedolino.update(ord_06=None)
        if el == 7:
            cedolino.update(ord_07=None)
        if el == 8:
            cedolino.update(ord_08=None)
        if el == 9:
            cedolino.update(ord_09=None)
        if el == 10:
            cedolino.update(ord_10=None)
        if el == 11:
            cedolino.update(ord_11=None)
        if el == 12:
            cedolino.update(ord_12=None)
        if el == 13:
            cedolino.update(ord_13=None)
        if el == 14:
            cedolino.update(ord_14=None)
        if el == 15:
            cedolino.update(ord_15=None)
        if el == 16:
            cedolino.update(ord_16=None)
        if el == 17:
            cedolino.update(ord_17=None)
        if el == 18:
            cedolino.update(ord_18=None)
        if el == 19:
            cedolino.update(ord_19=None)
        if el == 20:
            cedolino.update(ord_20=None)
        if el == 21:
            cedolino.update(ord_21=None)
        if el == 22:
            cedolino.update(ord_22=None)
        if el == 23:
            cedolino.update(ord_23=None)
        if el == 24:
            cedolino.update(ord_24=None)
        if el == 25:
            cedolino.update(ord_25=None)
        if el == 26:
            cedolino.update(ord_26=None)
        if el == 27:
            cedolino.update(ord_27=None)
        if el == 28:
            cedolino.update(ord_28=None)
        if el == 29:
            cedolino.update(ord_29=None)
        if el == 30:
            cedolino.update(ord_30=None)
        if el == 31:
            cedolino.update(ord_31=None)

def activateQueryPerc(queryRange,id,perc):
    cedolino = ced.objects.filter(id_cedolino=id)
    percent = str(perc).replace(".","")
    perc = f'0.{percent}'
    perc = float(perc)
    for el in queryRange:
        if el == 1:
            cedolino.update(ord_01=round((8*perc)))
        if el == 2:
            cedolino.update(ord_02=round((8*perc)))
        if el == 3:
            cedolino.update(ord_03=round((8*perc)))
        if el == 4:
            cedolino.update(ord_04=round((8*perc)))
        if el == 5:
            cedolino.update(ord_05=round((8*perc)))
        if el == 6:
            cedolino.update(ord_06=round((8*perc)))
        if el == 7:
            cedolino.update(ord_07=round((8*perc)))
        if el == 8:
            cedolino.update(ord_08=round((8*perc)))
        if el == 9:
            cedolino.update(ord_09=round((8*perc)))
        if el == 10:
            cedolino.update(ord_10=round((8*perc)))
        if el == 11:
            cedolino.update(ord_11=round((8*perc)))
        if el == 12:
            cedolino.update(ord_12=round((8*perc)))
        if el == 13:
            cedolino.update(ord_13=round((8*perc)))
        if el == 14:
            cedolino.update(ord_14=round((8*perc)))
        if el == 15:
            cedolino.update(ord_15=round((8*perc)))
        if el == 16:
            cedolino.update(ord_16=round((8*perc)))
        if el == 17:
            cedolino.update(ord_17=round((8*perc)))
        if el == 18:
            cedolino.update(ord_18=round((8*perc)))
        if el == 19:
            cedolino.update(ord_19=round((8*perc)))
        if el == 20:
            cedolino.update(ord_20=round((8*perc)))
        if el == 21:
            cedolino.update(ord_21=round((8*perc)))
        if el == 22:
            cedolino.update(ord_22=round((8*perc)))
        if el == 23:
            cedolino.update(ord_23=round((8*perc)))
        if el == 24:
            cedolino.update(ord_24=round((8*perc)))
        if el == 25:
            cedolino.update(ord_25=round((8*perc)))
        if el == 26:
            cedolino.update(ord_26=round((8*perc)))
        if el == 27:
            cedolino.update(ord_27=round((8*perc)))
        if el == 28:
            cedolino.update(ord_28=round((8*perc)))
        if el == 29:
            cedolino.update(ord_29=round((8*perc)))
        if el == 30:
            cedolino.update(ord_30=round((8*perc)))
        if el == 31:
            cedolino.update(ord_31=round((8*perc)))


def activateQueryFull(queryRange,id):
    cedolino = ced.objects.filter(id_cedolino=id)
    for el in queryRange:
        if el == 1:
            cedolino.update(ord_01=8)
        if el == 2:
            cedolino.update(ord_02=8)
        if el == 3:
            cedolino.update(ord_03=8)
        if el == 4:
            cedolino.update(ord_04=8)
        if el == 5:
            cedolino.update(ord_05=8)
        if el == 6:
            cedolino.update(ord_06=8)
        if el == 7:
            cedolino.update(ord_07=8)
        if el == 8:
            cedolino.update(ord_08=8)
        if el == 9:
            cedolino.update(ord_09=8)
        if el == 10:
            cedolino.update(ord_10=8)
        if el == 11:
            cedolino.update(ord_11=8)
        if el == 12:
            cedolino.update(ord_12=8)
        if el == 13:
            cedolino.update(ord_13=8)
        if el == 14:
            cedolino.update(ord_14=8)
        if el == 15:
            cedolino.update(ord_15=8)
        if el == 16:
            cedolino.update(ord_16=8)
        if el == 17:
            cedolino.update(ord_17=8)
        if el == 18:
            cedolino.update(ord_18=8)
        if el == 19:
            cedolino.update(ord_19=8)
        if el == 20:
            cedolino.update(ord_20=8)
        if el == 21:
            cedolino.update(ord_21=8)
        if el == 22:
            cedolino.update(ord_22=8)
        if el == 23:
            cedolino.update(ord_23=8)
        if el == 24:
            cedolino.update(ord_24=8)
        if el == 25:
            cedolino.update(ord_25=8)
        if el == 26:
            cedolino.update(ord_26=8)
        if el == 27:
            cedolino.update(ord_27=8)
        if el == 28:
            cedolino.update(ord_28=8)
        if el == 29:
            cedolino.update(ord_29=8)
        if el == 30:
            cedolino.update(ord_30=8)
        if el == 31:
            cedolino.update(ord_31=8)