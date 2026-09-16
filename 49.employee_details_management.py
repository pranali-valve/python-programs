



name = input("Enter employee name: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

with open("employees.txt", "a") as file:
    file.write(f"{name}, {department}, {salary}\n")

print("Employee details saved successfully")