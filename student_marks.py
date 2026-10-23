students = {
    "Ravi": 85,
    "Sneha": 92,
    "Priya": 78,
    "Kiran": 88
}

print("STUDENT MARKS ANALYSIS")
print("----------------------")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

topper = max(students, key=students.get)

print("----------------------")
print("Average Marks:", average)
print("Topper:", topper)
print("Highest Marks:", students[topper])
