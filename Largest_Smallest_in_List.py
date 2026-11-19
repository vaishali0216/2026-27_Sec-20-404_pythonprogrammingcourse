n = int(input("Enter number of elements: "))

my_list = []

for i in range(n):
    value = int(input("Enter element: "))
    my_list.append(value)

largest = max(my_list)
smallest = min(my_list)

print("List:", my_list)
print("Largest Element:", largest)
print("Smallest Element:", smallest)