




employees = [101, 102, 103, 104]

search_id = int(input("Enter employee ID: "))

for employee in employees:
    if employee == search_id:
        print("Employee found")
        break
else:
    print("Employee not found")