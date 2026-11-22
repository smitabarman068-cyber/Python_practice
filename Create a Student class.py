class Student:
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

student1 = Student("Dimpi", 26, "9854249610")
student1.display()