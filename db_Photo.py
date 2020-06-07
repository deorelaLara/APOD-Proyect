import sqlite3

#Crea y conéctate a la BD
conn = sqlite3.connect('APOD.db')
cur = conn.cursor()
#print('DB...')

def main():
    #Crea la tabla si no existe
    cur.execute(
		'''
			CREATE TABLE IF NOT EXISTS photo (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				date TEXT(50),
				title VARCHAR(200),
				explanation VARCHAR(3000),
                hdurl VARCHAR(200),
				mediaType VARCHAR(350)
			);
		'''
	);
    #print('ok...')
    # Salva los cambios
    conn.commit()
    # Cierra la conexion
    conn.close()

if __name__ == '__main__':
	print(':lol:')
	main()