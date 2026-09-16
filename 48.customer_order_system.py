


product_price = 500
stock = 5

try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise ValueError("Invalid quantity")

    if quantity > stock:
        raise ValueError("Product out of stock")

    total = product_price * quantity

    print("Order successful")
    print("Total amount:", total)

except ValueError as error:
    print("Order failed:", error)

finally:
    print("Thank you for shopping")