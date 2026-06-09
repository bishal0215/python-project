from database import create_table
from student import Student
from teacher import Teacher
from course import Course
from course_service import add_course, view_courses as get_all_courses
from student_service import add_student, delete_student, update_student, view_students as get_all_students
from teacher_service import add_teacher, delete_teacher, update_teacher, view_teachers as get_all_teachers

create_table()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Teacher")
    print("4. View Teachers")
    print("5. Add Course")
    print("6. View Courses")
    print("7. Update Teacher")
    print("8. Update Student")
    print("9. Delete Teacher")
    print("10. Delete Student")
    print("11. Exit")

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
        course = Course(
            int(input("Enter course ID: ")),
            input("Enter course name: "),
            input("Enter course description: ")
        )
        add_course(course)
        print("Course added successfully!")
    elif choice == '6':
        courses = get_all_courses()
        print("\n--- Course List ---")
        for course in courses:
            print(course)

    elif choice == '7':
        teacher_id = int(input("Enter teacher ID to update: "))
        name = input("new name:")
        subject = input("new subject:")

        age = int(input("new age:"))
        salary = float(input("new salary:"))
        teacher = Teacher(teacher_id, name, age, subject, salary)
        update_rows = update_teacher(teacher)
        if update_rows :
            print("Teacher updated successfully!")
        else:
            print("no teacher found with that id")

    elif choice == '8':
        student_id = int(input("Enter student ID to update: "))
        name = input("new name:")
        age = int(input("new age:"))
        grade = input("new grade:")
        student = Student(student_id, name, age, grade)
        update_rows = update_student(student)
        if update_rows:
            print("Student updated successfully!")
        else:
            print("Failed to update student.")
    elif choice == '9':
        teacher_id = int(input("Enter teacher ID to delete: "))
        delete_rows = delete_teacher(teacher_id)
        if delete_rows:
            print("Teacher deleted successfully!")
        else:
            print("Failed to delete teacher.")
            
    elif choice == '10':
        student_id = int(input("Enter student ID to delete: "))
        delete_rows = delete_student(student_id)
        if delete_rows:
            print("Student deleted successfully!")
        else:
            print("Failed to delete student.")
    elif choice == '11':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")