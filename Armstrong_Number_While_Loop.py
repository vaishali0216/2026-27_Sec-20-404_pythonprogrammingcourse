n = int(input("Enter a number: "))

temp = n
count = 0
total = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

temp = n

while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")