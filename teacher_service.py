from database import get_connection

def add_teacher(teacher):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO teachers (name, age, subject, salary)
        VALUES (?, ?, ?, ?)
    ''', (
        teacher.name,
        teacher.age,
        teacher.subject,
        teacher.salary
    ))

    conn.commit()
    conn.close()


def view_teachers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_teacher(teacher):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE teachers
        SET name = ?, age = ?, subject = ?, salary = ?
        WHERE id = ?
    ''', (
        teacher.name,
        teacher.age,
        teacher.subject,
        teacher.salary,
        teacher.teacher_id
    ))
    update_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return update_rows
def delete_teacher(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))
    delete_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return delete_rows


    