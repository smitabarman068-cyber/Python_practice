students = [
    {"name": "Janvi", "mobile": "6900211141", "course": "Python"},
    {"name": "Smita", "mobile": "6900971802", "course": "Java"},
    {"name": "Dimpi", "mobile": "9707887559", "course": "HTML"}
]
mobile = input("Enter mobile number: ")
for student in students:
    if student["mobile"] == mobile:
        print("Student Found")
        print("Name:", student["name"])
        print("Course:", student["course"])
        break
else:
    print("Student Not Found")