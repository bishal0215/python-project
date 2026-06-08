from database import get_connection

def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO STUDENTS
                    VALUES (?, ?, ?, ?)''',
                        (student.student_id,
                        student.name,
                        student.age,
                        student.grade)
                   )
    conn.commit()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

def update_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    UPDATE students
                    SET name = ?, age = ?, grade = ?
                    WHERE id = ?''',
                        (student.name,
                        student.age,
                        student.grade,
                        student.student_id)
                   )
    conn.commit()
    conn.close()
    
    update_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return update_rows