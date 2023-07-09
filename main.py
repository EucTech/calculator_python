#!/c/Users/User/AppData/Local/Microsoft/WindowsApps/python3

from calculator import *
from math import sin, tan, cos
#if __name__ == "__main__":
try:
    number = input("Input: ")
    #loop through number and split it into substrings with "+"
    if "+" in number:
        number = [int(num) for num in number.split("+")]
        result = add(*number)
    elif "-" in number:
        number = [int(num) for num in number.split("-")]
        result = sub(*number)   
    elif "/" in number:
        number = [int(num) for num in number.split("/")]
        result = div(*number)
    elif "*" in number:
        number = [int(num) for num in number.split("*")]
        result = mul(*number)
    elif "sin" in number:
        number = float(number.replace("sin(", "").replace(")", ""))
        result = sine(number)

    elif "cos" in number:
        number = float(number.replace("cos(", "").replace(")", ""))
        result = cose(number)

    elif "tan" in number:
        number = float(number.replace("tan(", "").replace(")", ""))
        result = tang(number)
    
    elif "sqrt" in number:
        number = float(number.replace("sqrt(", "").replace(")", ""))
        result = square_root(number)

    
    #The *numbers syntax unpacks the elements of the numbers
    #list as separate arguments, allowing them to be
    #passed to the add() function correctly.
    print(result)
except (ValueError, TypeError):
    print("Incorrect Operation")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except NameError:
    print("Input numbers")