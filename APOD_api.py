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

class DBServices():
    #Insertar datos desde API a DB
    def savePhoto(self, photo):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('Conectado')
        #Verificamos que la photo no exista en la base de datos
        cursor.execute('''SELECT date from photo WHERE date = "{}"'''.format(photo.date))
        #Guardamos el resultado de la consulta anterior en la variable count, puede contener una photo o None
        count = cursor.fetchone()

        if count is None:
            #Si el parametro es None se inserta la photo 
            param = {
                'DATE' : photo.date,
                'TITLE' : photo.title,
                'EXPLANATION' : photo.explanation,
                'URL' : photo.url,
                'MEDIA_TYPE': photo.media_type
            }

            try:
                cursor.execute("INSERT INTO photo(id, date, title, explanation, hdurl, media_type)VALUES(null, :DATE, :TITLE, :EXPLANATION, :URL, :MEDIA_TYPE);", param)
                conn.commit()
                print('Photo {} insertada con exito'.format(photo.date))
                cursor.close()

            except sqlite3.Error as error:
                print('Error en la conexion:', error)


if __name__== '__main__':
    date = input('Insert date:')
    biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    picture =getPicture(date, biblio)
    print(picture)
    #insert = picture['DATE'], picture['TITLE']
    #test = DBServices()
    #test.savePhoto(picture)


