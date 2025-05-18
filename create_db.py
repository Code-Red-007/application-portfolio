import sqlite3

conn = sqlite3.connect('signup.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE subscribers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    message TEXT
)
''')

conn.commit()
conn.close()

print("Database created with message column.")
