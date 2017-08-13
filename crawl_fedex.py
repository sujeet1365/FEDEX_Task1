import requests
from datetime import date as dt
import calendar as cl

def day_info(dd, mm, yy):
    d, m, y = int(date), int(month), int(year)
    tempDate = dt(y, m, d)
    dayName = cl.day_name[tempDate.weekday()]
    return dayName[:3]


print("Done!!!")