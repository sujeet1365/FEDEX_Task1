import requests
import json
from datetime import date as dt
import calendar as cl

def find_date(date, month, year):
    d, m, y = int(date), int(month), int(year)
    tempDate = dt(y, m, d)
    dayName = cl.day_name[tempDate.weekday()]
    return dayName[:3]


trac_no = '744668909687'

data = requests.post('https://www.fedex.com/trackingCal/track', data={
    'data': json.dumps({
        'TrackPackagesRequest': {
            'appType': 'wtrk',
            'uniqueKey': '',
            'processingParameters': {
                'anonymousTransaction': True,
                'clientId': 'WTRK',
                'returnDetailedErrors': True,
                'returnLocalizedDateTime': False
            },
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': trac_no,
                    'trackingQualifier': '',
                    'trackingCarrier': ''
                }
            }]
        }
    }),
    'action': 'trackpackages',
    'locale': 'en_US',
    'format': 'json',
    'version': 99
}).json()

p_details = data["TrackPackagesResponse"]["packageList"][0]
mainData = p_details["statusWithDetails"]
rawShipDate = p_details["displayTenderedDt"].split('/')
dayNameShipment = find_date(rawShipDate[1], rawShipDate[0], rawShipDate[2])
desiredShipDate = rawShipDate[1] + '/' + rawShipDate[0] + '/' + rawShipDate[2]

mainDataSplit = mainData.split(':')
status = mainDataSplit[0]
rawDeliveryDate = mainDataSplit[1][:10].split('/')
dayNameDelivery = find_date(rawDeliveryDate[1], rawDeliveryDate[0], rawDeliveryDate[2])
deliveryDate = rawDeliveryDate[1] + '/' + rawDeliveryDate[0] + '/' + rawDeliveryDate[2]

time = mainDataSplit[1][-1] + ':' + mainDataSplit[2][1:6]

output = "{\ntracking number: " + trac_no + ",\nshiping date: " + dayNameShipment + " " + desiredShipDate + ",\nstatus: " + status + ',\nscheduled delivery: ' + dayNameDelivery + " " + deliveryDate + " " + time + "\n}"

print(output)