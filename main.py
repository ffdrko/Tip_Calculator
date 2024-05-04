print("----- Welcome to tip calculator -----")
user_bill = float(input("Please enter the total bill: "))
user_tip = float(input("Enter your tip percentage: "))
user_count = int(input("How many people to split the bill: "))

tip_as_percentage = user_tip/100
total_tip = user_bill * tip_as_percentage
total_bill = total_tip + user_bill
per_head_amount = total_bill / user_count

print("----- BILL -----")
print(f"Each person will pay {per_head_amount:.2f}")