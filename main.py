from fee import calculate_fee
from admission import check_admission
from payment import calculate_due
fee = calculate_fee(50000, 25)
admission = check_admission(25)
due = calculate_due(50000, 20000)
print("Course Fee:", fee)
print("Admission Status:", admission)
print("Payment Due:", due)