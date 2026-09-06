

#concepts: Variables, Integers, Arithmetic, Comparison, nested if

units = 250

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity units:", units)
print("Electricity bill: ₹", bill)