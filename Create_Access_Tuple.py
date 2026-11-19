n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

t = tuple(lst)

print("Tuple:", t)

print("First element:", t[0])
print("Last element:", t[-1])

print("Using positive indexing:")
for i in range(n):
    print(t[i])

print("Using negative indexing:")
for i in range(-1, -n-1, -1):
    print(t[i])

print("Tuple slicing:", t[1:4])