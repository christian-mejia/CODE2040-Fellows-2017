#Step 5: The dating game

import json
import requests
import datetime
from datetime import timedelta

payload = requests.post("http://challenge.code2040.org/api/dating", 
                        data={'token':'656e703aa01b60f64f4c5b70501219f6'})

n = payload.json()

datestamp = n['datestamp']
interval = n['interval']

iso8601 = '%Y-%m-%dT%H:%M:%SZ'

#Convverts datestamp to iso8601 format
timeStamp = datetime.datetime.strptime(datestamp, iso8601)

#Converts interval to add to seconds
timeToAdd = timedelta(seconds=interval)

#Adds interval to timeStamp
newTime = timeStamp + timeToAdd

#Converts back to iso8601 format
newTime = newTime.strftime(iso8601)

r = requests.post("http://challenge.code2040.org/api/dating/validate", 
                  data = {'token':'656e703aa01b60f64f4c5b70501219f6',
                          'datestamp':newTime})
