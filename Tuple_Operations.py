t1 = (10, 20, 30, 20, 40)
t2 = (50, 60, 70)

print("Tuple 1:", t1)
print("Tuple 2:", t2)

print("Concatenation:", t1 + t2)

print("Repetition:", t1 * 2)

print("Length of Tuple 1:", len(t1))

print("Count of 20:", t1.count(20))

print("Index of 30:", t1.index(30))

value = int(input("Enter element to search: "))

if value in t1:
    print(value, "is present in tuple")
else:
    print(value, "is not present in tuple")

print("Maximum element:", max(t1))
print("Minimum element:", min(t1))