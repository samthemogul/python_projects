import sqlite3

DATABASE = 'guestbook.db'

def seed_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Sample data
    # entries = [
    #     ("Alice", "alice@example.com", "I am satisfied with your service"),
    # ]
    cursor.execute('INSERT INTO guests (name, email, message) VALUES ("Alice", "alice@example.com", "I am satisfied with your service")')

    # cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)
    conn.commit()
    conn.close()

    print("Database seeded successfully!")

seed_db()