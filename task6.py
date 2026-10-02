# 6. Shopping Discount Calculator
# Create a shopping program that asks for:
#  Customer name
#  Product price
#  Quantity
#  Membership status (yes/no)
# Calculate:
# Subtotal = price × quantity
# Apply discounts:
#  Subtotal ≥ Rs. 10,000 → 15%
#  Subtotal ≥ Rs. 5,000 → 10%
#  Subtotal ≥ Rs. 2,000 → 5%
#  Otherwise → No discount
# If the customer is a member and subtotal is at least Rs. 5,000, give an additional
# 5% discount.
# Display:
#  Customer name
#  Subtotal
#  Discount
#  Final amount
# Use f-strings.


username = input("Enter username: ")
password = input("Enter password: ")

role = None
if username == "admin":
	if password == "admin123":
		role = "Administrator"
elif username == "student12":
	if password == "study123":
		role = "Student"

if role is None:
	print("Invalid username or password")
else:
	print(f"Role: {role}")
	if role == "Administrator":
		print("Full system access")
	elif role == "Teacher":
		print("Teacher access")

