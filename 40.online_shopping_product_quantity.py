



stock = 10

try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if quantity > stock:
        raise ValueError("Not enough stock available")

    print("Order placed successfully")

except ValueError as error:
    print("Order failed:", error)