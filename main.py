from database import create_table
from student import Student
from student_service import add_student, view_students as get_all_students

create_table()
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        student = Student(
            student_id, 
            name, 
            age, 
            grade
        )
        add_student(student)
        print("Student added successfully!")
    elif choice == '2':
        students = get_all_students()
        print("\n--- Student List ---")
        for student in students:
            print(student)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")