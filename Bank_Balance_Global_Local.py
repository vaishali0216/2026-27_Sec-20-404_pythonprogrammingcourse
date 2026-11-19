balance = 5000

def deposit():
    global balance
    amount = 2000
    balance = balance + amount

    print("Deposit Amount:", amount)
    print("Updated Balance:", balance)

deposit()

print("Final Bank Balance:", balance)