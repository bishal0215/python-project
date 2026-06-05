from database import get_connection

def add_course(course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO courses (id, name, description)
        VALUES (?, ?, ?)
    ''', (
        course.course_id,
        course.name,
        course.description
    ))

    conn.commit()
    conn.close()


def view_courses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    conn.close()
    return rows
