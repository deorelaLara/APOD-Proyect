import requests
import json

print('*****Astronomy Picture Of The Day******')

#API REQUEST 
url = 'https://api.nasa.gov/planetary/apod'
key = '?api_key=DEMO_KEY'
param = {'api_key': key}
resp = requests.get(url, params=param).json()

#INFORMACION OBTENIDA
print(resp["title"])
print(resp["date"])
print(resp["explanation"])
print(resp['media_type'])
print(resp['hdurl'])