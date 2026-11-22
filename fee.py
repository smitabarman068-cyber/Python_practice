def calculate_fee(course_fee, discount):
    discount_amount = course_fee * discount / 100
    final_fee = course_fee - discount_amount
    return final_fee