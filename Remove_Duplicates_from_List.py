n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("Original List:", lst)
print("List without duplicates:", unique)