'''
Question-1: Creating a Basic Calculator
You are tasked with creating a simple calculator program that can perform addition, subtraction, multiplication, and division operations.
You need to create functions for each of these operations and allow the user to input two numbers and choose an operation to perform.

Requirements:
1. Create four functions: add, subtract, multiply, and divide. Each function should take two arguments
    (the two numbers to perform the operation on) and return the result of the operation.
2. Create a function named calculator that presents a menu to the user with options for each operation.
    The user should be able to input their choice, as well as the two numbers for the operation.
3. After performing the selected operation, display the result to the user.
'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice (1/2/3/4): "))
    if choice > 4 or choice < 1:
        print("Invalid choice")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(num1, " + ", num2, "=", result)
        elif choice == 2:
            result = subtract(num1, num2)
            print(num1, " - ", num2, "=", result)
        elif choice == 3:
            result = multiply(num1, num2)
            print(num1, " * ", num2, "=", result)
        else:
            result = divide(num1, num2)
            print(num1, " / ", num2, "=", result)

while True:
    print("-----Simple Calculator-----")
    calculator()

