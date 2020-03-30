import sqlite3

def main():
    con = sqlite3.connect('APOD.db')
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Track
    (date text,
    explanation Text,
    hdurl Text,
    mediaType Text,
    title Text
    )
    ''')
    
    con.commit()
    con.close()
    
if __name__ == '__main__':
    main()