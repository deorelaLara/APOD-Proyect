from abc import ABC, abstractclassmethod

#interfaz para DB
class DBService(ABC):
    @abstractclassmethod
    def savePhoto(self):
        pass
    
    @abstractclassmethod
    def deletePhoto(self):
        pass
    
    @abstractclassmethod
    def getPhotoFromDB(self):
        pass
    '''
    @abstractclassmethod
    def searchPic(self):
        pass'''