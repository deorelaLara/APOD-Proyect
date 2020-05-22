from abc import ABC, abstractclassmethod
import requests
import json

#CLASE PHOTO OBJETO
class APOD():
    def __init__(self, title):
        self.Title = title
        
#INTERFAZ API
class BiblioAPOD(ABC):
    @abstractclassmethod
    def SearchPicture(date):
        pass

def getPicture(date, bibliotec):
    apod = bibliotec.SearchPicture(date)
    return apod.Title

#IMPLEMENTACION
class Nasa(BiblioAPOD):
    def __init__(self, url_base):
        self.url = url_base

    def SearchPicture(self, date):
        res = requests.get('{}&date={}'.format(self.url, date))
        data = res.json()
        return APOD(data['title'])

        
    
    
if __name__ == '__main__':
    date = input('Insert Date:')
    #https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP&date=2020-04-04
    biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    print(getPicture(date, biblio))