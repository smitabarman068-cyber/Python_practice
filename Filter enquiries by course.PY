students = [
    {"name": "Smita", "course": "Python"},
    {"name": "Pranay", "course": "Java"},
    {"name": "Dimpi", "course": "Python"},
    {"name": "Janvi", "course": "HTML"},
    {"name": "Namrata", "course": "Java"}
]
for student in students:
    if student["course"] == "HTML":
        print(student["name"])