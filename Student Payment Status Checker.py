total_fee = 50000
paid_amount = float(input("Enter paid amount: "))
if paid_amount == total_fee:
    print("Payment Status: Paid")
elif paid_amount > 0 and paid_amount < total_fee:
    print("Payment Status: Partial Payment")
elif paid_amount == 0:
    print("Payment Status: Pending")
else:
    print("Invalid Payment Amount")