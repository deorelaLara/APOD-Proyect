from abc import ABC, abstractclassmethod

#interfaz
class PhotoBiblio(ABC):
    @abstractclassmethod
   
    def search(date):
        pass
    
    def delete(date):
        pass
    
    def insert(date):
        pass
    
    def getPhoto(date, bibliotec):
        apod = bibliotec.search(date)
        return apod.title
    
    
    def deletePhoto(date, bibliotec):
        apod = bibliotec.delete(date)
        return apod.date