#Step 1 Registration

import json
import requests

payload = {'token': '656e703aa01b60f64f4c5b70501219f6',
           'github': 'https://github.com/christian-mejia/CODE2040-Fellows-2017'}

r = requests.post("http://challenge.code2040.org/api/register", data=payload)

