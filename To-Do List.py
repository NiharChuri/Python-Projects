# user input loop
while True:
    user_action = input("ADD an item, EDIT, VIEW, or COMPLETE an item your to-do list: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    # add an item to the list
    if "add" in user_action or "new" in user_action:
        todo_input = user_action[4:]
        
        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

        todo_list.append(todo_input + '\n')

        with open ("todos.txt" , "w") as file:
            todo_list = file.writelines(todo_list)
        
    # view the list
    elif "view" in user_action or "show" in user_action:

        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            row = f"{index+1}) {item.capitalize()}"
            print(row)

    # edit the list
    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

            new_todo = input("enter new to-do: ")
            todo_list[number] = new_todo + "\n"

        with open ("todos.txt" , "w") as file:
            todo_list = file.writelines(todo_list)

    # complete a task
    elif "complete" in user_action:
        number = int(user_action[8:])

        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

        completed_todo = todo_list[number-1].strip("\n")
        todo_list.pop(number-1)

        with open ("todos.txt" , "w") as file:
            file.writelines(todo_list)

        completetion_message = f"the task: '{completed_todo}' was completed, and removed from list"
        print(completetion_message)
        
    # clearing the to-do list
    elif "clear all" in user_action:
        # Clear the in-memory list
        todo_list.clear()

        # Clear the content of the file
        with open("todos.txt", "w") as file:
            file.truncate(0)

            print("To-do list cleared")

        with open("todos.txt" , "w") as file:
            file.writelines(todo_list)

    # exit the loop, completing the list
    elif "exit" in user_action:
        break
    
    # invalid commands
    elif _:
        print("invalid request")
    else:
        print("enter a valid command:")