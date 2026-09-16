


product = input("Enter product name: ")
quantity = input("Enter available quantity: ")

with open("inventory.txt", "a") as file:
    file.write(f"Product: {product}, Stock: {quantity}\n")

print("Inventory updated")