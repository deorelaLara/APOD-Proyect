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

def getPicture(date, bibliotec):
    apod = bibliotec.SearchPicture(date)
    params = {
        'date' : apod.date,
        'title' : apod.title,
        'explanation' : apod.explanation,
        'url' : apod.url,
        'media-type' : apod.media_type
    }
    return params

class Nasa(BiblioAPOD):
    def __init__(self, url_base):
        self.url = url_base
    
    def SearchPicture(self, date):
        res = requests.get('{}&date={}'.format(self.url, date))
        data = res.json()
        return Photo(data['date'] ,data['title'], data['explanation'], data['url'], data['media_type'])


##############################################################################
################## IMPLEMENTACION INTERFAZ DB ###############################
#############################################################################

class DBServices(DBService):



    #Insertar datos desde API a DB
    def savePhoto(self, Photo):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('Conectado')
        try:
            querito = f"""
                INSERT INTO photo (date, title, explanation, url, media_type)
                VALUES ('{Photo['date']}', '{Photo['title']}', '{Photo['explanation']}', '{Photo['url']}', '{Photo['media_type']}')
                """

            #queryto = '''INSERT INTO photo VALUES
            #           ('{}', '{}', '{}', '{}', '{}')'''.format(Photo.date, Photo.title, Photo.explanation, Photo.url, Photo.media_type)
            resultado = cursor.execute(querito)
            conn.commit()
            print('Inf insertada con exito', resultado)
            cursor.close()

        except sqlite3.Error as error:
            print('Error --->', error)
        finally:
            if(conn):
                conn.close()



if __name__== '__main__':
    
    date = input('Insert date:')
    biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    picture = getPicture(date, biblio)
    print(picture)
    print('---------------------------------------------------------------------------------------------')
    #insert = picture['DATE'], picture['TITLE']
    #test = DBServices()
    #test.savePhoto(getPicture(date, biblio))

