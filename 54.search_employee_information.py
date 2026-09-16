


search_name = input("Enter employee name to search: ")

with open("employees.txt", "r") as file:
    employees = file.readlines()

found = False

for employee in employees:
    if search_name.lower() in employee.lower():
        print("Employee found:", employee.strip())
        found = True

if not found:
    print("Employee not found")