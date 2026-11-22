def calculate_payment_due(total_fee, paid_amount):
    payment_due = total_fee - paid_amount
    return payment_due

result = calculate_payment_due(50000, 20000)
print("Payment Due:", result)