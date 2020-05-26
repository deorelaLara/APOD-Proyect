import sqlite3
import os 
import DB_Abs
import Photo


class DBServices():

    #Insertar datos desde API a DB
    def savePhoto(self, Photo):
        try:
            conn = sqlite3.connect('APOD.db')
            cursor = conn.cursor()
            print('Conectado')

            query = '''INSERT INTO photo VALUES
                    ('{}', '{}', '{}', '{}', '{}')'''.format(Photo.Title, Photo.Url, Photo.Explanation, Photo.Date, Photo.Media_type)
            resultado = cursor.execute(query)
            conn.commit()
            print('Datos insertados correctamente', resultado)
            cursor.close()
            
        except sqlite3.Error as error:
            print('Error en la conexion:', error)

        finally:
            if(conn):
                conn.close()

if __name__ == "__main__":
    test = DBServices()
    test.savePhoto()

