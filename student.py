'''
students=[]
for i in range(2):
    
    
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (dd/mm/yy): ")
    address = input("Enter your address: ")
    contact_no = input("Enter your contact number: ")
    

    print("\n--- Summary ---")
    student_info = {
        'name':name,
        'dob' : dob,
        'contact_no':contact_no,
        'adress':address
    }
    students.append(student_info)
print(students)
print("\nstudent information:")
for student in students:
    print(f"name: {student['name']},\ndate of birth:{student['dob']},\ncontact_no:{contact_no}")
print("\nData entry complete.")
'''
class Student:
    def __init__(self,student_id,name,age,grade,teacher_id):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.teacher_id = teacher_id
    def to_list(self):
        return[self.student_id,self.name,self.age,self.grade,self.teacher_id]

    def display(self):
        print(f"student id: {self.student_id},name:{self.name},age:{self.age},grade:{self.grade},teacher id:{self.teacher_id}")
        
'''s1= student(1,"alice",20,"A",1)
s2= student(2,"Bob",21,"B")
student_data= s1.to_list()
print(student_data)

print(s1.student_id)
print(s1.name)
print(s1.age)

print(s2.student_id)
print(s2.name)
print(s2.age)
'''
    
