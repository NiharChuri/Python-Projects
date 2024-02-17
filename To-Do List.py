# user input loop
while True:
    user_action = input("ADD an item, EDIT, VIEW, or COMPLETE an item your to-do list: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    # add an item to the list
    if user_action.startswith("add") or user_action.startswith("new"):
        todo_input = user_action[4:]
        
        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

        todo_list.append(todo_input + '\n')

        with open ("todos.txt" , "w") as file:
            todo_list = file.writelines(todo_list)
        
    # view the list
    elif user_action.startswith("view") or user_action.startswith("show"):

        with open("todos.txt" , "r") as file:
            todo_list = file.readlines()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            row = f"{index+1}) {item.title()}"
            print(row)

    # edit the list
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

                new_todo = input("enter new to-do: ")
                todo_list[number] = new_todo + "\n"

            with open ("todos.txt" , "w") as file:
                todo_list = file.writelines(todo_list)
        except ValueError:
            print("Enter the serial number of the task to be edited.")
            continue
        except IndexError:
            print("That Index does not exist.")
            continue

    # complete a task
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[8:])

            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

            completed_todo = todo_list[number-1].strip("\n")
            todo_list.pop(number-1)

            with open ("todos.txt" , "w") as file:
                file.writelines(todo_list)

            completetion_message = f"the task: '{completed_todo}' was completed, and removed from list"
            print(completetion_message)
        except ValueError:
            print("Enter the serial number of the task to be completed.")
            continue
        except IndexError:
            print("That Index does not exist.")
            continue

    # clearing the to-do list
    elif user_action.startswith("clear all"):
        # Clear the in-memory list
        todo_list.clear()
        break

        # Clear the content of the file
        with open("todos.txt", "w") as file:
            file.truncate(0)

            print("To-do list cleared")

        with open("todos.txt" , "w") as file:
            file.writelines(todo_list)

    # exit the loop, completing the list
    elif user_action.startswith("exit"):
        break
    
    # invalid commands
    elif _:
        print("invalid request")
    else:
        print("enter a valid command:")