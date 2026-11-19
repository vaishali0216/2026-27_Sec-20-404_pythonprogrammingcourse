def shopping_cart(**kwargs):
    total = 0

    print("Shopping Cart Details:")

    for item, price in kwargs.items():
        print(item, ":", price)
        total = total + price

    print("Total Amount:", total)


shopping_cart(
    Apple=50,
    Banana=30,
    Mango=60,
    Orange=40
)