def getTodos(filepath):
    with open(filepath, "r") as local_file:
        local_todo_list = local_file.readlines()
    return local_todo_list


def writeTodos(filepath, todo_arg):
    with open (filepath , "w") as file:
        file.writelines(todo_arg)

# user input loop
while True:
    user_action = input("ADD an item, EDIT, VIEW, or COMPLETE an item your to-do list: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    # add an item to the list
    if user_action.startswith("add") or user_action.startswith("new"):
        todo_input = user_action[4:]
        
        todo_list = getTodos("todos.txt")

        todo_list.append(todo_input + '\n')

        writeTodos("todos.txt", todo_list)
        
    # view the list
    elif user_action.startswith("view") or user_action.startswith("show"):

        todo_list = getTodos("todos.txt")

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            row = f"{index+1}) {item.title()}"
            print(row)

    # edit the list
    elif user_action.startswith("edit"):
        try:
            editIndex = int(user_action[5:])
            editIndex -= 1

            todo_list = getTodos("todos.txt")

            new_todo = input("enter new to-do: ")
            todo_list[editIndex] = new_todo + "\n"

            writeTodos("todos.txt", todo_list)

        except ValueError:
            print("Enter the serial number of the task to be edited.")
            continue
        except IndexError:
            print("That Index does not exist.")
            continue

    # complete a task
    elif user_action.startswith("complete"):
        try:
            completeIndex = int(user_action[8:])

            todo_list = getTodos("todos.txt")

            completed_todo = todo_list[completeIndex-1].strip("\n")
            todo_list.pop(completeIndex-1)

            writeTodos("todos.txt", todo_list)

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

        writeTodos("todos.txt", todo_list)

    # exit the loop, completing the list
    elif user_action.startswith("exit"):
        break
    
    # invalid commands
    elif _:
        print("invalid request")
    else:
        print("enter a valid command:")