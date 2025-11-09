name = "FaliOS"

import random
def calculator():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    operator = input("Operator (+, -, *, /): ")
    if operator == "+":
        print(f"{num1} {operator} {num2} = {num1 + num2}")
        calculator()
    elif operator == "-":
        print(f"{num1} {operator} {num2} = {num1 - num2}")
        calculator()
    elif operator == "*":
        print(f"{num1} {operator} {num2} = {num1 * num2}")
        calculator()
    elif num2 == 0 and operator == "/":
        print("0 division")
        calculator()
    elif operator == "/":
        print(f"{num1} {operator} {num2} = {num1 / num2}")
        calculator()
def game():
    start = int(input("Starting number: "))
    end = int(input("Ending number: "))
    number = random.randint(start,end)
    numberguess = int(input("Guess the number: "))
    if numberguess == number:
        print("You have guessed the number!\n")
        game()
    else:
        print(f"Failed to guess number! It was {number}\n")
        game()
def menu():
    app = int(input(f"{name}\n\n1. Calculator\n2. Guess it!\n"))
    if app == 1:
        calculator()
    elif app == 2:
        game()
    else:
        print(f"Unknown app with ID {app}!\n")
        menu()
menu()