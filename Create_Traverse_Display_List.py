n = int(input("Enter number of elements: "))

my_list = []

for i in range(n):
    value = input("Enter element: ")
    my_list.append(value)

print("Created List:", my_list)

print("List Elements:")

for item in my_list:
    print(item)