students = {
    101: {
        "name": "Vaishali",
        "age": 18,
        "department": "CSE"
    },
    102: {
        "name": "Ravi",
        "age": 19,
        "department": "ECE"
    }
}

print("Student Records:")

for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Department:", details["department"])
    print()

students[103] = {
    "name": "Priya",
    "age": 18,
    "department": "IT"
}

students[101]["age"] = 19

print("Updated Student Records:", students)