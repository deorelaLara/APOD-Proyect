import requests
import json


def jPrint(obj):
    #create a formatted string of the python json object 
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#PRUEBA PARA SABER SI ESTA CONECTANDO CON EL SERVIDOR 
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP&date=1995-07-16')
#print(json.dumps(response, indent=4))
jPrint(response.json())