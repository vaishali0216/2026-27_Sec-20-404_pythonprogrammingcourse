s = {10, 20, 30, 40}

print("Original Set:", s)

value = int(input("Enter element to search: "))

if value in s:
    print(value, "is present in set")
else:
    print(value, "is not present in set")

if 50 not in s:
    print("50 is not present in set")

s.add(50)
print("After add():", s)

s.update([60, 70])
print("After update():", s)

s.remove(20)
print("After remove():", s)

s.discard(100)
print("After discard():", s)

s.pop()
print("After pop():", s)

print("Length of set:", len(s))

s.clear()
print("After clear():", s)