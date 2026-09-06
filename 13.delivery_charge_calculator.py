

#Concepts: conditions, arithmetic, comparisons.

order_value = 1200

if order_value >= 1000:
    delivery_charge = 0
else:
    delivery_charge = 50

final_amount = order_value + delivery_charge

print("Delivery charge:", delivery_charge)
print("Final amount:", final_amount)