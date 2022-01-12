def calctest():
    # take input from the user
    operator = input("Enter operator: (x, /, +, -)")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = calculate(operator,num1,num2)
    print(result)


def calculate(operator, num1, num2):
    if operator == 'x':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    elif operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    else: 
        print("operator not found!")
        quit()

    return(result)

