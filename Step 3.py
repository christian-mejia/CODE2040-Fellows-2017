#Step 3: Needle in a haystack

import json
import requests

challengeRequest = requests.post("http://challenge.code2040.org/api/haystack", 
                              data={'token':'656e703aa01b60f64f4c5b70501219f6'})

needleInStack = challengeRequest.json()

#Retrieving values from dictionary
needle = needleInStack['needle']
haystack = needleInStack['haystack']

#Looping through haystack to find needle
for x in range(0,len(needleInStack)):
    if(haystack[x] == needle):
        r = requests.post("http://challenge.code2040.org/api/haystack/validate", 
                          data={'token':'656e703aa01b60f64f4c5b70501219f6', 
                                'needle': x})
