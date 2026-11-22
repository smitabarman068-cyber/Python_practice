class Course:
    def __init__(self, course_name, fee):
        self.course_name = course_name
        self.fee = fee
    def display(self):
        print("Course Name:", self.course_name)
        print("Course Fee:", self.fee)
course1 = Course("AI/ML", 50000)
course1.display()