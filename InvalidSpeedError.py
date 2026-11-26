class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter vehicle speed: "))

    if speed < 0 or speed > 200:
        raise InvalidSpeedError("Invalid speed!")

    print("Valid speed:", speed)

except InvalidSpeedError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid number")