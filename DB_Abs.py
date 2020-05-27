from abc import ABC, abstractclassmethod

#interfaz para DB
class DBService(ABC):
    #Insert
    @abstractclassmethod
    def savePhoto(self):
        pass
    '''
    #delete
    @abstractclassmethod
    def deletePhoto(self):
        pass
    #select
    @abstractclassmethod
    def getPhotoFromDB(self):
        pass'''
    '''
    @abstractclassmethod
    def searchPic(self):
        pass'''