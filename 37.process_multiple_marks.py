



def total_marks(*marks):
    total = 0

    for mark in marks:
        total += mark

    return total

print(total_marks(80, 75, 90, 85))