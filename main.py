from database import create_table
from student import Student
from teacher import Teacher
from student_service import add_student, view_students as get_all_students
from teacher_service import add_teacher, view_teachers as get_all_teachers

create_table()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Teacher")
    print("4. View Teachers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student = Student(
            int(input("Enter student ID: ")),
            input("Enter student name: "),
            int(input("Enter student age: ")),
            input("Enter student grade: ")
        )
        add_student(student)
        print("Student added successfully!")

    elif choice == '2':
        for student in get_all_students():
            print(student)

    elif choice == '3':
        teacher = Teacher(
            int(input("Enter teacher ID: ")),
            input("Enter teacher name: "),
            int(input("Enter teacher age: ")),
            input("Enter teacher subject: "),
            float(input("Enter teacher salary: "))
        )
        add_teacher(teacher)
        print("Teacher added successfully!")

    elif choice == '4':
        for teacher in get_all_teachers():
            print(teacher)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")