course_fee = float(input("Enter course fee: "))
discount = float(input("Enter discount percentage: "))
discount_amount = course_fee * discount / 100
final_fee = course_fee - discount_amount
print("Course Fee:", course_fee)
print("Discount:", discount_amount)
print("Final Fee:", final_fee)