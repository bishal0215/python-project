import sqlite3

DATABASE_NAME = 'students.db'

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')

    # Teachers table (FIXED + salary included)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            subject TEXT,
            salary REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT
    )

   ''')

    conn.commit()
    conn.close()