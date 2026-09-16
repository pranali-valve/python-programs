


name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("marks_report.txt", "w") as file:
    file.write(f"Student Name: {name}\n")
    file.write(f"Marks: {marks}\n")

with open("marks_report.txt", "r") as file:
    report = file.read()

print("\nStudent Report")
print(report)