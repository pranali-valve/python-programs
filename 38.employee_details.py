



def employee_details(**details):
    for key, value in details.items():
        print(key, ":", value)

employee_details(
    name="Pranali",
    department="Data",
    experience=2
)