


username = input("Enter username: ")

with open("login_log.txt", "a") as file:
    file.write(f"{username} logged in successfully\n")

print("Login activity recorded")