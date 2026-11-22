def check_admission(marks):
    if marks >= 45:
        return "Eligible for Admission"
    else:
        return "Not Eligible for Admission"

result = check_admission(85)
print(result)