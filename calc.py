# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("Enter: x, +, - or /")


while True:
    # take input from the user
    operator = input("Enter operator: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # check if choice is one of the four options
    if operator in ('x', '+', '-', '/'):

        if operator == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operator == 'x':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")