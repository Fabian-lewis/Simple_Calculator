# Simple Calculator

print("***SIMPLE CALCULATOR***")
number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
operator = input("Enter operator ('+', '-', '/', 'X / */x'): ")

if operator == '+':
    print(f"{number_one} + {number_two} = {number_one + number_two}")
elif operator == '-':
    print(f"{number_one} - {number_two} = {number_one - number_two}")
elif operator == '/':
    print(f"{number_one} / {number_two} = {number_one / number_two}")
elif operator == 'X' or operator == '*' or operator == 'x':
    print(f"{number_one} X {number_two} = {number_one * number_two}")
else:
    print("Invalid operator")