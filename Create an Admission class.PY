class Admission:
    def __init__(self, student_name, course_name):
        self.student_name = student_name
        self.course_name = course_name

    def display(self):
        print("Student Name:", self.student_name)
        print("Course Name:", self.course_name)
        print("Admission Successful")
admission1 = Admission("Janvi", "Python")
admission1.display()