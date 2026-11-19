name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Using f-string:")
print(f"My name is {name}, my age is {age}, and my marks are {marks}")

print("Using format() method:")
print("My name is {}, my age is {}, and my marks are {}".format(name, age, marks))

print("Using % formatting:")
print("My name is %s, my age is %d, and my marks are %.2f" % (name, age, marks))