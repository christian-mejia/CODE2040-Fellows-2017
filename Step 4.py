import json
import requests

payload = requests.post("http://challenge.code2040.org/api/prefix",data={'token':'656e703aa01b60f64f4c5b70501219f6'})

n = payload.json()

prefix = n['prefix']
array = n['array']

arrayNoPrefix = []

for item in array:
    if not item.startswith(prefix):
        arrayNoPrefix.append(item)

r = requests.post("http://challenge.code2040.org/api/prefix/validate", json={'token':'656e703aa01b60f64f4c5b70501219f6', 'array':arrayNoPrefix})
