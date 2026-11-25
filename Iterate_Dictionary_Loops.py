student = {
    "name": "Vaishali",
    "age": 18,
    "department": "CSE",
    "college": "NRI University"
}

print("Dictionary Keys:")
for key in student:
    print(key)

print("Dictionary Values:")
for value in student.values():
    print(value)

print("Dictionary Items:")
for key, value in student.items():
    print(key, ":", value)