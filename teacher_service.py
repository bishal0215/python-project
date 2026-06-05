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