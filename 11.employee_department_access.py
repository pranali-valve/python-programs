

#Concepts: strings, variables, conditions, nested if.

department = "IT"
is_employee = True

if is_employee:
    if department == "IT":
        print("Access to IT systems granted")
    else:
        print("General employee access granted")
else:
    print("Access denied")