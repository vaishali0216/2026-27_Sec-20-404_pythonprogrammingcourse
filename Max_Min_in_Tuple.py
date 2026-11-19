n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

t = tuple(lst)

maximum = max(t)
minimum = min(t)

print("Tuple:", t)
print("Maximum element:", maximum)
print("Minimum element:", minimum)