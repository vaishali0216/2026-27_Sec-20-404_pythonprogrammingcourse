n = int(input("Enter number to skip: "))

for i in range(1, 11):
    if i == n:
        continue
    print(i)