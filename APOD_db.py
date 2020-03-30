import sqlite3
import os 

#CREAR BASE DE DATOS
try:
    con = sqlite3.connect('APOD.db')
    cursor = con.cursor()
    print('Conectado')
    
    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de Sqlite: ', rows)
    cursor.close()

except sqlite3.Error as error:
    print('No se puede realizar la conexion', error)
    
finally:
    if(con):
        con.close()
        print('Done')


