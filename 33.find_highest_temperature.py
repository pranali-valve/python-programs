



def highest_temperature(temperatures):
    highest = temperatures[0]

    for temp in temperatures:
        if temp > highest:
            highest = temp

    return highest

print(highest_temperature([28, 32, 25, 35, 30]))