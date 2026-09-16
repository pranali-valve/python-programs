


try:
    salary = float(input("Enter employee salary: "))

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    print("Salary:", salary)

except ValueError as error:
    print("Invalid salary:", error)