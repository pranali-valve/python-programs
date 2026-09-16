


try:
    units = int(input("Enter electricity units: "))

    if units < 0:
        raise ValueError("Units cannot be negative")

    bill = units * 8

    print("Electricity bill:", bill)

except ValueError as error:
    print("Invalid input:", error)