import json
import requests

needleInStack = requests.post("http://challenge.code2040.org/api/haystack", data={'token':'656e703aa01b60f64f4c5b70501219f6'})

needleInStack = needleInStack.json()

needle = needleInStack['needle']
haystack = needleInStack['haystack']

for x in range(0,len(needleInStack)):
    if(haystack[x] == needle):
        r = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token':'656e703aa01b60f64f4c5b70501219f6', 'needle': x})
