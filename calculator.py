# Simple Calculator

print("***SIMPLE CALCULATOR***")
number_one = float(input("Enter first number: ").strip())
number_two = float(input("Enter second number: ").strip())
operator = input("Enter operator ('+', '-', '/', 'X / */x'): ")

if operator == '+':
    print(f"{number_one} + {number_two} = {number_one + number_two}")
elif operator == '-':
    print(f"{number_one} - {number_two} = {number_one - number_two}")
elif operator == '/':
    if number_two == 0:
        print("Division by zero is not allowed")
    else:
        print(f"{number_one} / {number_two} = {number_one / number_two}")
elif operator == 'X' or operator == '*' or operator == 'x':
    print(f"{number_one} X {number_two} = {number_one * number_two}")
else:
    print("Invalid operator")