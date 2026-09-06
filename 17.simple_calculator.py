

#concepts: Variables, Integers, Strings, Arithmetic, Comparison, nested if


num1 = 20
num2 = 10
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result:", result)