from abc import ABC, abstractclassmethod

#interfaz para DB
class DBService(ABC):
    #Insert
    @abstractclassmethod
    def savePhoto(self):
        pass
    #Delete
    @abstractclassmethod
    def deletePhoto(self):
        pass
    #Select all photos on data base
    @abstractclassmethod
    def getPhoto(self):
        pass
    #Select photo by date 
    @abstractclassmethod
    def getPhotobyDate(self):
        pass