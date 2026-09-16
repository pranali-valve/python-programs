


try:
    file = open("employee.txt", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("Employee file not found")

finally:
    print("File operation completed")