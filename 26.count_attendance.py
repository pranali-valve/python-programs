




attendance = ["P", "A", "P", "P", "A", "P"]

present = 0

for status in attendance:
    if status == "P":
        present += 1

print("Present:", present)