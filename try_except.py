
try:
 age = int(input('Enter your age: '))
 if age <= 21:
  print('You are not allowed to enter, you are too young.')
 else:
  print('Welcome, you are old enough.')
except:
    print("Age not identified.")

try:
  faveNum = int(input('What is your favorite number: '))
except:
  print("Not divisible by 0")


try:
  print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
  print("Not divisible by zero.")