students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Anu", "marks": 95},
    {"name": "Kiran", "marks": 75},
    {"name": "Sita", "marks": 90}
]

students.sort(key=lambda x: x["marks"])

print("Sorted List of Dictionaries:")

for student in students:
    print(student)