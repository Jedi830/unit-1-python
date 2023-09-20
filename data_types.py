
"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
# I have to create a float and convert into an integer. First create Float variable.
my_float = 134.5 
my_integer = int(my_float)
print(my_float)
print(my_integer)
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
# First I created a variable with a number 56 and I used if to print whether its negative or positive.
a = 56
if a > 0 :
    print ("Positive")
if a < 0:
    print ("Negative")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
# I created two variables, one with an integer and the other with float and printed them adding each variable.
c = 12
d = 3.5
print(d+c)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
# Bassically I created a Dictonary names my_fruits and put fruits with quantites and at the end printing each fruit and their value.
my_fruits = {
    'Grapes': 9,
    'Peaches': 18,
    'apples': 7
}
print(my_fruits)
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
my_controllers = "1, 2, 3"