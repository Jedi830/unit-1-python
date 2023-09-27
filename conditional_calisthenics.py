'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
# I bassically went to see if the number the user inputed was divisble by 2 with a remainder of 0 to see if its either true of false.
number = int(input("Enter number: "))

if number > 10 and number % 2 == 0:
    print("True")
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
# I created a variable and utitlized it to ask the user if they are under 18 to see if they have to pay 10$ or 20.
student_age = int(input("Enter your age: "))
if student_age < 18:
    print("You must pay 10$ to enter for a ticket")
else:
    print("You must pay 20$ if over the age of 18")
'''
Exercise 3:
Convert a numerical grade to a letter grade based on scale.
A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: Below 60.
'''
# What I did was for every grade section I set it to a letter grade based of the grade section printed out if they have whichever letter grade they had.
student_grade = int(input("Enter the student grade: "))
if student_grade >= 90 and student_grade < 101:
    print("You have a A!")
elif student_grade >= 80 and student_grade < 90:
    print("You have a B!")
elif student_grade >= 70 and student_grade < 80:
    print("You have a C!")
elif student_grade < 70:
    print("You have a F!")
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
# I just created a variable asking what year the user inputed, and if the year was divisible by 4 with a remainder of 0 as well as divisible by 100 with a remainder of 0 it would be a Century year as well as a Leap year.
year = input("Enter a year:")
if int(year) % 4 == 0 and int(year) % 100 == 0:
    print("This is a century and a leap year")
else:
    print("False")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
# This one was difficult cause I utilized every variable bassically making it so that im asking the weight and which zone they live in to determine there cost.
weight_per_kilogram = int(input("What is the weight of the package: "))
area = input(f"Which zone do you live in?" )
ZoneA = 5
ZoneB = 7
print("-ZoneA")
print("-ZoneB")
if area == ZoneA:
    print("Your cost is 5$ per kilogram.")
elif area == ZoneB:
    print("Your cost is 7$ per kilogram")
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''