#Step 2: Reverse a string

import json
import requests

string = requests.post("http://challenge.code2040.org/api/reverse", 
                       data={'token': '656e703aa01b60f64f4c5b70501219f6'})

reversedStr = string.text[::-1]   #Reverses string

data = requests.post("http://challenge.code2040.org/api/reverse/validate", 
                     data = {'token': '656e703aa01b60f64f4c5b70501219f6', 
                             'string':reversedStr})
