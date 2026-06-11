import sqlite3


DATABASE_NAME = 'many_to_many_demo.db'

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()\
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER,
                    grade TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    subject TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_teacher (
                    student_id INTEGER,
                    teacher_id INTEGER,
                    PRIMARY KEY (student_id, teacher_id),
                    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()    

def add_student(student_id, name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO students (id, name, age, grade)
                    VALUES (?, ?, ?, ?)''',
                        (student_id, name, age, grade)
                    )
    conn.commit()
    conn.close()    

def add_teacher(teacher_id, name, subject):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO teachers (id, name, subject)
                    VALUES (?, ?, ?)''',
                        (teacher_id, name, subject)
                    )
    conn.commit()
    conn.close()