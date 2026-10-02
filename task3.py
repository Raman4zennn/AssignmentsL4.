# 3. Electricity Bill Calculator
# Create a program that asks the user for the number of electricity units consumed.
# Calculate the bill according to:

# Units Rate
# First 20 units Rs. 5/unit
# Next 30 units Rs. 7/unit

# Next 50 units Rs.
# 10/unit

# Above 100
# units

# Rs.
# 12/unit

# Use if-elif-else to calculate the bill.
# Also display:
#  Units consumed
#  Total bill
# using f-strings.
# Challenge: Make sure the calculation is based on the different slabs rather than
# applying one rate to all units.

units = int(input("Enter the number of electricity units consumed: "))

if units <= 20:
	bill = units * 5
elif units <= 50:
	bill = (20 * 5) + ((units - 20) * 7)
elif units <= 100:
	bill = (20 * 5) + (30 * 7) + ((units - 50) * 10)
else:
	bill = (20 * 5) + (30 * 7) + (50 * 10) + ((units - 100) * 12)

print(f"Units consumed: {units}")
print(f"Total bill: Rs. {bill}")
