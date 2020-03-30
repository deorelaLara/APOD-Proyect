from abc import ABC, abstractclassmethod

#interfaz
class PhotoBiblio(ABC):
    @abstractclassmethod
   
    def search(date):
        pass
    
    def getPhoto(date, bibliotec):
        apod = bibliotec.search(date)
        return apod.title