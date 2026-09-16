


task = input("Enter a task: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("\nYour tasks:")

with open("tasks.txt", "r") as file:
    tasks = file.readlines()

for index, task in enumerate(tasks, start=1):
    print(index, task.strip())