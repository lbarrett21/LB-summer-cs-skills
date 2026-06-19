#basic calculator 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    if(b == 0):
        return('Error: Cannot Divide By 0')
    return a/b
    
quit = False

print('Python Calculator')
print('------------------------')

while quit ==False:
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation not in ['+','-', '*','/']:
            print("Please enter a valid operation")
            continue

        num2 = float(input("Enter the second number: "))



        if(operation == '+'):
            result = add(num1, num2)
        elif(operation == '-'):
            result = subtract(num1, num2)
        elif(operation == '*'):
            result = multiply(num1, num2)
        elif(operation == '/'):
            result = divide(num1, num2)
        

        print(result)
        again = input("Do another calculation (Y/N): ")
        if again == "N" or again == "n":
            break

    except ValueError:
        print("Please enter a number.")
        continue
