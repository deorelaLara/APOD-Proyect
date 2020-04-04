from abc import ABC, abstractclassmethod

#interfaz para DB
class PhotoBiblio(ABC):
    @abstractclassmethod
    def search(date):
        pass
   