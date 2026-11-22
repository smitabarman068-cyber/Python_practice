class Course:
    course_name = "Python"
    fee = 20000

    @classmethod
    def calculate_fee(cls, discount):
        discount_amount = cls.fee * discount / 100
        final_fee = cls.fee - discount_amount
        print("Course Name:", cls.course_name)
        print("Original Fee:", cls.fee)
        print("Discount Amount:", discount_amount)
        print("Final Fee:", final_fee)

Course.calculate_fee(10)