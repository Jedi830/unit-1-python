"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
# Used the range function starting from 1 to 10 in incriments of 1.
for x in range(1,11,1):
    print(x)
print(" ")
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
# Same thing starting from 900 to 1000 in incriments of 10.
for x in range(900,1001,10):
    print(x)

print(" ")
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
# Starting from 1 to 100 in increments of 9.
for x in range(1,101,9):
    print(x)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
# Bassically using a variable, I added the numbers in the loop using the += symbol and num variable in the range.
x = 0 
for num in range(1,11,1):
    x += num
    print(x)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
*
* *
* * *
* * * *
* * * * *
- Explain the iterative process that this code executes to get that output
"""
# So bassically the rows variable is used 5 times so basically for every row the variable i is adding by one each row and making the i variable the * symbol.
rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
    print()
