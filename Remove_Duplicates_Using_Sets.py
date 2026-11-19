n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

print("Original List:", lst)

s = set(lst)

unique = list(s)

print("Set after removing duplicates:", s)
print("List without duplicates:", unique)