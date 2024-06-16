import sqlite3

def init_db():
    db = sqlite3.connect('guestbook.db')
    cursor = db.cursor()
        
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            message TEXT NOT NULL
    )''')
    db.commit()

    print("DB successfully created")

init_db()


