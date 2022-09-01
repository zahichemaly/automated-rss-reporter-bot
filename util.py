from datetime import datetime as dt
from datetime import timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def get_date_today():
    return dt.now()

def get_date(dateString):
    #Date Format in feed
    #Fri, 10 Jul 2020 13:48:41 +0000
    #Sun, 19 Jun 2022 01:30:00 UTC
    #trimmedDate = dateString[:-6]
    return dt.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
