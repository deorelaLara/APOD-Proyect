import requests
import json
from Photo import *
from APOD_Abs import *
from DB_Abs import *
import sqlite3
import os 

##############################################################################
################## IMPLEMENTACION INTERFAZ API ##############################
#############################################################################

def getPicture(bibliotec):#devuelve de json a Photo


    keys=['date','title','explanation','url','media_type']
    rules=[[keys[0],10,],[keys[1],200],[keys[2],3000],[keys[3],200],[keys[4],350]]
    print("DBG: ",len(bibliotec))
    print("DBG: ",bibliotec.keys())

    if (not isinstance(bibliotec,dict)):
        print(" [-] Error, bibliotec not is dict ")   
        return 1
    if(len(bibliotec)!=5):
        print(" [-] Error, bibliotec len != 5 ")   
        return 1
    for k,v in bibliotec.items():
        if( k not in keys):
            print(" [-] Error ",v," is not in keys")
            return 1
        if (not isinstance(v,str)):
            print(" [-] Error in ",k, " : ", v)
            return 1
        if k==keys[0] and len(v)!=rules[0][1]:
            print(" [-] Error in ",k, " : ", v)
            return 1
        if k==keys[1] and len(v)>rules[1][1]:
            print(" [-] Error in ",k , " : ", v)
            return 1
        if k==keys[2] and len(v)>rules[2][1]:
            print(" [-] Error in ",k," ", len(v))
            print(v)
            return 1
        if k==keys[3] and (len(v)>rules[3][1] or len(v)<10):
            print(" [-] Error in ",k, " : ", v)
            return 1
        if k==keys[4] and (len(v)>rules[4][1] or v!='image'):
            print(" [-] Error in ",k, " : ", v)
            return 1

    photo = Photo(bibliotec['date'], bibliotec['title'], bibliotec['explanation'], bibliotec['url'], bibliotec['media_type'])    

    return photo
    #return apod.date, apod.title, apod.explanation, apod.url, apod.media_type

class Nasa(BiblioAPOD):
    def __init__(self, url_base):

        self.url = url_base
    

    def SearchPicture(self, date):

        keys=['date','title','explanation','url','media_type']

        if (not isinstance(date, str)) or date==(" " or "")  or date==None or len(date)==0  or len(date)!=10 :
            print(" [-] Error en datatype, len or is null [if]", date)
            return 1
        for x in date:
            if not (x.isnumeric() or x=='-'):
                print(" [-] Error en id tiene caracteres especiales")
                return 1
        try:
            res = requests.get('{}&date={}'.format(self.url, date))
            print("\treq >>>>",'{}&date={}'.format(self.url, date))
            status=res.status_code
            data = res.json()
            print("status >>>>>>> ",status)
            if(status!=200):
                print(" [-] Error en request",res.status_code)
                return 1
            myres={k:v for (k,v) in data.items() if k in keys }
            return (dict(myres))
        except:
            return 1


##############################################################################
################## IMPLEMENTACION INTERFAZ DB ###############################
#############################################################################

class DBServices(DBService):

    #Insertar datos desde API a DB
    def savePhoto(self, photo):


        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('----------------------------------------------------------------------------------')
        print('Connected!')
        try:
            cursor.execute("INSERT INTO photo(date, title, explanation, hdurl, mediaType) VALUES (?,?,?,?,?)",(photo.date,photo.title,photo.explanation,photo.url,photo.media_type))
            #cursor.execute("INSERT INTO photo(date, title, explanation, hdurl, mediaType) VALUES (?,?,?,?,?)",(photo[0],photo[1],photo[2],photo[3],photo[4]))
            conn.commit()
            print('----------------------------------------------------------------------------------')
            print('Foto insertada con exito!')
            cursor.close()

        except sqlite3.Error as error:
            print('Error --->', error)
        
        finally:
            if(conn):
                conn.close()

    #Eliminar fato desde la DB
    def deletePhoto(self):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('----------------------------------------------------------------------------------')
        print('Connected!')
        print('----------------------------------------------------------------------------------')
        try:
            fecha = input('Insert Date: ')
            cursor = conn.execute("DELETE FROM photo WHERE date=?", (fecha, ))
            print('Photo successfully deleted')
            conn.commit()

        except sqlite3.Error as error:
            print('Error --->', error)
        
        finally:
            if(conn):
                conn.close()

    
    #Mostrar fotos almacenadas desde la DB
    def getPhoto(self):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('----------------------------------------------------------------------------------')
        print('Connected!')
        print('----------------------------------------------------------------------------------')
        try:
            cursor = conn.execute("SELECT * FROM photo")
            [print(elemento) for elemento  in cursor] 
            print('----------------------------------------------------------------------------------')

        except sqlite3.Error as error:
            print('Error --->', error)
        
        finally:
            if(conn):
                conn.close()

    #Mostrar foto especifica por fecha desde la DB
    def getPhotobyDate(self):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('----------------------------------------------------------------------------------')
        print('Connected!')
        print('----------------------------------------------------------------------------------')
        try:
            fecha = input('Insert date: ')
            cursor = conn.execute("SELECT * FROM photo WHERE date=?", (fecha, ))
            data = cursor.fetchall()
            if len(data)>0 :
                [print(element) for element in data]
            else :
                print('Photo does not exists in DB')
        
        except sqlite3.Error as error:
            print('Error --->', error)
        
        finally:
            if(conn):
                conn.close()

##############################################################################
############################ MAIN ###########################################
#############################################################################
def seleccion():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input('Introduce opcion: '))
            correcto = True
        except ValueError:
            print('Opcion invalida')
    return num

def menu():
    test = DBServices()
    os.system('cls')
    exit = False
    op = 0
    while not exit:
        print('\n'+' ------ Astronomy Picture of the Day ------'+'\n')
        print('Selecciona una opcion')
        print('\t1 - Insertar fotografia en BD')
        print('\t2 - Mostrar lista de fotografias en BD')
        print('\t3 - Eliminar fotografia almacenada en BD')
        print('\t4 - Buscar fotografia por fecha')
        print('\t5 - Salir')

        op = seleccion()
        if op == 1:
            date = input('Insert date:')
            biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
            picture = getPicture(biblio.SearchPicture(date))
            print(picture)
            #print(getPicture(picture, biblio))
            test.savePhoto(picture)
        elif op == 2:
            test.getPhoto()
        elif op == 3:
            test.deletePhoto()
        elif op == 4:
            test.getPhotobyDate()
        elif op == 5:
            break
        else:
            print('Opcion Invalida')
            


if __name__== '__main__':
    print('ok')
    #menu()
    
    '''
        Probando funciones de interfaz api
    '''
    # date = input('Insert date:')
    #date = "2020-05-10"##formato
    # biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    #print(biblio)
    #print("*"*30)
    # b=biblio.SearchPicture(date)
    # picture =getPicture(date, biblio)
    #print(b)
    #print(getPicture(picture, biblio))
    '''
        Probando funciones de interfaz DB
    '''
    #test = DBServices()
    #test.savePhoto(picture)
    #test.getPhoto()
    #test.getPhotobyDate()
    #test.deletePhoto()