import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
# For this one I just used the normal datetime.now function to print out the time and date now.
x = datetime.datetime.now()
print(x)
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
# For this one I used the function strftime which is "string for time" to print out the month day and year us format.
from datetime import datetime
now = datetime.now()
month = now.strftime("%m")
print("month: ",month)
day = now.strftime("%D")
print("Day: ",day)
year = now.strftime("%Y")
print("Year: ",year)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
# I used the datetime module to convert the string into a actual datetime thats printed on the console.
from datetime import datetime
date_string = "10/11/2023"
date_time = datetime.strptime(date_string, "%m/%d/%Y")
print(date_time)
time_string = "09:50:30"
time_clock = datetime.strptime(time_string,"%H:%M:%S")
print(time_clock)
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""