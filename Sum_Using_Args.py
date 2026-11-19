def calculate_sum(*args):
    total = 0

    for i in args:
        total = total + i

    return total

result = calculate_sum(10, 20, 30, 40, 50)

print("Numbers: 10, 20, 30, 40, 50")
print("Sum of Numbers:", result)