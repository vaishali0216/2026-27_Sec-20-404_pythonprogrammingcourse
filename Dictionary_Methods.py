student = {
    "name": "Vaishali",
    "age": 18,
    "department": "CSE"
}

print("Original Dictionary:", student)

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Get Name:", student.get("name"))

student.update({"age": 19})
print("After Update:", student)

student.pop("age")
print("After Pop:", student)

print("Dictionary Length:", len(student))

student.clear()
print("After Clear:", student)