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
    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, grade)
            )
    conn.commit()
    conn.close()    

def add_teacher(teacher_id, name, subject):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO teachers VALUES (?, ?, ?)",
        (teacher_id, name, subject)
            )
    conn.commit()
    conn.close()
def assign_teacher_to_student(student_id, teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO student_teacher VALUES (?, ?)",
        (student_id, teacher_id)
            )
    conn.commit()
    conn.close()
def view_students_with_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            students.id,
            students.name,
            students.age,
            students.grade,
            teachers.name,
            teachers.subject,
           
        FROM students_teachers
        JOIN students ON student_teacher.student_id = students.id
        JOIN teachers ON student_teacher.teacher_id = teachers.id
        ORDER BY students.id, teachers.id
                   
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_teachers_with_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            teachers.id,
            teachers.name,
            teachers.subject,
            students.name,
            students.grade
        FROM student_teacher
        JOIN teachers ON student_teacher.teacher_id = teachers.id
        JOIN students ON student_teacher.student_id = students.id
        ORDER BY teachers.id, students.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows
def main():
    create_tables()
    
    while True:
        print("\nMany-to many student teacher system")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Assign Teacher to Student")
        print("4. View Students with Teachers")
        print("5. View Teachers with Students")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(student_id, name, age, grade)
            print("Student added successfully.")
        elif choice == '2':
            teacher_id = int(input("Enter teacher ID: "))
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")

            add_teacher(teacher_id, name, subject)
            print("Teacher added successfully.")
        elif choice == '3': 
            student_id = int(input("Enter student ID: "))
            teacher_id = int(input("Enter teacher ID: "))
            assign_teacher_to_student(student_id, teacher_id)
            print("Teacher assigned to student successfully.")
            
        elif choice == '4':
            students_with_teachers = view_students_with_teachers()
            print("\nStudents with Teachers:")
            for row in students_with_teachers:
                print(f"Student: {row[1]}, Age: {row[2]}, Grade: {row[3]}, Teacher: {row[4]}, Subject: {row[5]}")
        
        elif choice == '5':
            teachers_with_students = view_teachers_with_students()
            print("\nTeachers with Students:")
            for row in teachers_with_students:
                print(
                    f"Teacher ID: {teacher_id}, Teacher: {name},"
                    f"Subject: {subject}, Student: {name}, Grade: {grade}"
                )
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":    
    main()
            