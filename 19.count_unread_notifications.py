




notifications = [1, 0, 1, 1, 0, 1]

count = 0

for notification in notifications:
    if notification == 1:
        count += 1

print("Unread notifications:", count)