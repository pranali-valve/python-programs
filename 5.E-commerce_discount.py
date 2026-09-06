

#Concepts: int, comparison operators, conditions.

cart_value = 3500

if cart_value >= 5000:
    discount = 20
elif cart_value >= 3000:
    discount = 10
else:
    discount = 0

final_price = cart_value - (cart_value * discount / 100)

print("Discount:", discount, "%")
print("Final price:", final_price)