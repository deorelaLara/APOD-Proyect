from abc import ABC, abstractclassmethod
import requests

class APOD():
    def __init__(self, **args):
        self.Date = args.get('date')
        self.Description = args.get('description')
        self.hdUrl = args.get('hdUrl')
        self.Title = args.get('title')
        
class BiblioAPOD(ABC):
    @abstractclassmethod
    def Search(date):
        pass

def getAPOD(date, bibliotec):
    apod = bibliotec.Search(date)
    return apod.Title

class Nasa(BiblioAPOD):
    def __init__(self, url_base):
        self.url = url_base
        
    def Search(self, date=''):
        res = requests.get('{}/{}'.format(self.url, date))
        json = res.json()
        return APOD(json['date'])
    
    
if __name__ == '__main__':
    biblio = Nasa('https://api.nasa.gov/planetary/apod') #URL para hacer el request
    print(getAPOD('2020-03-16', biblio))