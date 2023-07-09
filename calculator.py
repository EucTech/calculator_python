#!/c/Users/User/AppData/Local/Microsoft/WindowsApps/python3
import math


def add(*args):
    """To add the inputs given by the user"""
    value = 0
    for num in args:
        value += num
    return value

def sub(*args):
    """To subtract the inputs given by the user"""
    value = args[0]
    for num in args[1:]:
        value -= num
    return value

def div(*args):
    """To divide the inputs given by the user"""
    value = args[0] #assign the numerator which is the first arguments to value
    for num in args[1:]: #start for the index 1 to loop through the arguments
        value /= num
    return value

def mul(*args):
    """To multipy the inputs given by the users"""
    value = 1 #anything multiply by 1 is 1 
    for num in args:
        value *= num
    return value

def sine(*num):
    """Sin()"""
    return math.sin(*num)

def cose(*num):
    """cos()"""
    return math.cos(*num)

def tang(*num):
    """tan()"""
    return math.tan(*num)

def square_root(*num):
    """"To calculate square root"""
    return math.sqrt(*num)

def power_of(a, o, b):
    """To calculate the power of a number"""

#print(add(4, 5))
#print(sub(2, 5))
#print(div(20, 10, 30))
#print(mul(2.0, 2))
