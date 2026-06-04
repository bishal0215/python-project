class teacher:
    def __init__(self, teacher_id,name,age,subject):
        self.teacher_id = teacher_id
        self.name = name
        self.age = age
        self.subject = subject
    def to_list(self):
        return[self.teacher_id,self.name,self.age,self.subject]
    
    def display(self):
        print(f"Teacher id: {self.teacher_id},name:{self.name},age:{self.age},grade:{self.subject}")
'''t1= teacher(1,"Rishi",20,"python")

teacher_data= t1.to_list()
print(teacher_data)'''