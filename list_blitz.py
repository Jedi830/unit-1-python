
"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
# I just created 4 variables of my games on my xbox.
my_games = ["Castle Crashers","Apex","Brawlhalla","Diablo 4"]
print(my_games)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
# Added fortnite to my "List" of games.
my_games.append("Fortnite")
print(my_games)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
# I removed castle crashers from my "list" of games.
my_games.remove("Castle Crashers")
print(my_games)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
# I first deleted "fortnite" and added in its place the game "gang beasts".
del my_games[3]
my_games.append("Gang Beasts")
print(my_games)


# I just added two more games overwatch and cod to my_games list.
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_games.append("Overwatch")
my_games.append("Call of Duty")
print(my_games)


# I then deleted the first value of my list of games and printed it.
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del my_games[0]
print(my_games)
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
# Then I created a new value equal to the first two games using the index colon method.
other_games = my_games[0:2]
print(other_games)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
# And then in all added both values together to get my full list, all_games.
all_games = my_games + other_games
print(all_games)