


try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError as error:
    with open("error_log.txt", "a") as file:
        file.write(f"ValueError: {error}\n")

    print("Please enter a valid number")

except ZeroDivisionError as error:
    with open("error_log.txt", "a") as file:
        file.write(f"ZeroDivisionError: {error}\n")

    print("Number cannot be zero")