todo_list = ["Do your homework","Practice guitar","Work out"]
# For this little code right here, I just did a while loop because I wanted to make the user inteface have easier access to the todos.
while 1:
    print("Your current todos are:") 
    print(" ")

    # First off I have to print the todos I chose and list them out for the user.
    print(todo_list)
    # Second I created a variable called choice and made it a sting input so that I can ask the user if they would either add or remove a todo and type in either "add" or "remove".
    choice = (input("Would you like to add or remove a todo from your todo list?"))
    # After that I then created a if statement that checks if the choice is either add or remove, and if its add, asks the user what they want to add, and list the new list. Same with the remove statement.
    if choice == 'add':
        todo = input("enter todo: ")
        todo_list.append(todo)
        print(todo_list)
    if choice == 'remove':
        print("What would you like to remove from the list: ")
        todo2 = input("enter todo: ")
        todo_list.remove(todo2)
        print(todo_list)
