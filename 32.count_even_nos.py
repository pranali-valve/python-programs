



def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

print(count_even([10, 15, 20, 25, 30]))