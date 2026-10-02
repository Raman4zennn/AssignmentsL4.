# Number Analyzer
# Ask the user to enter an integer.
# Your program must determine:
# Whether the number is positive, negative, or zero.
# Whether it is even or odd.
# Whether it is divisible by 3.
# Whether it is divisible by 5.
# Whether it is divisible by both 3 and 5.
# Display the results clearly using f-strings.
# Hint: Use %, if-elif-else, and.

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