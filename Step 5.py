import json
import requests
import datetime
from datetime import timedelta

payload = requests.post("http://challenge.code2040.org/api/dating", data={'token': '656e703aa01b60f64f4c5b70501219f6'})

n = payload.json()

datestamp = n['datestamp']
interval = n['interval']

iso8601 = '%Y-%m-%dT%H:%M:%SZ'

timeStamp = datetime.datetime.strptime(datestamp, iso8601)

timeToAdd = timedelta(seconds=interval)

newTime = timeStamp + timeToAdd

newTime = newTime.strftime(iso8601)

r = requests.post("http://challenge.code2040.org/api/dating/validate", data = {'token':'656e703aa01b60f64f4c5b70501219f6','datestamp':newTime})
