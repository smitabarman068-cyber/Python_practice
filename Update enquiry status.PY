students = [
    {"name": "Gungun", "mobile": "8822578899", "status": "Pending"},
    {"name": "Pallabi", "mobile": "9876543211", "status": "Pending"}
]
mobile = input("Enter mobile number: ")
for student in students:
    if student["mobile"] == mobile:
        student["status"] = "Approved"
        print("Status Updated Successfully")
        print(student)
        break
else:
    print("Student Not Found")