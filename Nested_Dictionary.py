students = {
    "student1": {
        "name": "Vaishali",
        "age": 18,
        "department": "CSE"
    },
    "student2": {
        "name": "Ravi",
        "age": 19,
        "department": "ECE"
    }
}

print("Student Details:")

for key, value in students.items():
    print(key)
    for k, v in value.items():
        print(k, ":", v)

print("Student 1 Name:", students["student1"]["name"])