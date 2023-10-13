
"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
x = 1
while x < 11:
    print(x)
    x += 1
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
x = 10
while (x >= 1):
    print(x)
    x=x - 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number = int(input("Enter a number: "))
product = 1
while number > 0:
    product *= number
    number -= 1
    print(product)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
ps = "Mango"
ans = input("Guess the password")
while ans != ps:
    print("Try again")
    ans = input("Guess my password: ")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""