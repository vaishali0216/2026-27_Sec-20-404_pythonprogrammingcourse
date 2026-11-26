while True:
    try:
        num = int(input("Enter a positive number: "))

        if num <= 0:
            print("Error: Number must be positive")
            continue

        print("Valid number:", num)
        break

    except ValueError:
        print("Error: Please enter a valid integer")