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
    #info =[]
    #info.append(params)
    return apod.date, apod.title, apod.explanation, apod.url, apod.media_type
    #return apod.date, apod.title, apod.explanation, apod.url, apod.media_type

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
    def savePhoto(self, photo):
        #Conexion a la DB
        conn = sqlite3.connect('APOD.db')
        cursor = conn.cursor()
        print('----------------------------------------------------------------------------------')
        print('Conectado!')
        try:
            cursor.execute("INSERT INTO photo(date, title, explanation, hdurl, mediaType) VALUES (?,?,?,?,?)",(photo[0],photo[1],photo[2],photo[3],photo[4]))
            conn.commit()
            print('----------------------------------------------------------------------------------')
            print('Foto insertada con exito!')
            cursor.close()

        except sqlite3.Error as error:
            print('Error --->', error)
        finally:
            if(conn):
                conn.close()


if __name__== '__main__':
    date = input('Insert date:')
    biblio = Nasa('https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP') #URL para hacer el request
    picture =getPicture(date, biblio)
    #print(picture)

    test = DBServices()
    test.savePhoto(picture)


