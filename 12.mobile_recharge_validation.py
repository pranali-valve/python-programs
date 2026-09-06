

#Concepts: nested conditions, arithmetic, comparisons.

balance = 250
recharge_amount = 199

if recharge_amount > 0:
    if recharge_amount <= balance:
        balance = balance - recharge_amount
        print("Recharge successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid recharge amount")