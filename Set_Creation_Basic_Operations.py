set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(50)
print("After adding 50:", set1)

set1.remove(20)
print("After removing 20:", set1)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference:", set1.difference(set2))

value = int(input("Enter element to search: "))

if value in set1:
    print(value, "is present in set")
else:
    print(value, "is not present in set")

print("Length of Set 1:", len(set1))