import math
# First print the welcoming text to welcome the user to the calculator.
print("Welcome to CALCULATOR-inator 9000")
# Next make the user type in two numbers for a calculator.
number = float(input("Enter your first number: "))
number_2 = float(input("Enter your second number: "))

print("Select the operation")

print("")
# Then make the user select an operation to utilize the two numbers they put.
print("Options include: ")

print("addition")

print("subtraction")

print("multiplication")

print("division")

print("floor_division")

print("exponents")

print("remainder")

# Then after they type in the operation I use conditional statements to print the result.
choice = (input("Type in the operation: "))
print("")
print("Warning: If the operation is not in the following code will not run.")

if choice == 'addition':
    print(number + number_2)
elif choice == 'subtraction':
    print(number - number_2)
elif choice == 'multiplication':
    print(number * number_2)
elif choice == 'division':
    print(number / number_2)
elif choice == 'floor_divison':
    print(number // number_2)
elif choice == 'exponents':
    print(number ** number_2)
elif choice == 'remainder':
    print(number % number_2)




