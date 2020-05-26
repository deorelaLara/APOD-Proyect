from abc import ABC, abstractclassmethod
import requests
import json

#CLASE PHOTO OBJETO
class APOD():
    def __init__(self, title, hdurl, explanation, date, media_type):
        self.Title = title
        self.Hdurl= hdurl
        self.Explanation = explanation
        self.Date = date
        self.Media_type = media_type
        
#INTERFAZ API
class BiblioAPOD(ABC):
    @abstractclassmethod
    def SearchPicture(date):
        pass

def getPicture(date, bibliotec):
    apod = bibliotec.SearchPicture(date)
    return apod.Title, apod.Hdurl ,apod.Explanation, apod.Date, apod.Media_type

#IMPLEMENTACION
class Nasa(BiblioAPOD):
    def __init__(self, url_base):
        self.url = url_base

    def SearchPicture(self, date):
        res = requests.get('{}&date={}'.format(self.url, date))
        data = res.json()
        return APOD(data['date'] ,data['title'], data['explanation'], data['hdurl'], data['media_type'])
    
    
if __name__ == '__main__':
    date = input('Insert Date:')
    #https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP&date=2020-04-04
    biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    print(getPicture(date, biblio))