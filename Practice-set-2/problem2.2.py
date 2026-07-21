# 2 - Write a program using match case that simulates a simple calculator.

'''
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case.
'''

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your Second number: "))

operator = input("choose any operator: ")

match operator:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "/":
        print(num1 / num2)

    case "*":
        print(num1 * num2)

    case "//":
        print(num1 // num2)

    case "**":
        print(num1 ** num2)

    case "%":
        print(num1 % num2)