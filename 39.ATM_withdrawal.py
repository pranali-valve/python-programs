


balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as error:
    print("Transaction failed:", error)