""" Demonstrate use of Python for requesting info from the web.

astronaut data: http://open-notify.org/Open-Notify-API/People-In-Space/
mbta data: https://www.mbta.com/developers/v3-api

requests package: http://docs.python-requests.org/en/master/
"""

import requests

#astronaut info
astrodata = requests.get('http://api.open-notify.org/astros.json')
astronauts = astrodata.json()
print(astronauts)
print('There are {} people in space:'.format(astronauts['number']))
for astronaut in astronauts['people']:
    print(astronaut['name'])
print()

#mbta info
mbta = 'https://api-v3.mbta.com'

#get station names
response = requests.get('https://api-v3.mbta.com/stops?filter[route_type]=0,1')
stops = response.json()
#description, platform_name, id
station_names = [(int(stop['id']),
                  stop['attributes']['description']) for stop in stops['data']]
station_names.sort()
for station_name in station_names:
    print(station_name)

#select station ID for Boston University West - Green Line - Inbound
stop = '70142'

mbta = requests.get(mbta+'/predictions?filter[stop]={}'
                    '&page[limit]=5'.format(stop))
print('\n', mbta.json()['data'], '\n')

for train in mbta.json()['data']:
    arrivaltime = train['attributes']['arrival_time']
    arrivaltime = arrivaltime.split('T')[1].split('-')[0]
    print('Train expected at: ', arrivaltime)
