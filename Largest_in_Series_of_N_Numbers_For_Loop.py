n = int(input("Enter number of values: "))

largest = int(input("Enter a number: "))

for i in range(n - 1):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

print("Largest Number =", largest)