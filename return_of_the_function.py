"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
# I used the function to mulitply the variable by itself and get the sqaured answer
def add_num(a):
    return a * a
x = add_num(7)
print(x)

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
# I used the same method beofre just with two different variables and multiplied them.
def add_area(a,b):
    return a * b
x = add_area(12,8)
print(x)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
# This one I used the actual formula to get the conversion from celcius to farenheit.
def con_cf(a):
    return (a * 9) / 5 + 32
x = con_cf(67)
print(x)

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def avg(a):
    total = sum(a)
    return total / len(a)
a = 4,5,6,9,10
print((average(a)))
