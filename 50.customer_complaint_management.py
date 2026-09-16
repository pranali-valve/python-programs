



customer_name = input("Enter customer name: ")
complaint = input("Enter complaint: ")

with open("complaints.txt", "a") as file:
    file.write(f"Customer: {customer_name}\n")
    file.write(f"Complaint: {complaint}\n")
    file.write("-" * 30 + "\n")

print("Complaint registered successfully")