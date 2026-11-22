def search_enquiry(name):
    students = ["Smita", "Priya", "Janvi", "Amit"]

    for student in students:
        if student == name:
            return "Enquiry Found"
    return "Enquiry Not Found"

result = search_enquiry("Smita")
print(result)