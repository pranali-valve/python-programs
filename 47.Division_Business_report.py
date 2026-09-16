


try:
    total_sales = 50000
    number_of_days = int(input("Enter number of days: "))

    average = total_sales / number_of_days

    print("Average daily sales:", average)

except ZeroDivisionError:
    print("Number of days cannot be zero")

except ValueError:
    print("Please enter a valid number")