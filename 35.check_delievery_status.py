



def delivery_status(status):
    if status == "delivered":
        return "Order completed"
    elif status == "shipped":
        return "Order on the way"
    else:
        return "Order processing"

print(delivery_status("shipped"))