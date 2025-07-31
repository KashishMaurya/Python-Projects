def add(num1, num2) :
    return num1 + num2

def subtract(num1, num2) :
    return num1 - num2

def multiply(num1, num2) :
    return num1 * num2

def divide(num1, num2) :
    return num1 / num2


def calculator() :
    if opeartion == "+" :
        print(f"{num1} + {num2} = {add(num1, num2)}")
        return add(num1, num2)
    elif opeartion == "-" :
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
        return subtract(num1, num2)
    elif opeartion == "*" :
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
        return multiply(num1, num2)
    elif opeartion == "/" :
        print(f"{num1} / {num2} = {divide(num1, num2)}")
        return divide(num1, num2)
        
        
#main
num1 = float(input("Enter number 1 : "))
opeartion = input("Enter operation (+, -, *, /) : ")
num2 = float(input("Enter number 2 : "))

to_continue = True

while to_continue :
    prev_num = calculator()
    
    to_continue = input("Do you want to continue with the previous result? Type 'yes' or 'no' : ").lower()
    
    if to_continue == "yes" :
        num1 = prev_num
        opeartion = input("Enter operation (+, -, *, /) : ")
        num2 = float(input("Enter number 2 : "))
    else : 
        to_continue = False
        print("Thank you")
        
    