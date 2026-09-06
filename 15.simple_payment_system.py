

#concepts: variables, data types, operators, conditions, logical operators.

account_balance = 10000
payment_amount = 2500
payment_method = "UPI"

if payment_amount <= account_balance:
    
    if payment_method == "UPI" or payment_method == "Card":
        account_balance -= payment_amount
        print("Payment successful")
        print("Remaining balance:", account_balance)
    else:
        print("Invalid payment method")

else:
    print("Insufficient account balance")