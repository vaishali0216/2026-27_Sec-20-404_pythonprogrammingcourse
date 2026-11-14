a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        print("A is Smallest")
    else:
        print("C is Smallest")
else:
    if b < c:
        print("B is Smallest")
    else:
        print("C is Smallest")