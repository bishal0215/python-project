class Teacher:
    def __init__(self, teacher_id, name, age, subject, salary):
        self.teacher_id = teacher_id
        self.name = name
        self.age = age
        self.subject = subject
        self.salary = salary

    def to_list(self):
        return [self.teacher_id, self.name, self.age, self.subject, self.salary]

    def display(self):
        print(f"ID: {self.teacher_id}, Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Salary: {self.salary}")