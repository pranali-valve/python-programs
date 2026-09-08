




payments = ["success", "failed", "success", "success", "failed"]

count = 0

for payment in payments:
    if payment == "success":
        count += 1

print("Successful payments:", count)