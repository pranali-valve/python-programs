


correct_password = "python123"

try:
    password = input("Enter password: ")

    if password != correct_password:
        raise ValueError("Incorrect password")

    print("Login successful")

except ValueError as error:
    print("Login failed:", error)