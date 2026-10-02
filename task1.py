# 1. Student Result Analyzer
# Create a Python program that accepts a student&#39;s:
#  Name
#  Marks in 3 subjects
# Calculate:
#  Total marks
#  Average marks
#  Highest mark
#  Lowest mark
# Use if-elif-else to assign:
#  A+ → Average ≥ 90
#  A → Average ≥ 80
#  B → Average ≥ 70
#  C → Average ≥ 60
#  D → Average ≥ 40
#  F → Below 40
# Display all information using f-strings.

name = input("Enter student's name: ")
marks = [
	float(input(f"Enter marks for subject {subject}: "))
	for subject in range(1, 4)
]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

if average >= 90:
	grade = "A+"
elif average >= 80:
	grade = "A"
elif average >= 70:
	grade = "B"
elif average >= 60:
	grade = "C"
elif average >= 40:
	grade = "D"
else:
	grade = "F"

print(f"\nStudent: {name}")
print(f"Total marks: {total}")
print(f"Average marks: {average:.2f}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
print(f"Grade: {grade}")

