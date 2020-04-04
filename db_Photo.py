import sqlite3

def main():
    con = sqlite3.connect('APOD.db')
    cur = con.cursor()
    
    if cur.execute('''CREATE TABLE IF NOT EXISTS Photo(
        date text,
        explanation Text,
        hdurl Text,
        mediaType Text,
        title Text
        )'''):
        
        return 'Tabla creada con exito'
    else:
        return 'Error al crear la tabla'
    
    con.commit()
    con.close()
    
if __name__ == '__main__':
    main()