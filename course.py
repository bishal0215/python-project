class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description

    def to_list(self):
        return [self.course_id, self.course_name, self.description]

    def display(self):
        print(f"Course id: {self.course_id}, Name: {self.course_name}, Description: {self.description}")