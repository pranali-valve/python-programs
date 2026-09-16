



def check_stock(quantity):
    if quantity > 0:
        return "Product available"
    else:
        return "Out of stock"

print(check_stock(10))
print(check_stock(0))