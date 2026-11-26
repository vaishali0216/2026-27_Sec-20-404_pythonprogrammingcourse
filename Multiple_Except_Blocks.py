try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Division =", result)

except ValueError:
    print("Error: Please enter valid numbers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except Exception:
    print("Error: Something went wrong")