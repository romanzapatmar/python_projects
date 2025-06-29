# Project Name : Calculator in Python
# Author : Roman Zapatmar
# Date : 06 June 2025

while True:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    operator = input("Enter the operator (+, -, *, /) : ")
    if(operator == "+"):
        print("Result : ",num1 + num2)
    elif(operator == "-"):
        print("Result : ",num1 - num2)
    elif(operator == "*"):
        print("Result : ",num1 * num2)
    elif(operator == "/"):
        print("Result : ",num1 / num2)
    else:
        print("Invalid operator")
        continue

    # Ask if user wants to calculate again
    choice = input("Do you want to calculate again? (yes/no): ").lower() #added a lower() to make it case insensitive
    if choice != 'yes':
        print("Thanks for using the calculator. Goodbye!")
        break

