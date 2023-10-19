"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
# I used a class that was person then created attributes with name and age then called to the method.
class person:
    role = "student"
    def __init__(self,name, age):
        self.name = name
        self.age = age

jedaiah = person("Jedaiah D.", 17)
print(jedaiah.name)
print(jedaiah.age)
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
# I used the class animal first then created two subclasses bassically using the info from the main class to get my code.
class animal:
    def speak(self):
        print("")

cat = "Landon"

class cat(animal):
    role = "pet"
    def speak(self):
        print("MEOWWWWWW")

dog = "Charles"

class dog(animal):
    role = "pet"
    def speak(self):
        print("RUFFF")


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class bank_account:
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner

    def u_balance(self):
        print("The balance is" + self.balance)
        
    def deposit(self,dep):
        self.balance = self.balance + dep
        print("Your new balance is", self.balance)

    def withdraw(self,with_draw):
        self.balance = self.balance - with_draw
        print("New balance is", self.balance)


