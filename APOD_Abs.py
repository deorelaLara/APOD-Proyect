from abc import ABC, abstractclassmethod

"""
    Toma como parametro la fecha de la foto y regresa un objeto de tipo Photo, 
    la clase que se que conecte al api implementa esta clase abstracta
    
    @abstractclassmethod
    def deletePicture(date):
        pass
    
    @abstractclassmethod
    def savePicture(date):
        pass
"""
    
#INTERFAZ PARA API
class BiblioAPOD(ABC):
    
    @abstractclassmethod
    def SearchPicture(date):
        pass