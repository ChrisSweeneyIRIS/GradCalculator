

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    userInput = input ("Enter an operator: +, -, *, /     ")
    if userInput in ("+", "-", "*", "/"):
        firstNum = int(input("\nEnter the first number: "))
        secondNum = int(input("Enter the second number"))

        if userInput == "+" :
            print(firstNum, "+", secondNum, "=", add(firstNum, secondNum))

        if userInput == "-" :
            print(firstNum, "-", secondNum, "=", subtract(firstNum, secondNum))

        if userInput == "*" :
            print(firstNum, "*", secondNum, "=", multiply(firstNum, secondNum))

        if userInput == "/" :
            print(firstNum, "/", secondNum, "=", divide(firstNum, secondNum))