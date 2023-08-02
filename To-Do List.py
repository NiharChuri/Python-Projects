# user input loop
while True:
    user_action = input("ADD an item, EDIT, VIEW, or COMPLETE an item your to-do list: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:

        # add an item to the list
        case "add" | "new" :
            todo_input = input("enter a to-do: ") + "\n"
            
            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

            todo_list.append(todo_input)

            with open ("todos.txt" , "w") as file:
                todo_list = file.writelines(todo_list)
            
        # view the list
        case "view" | "show" | "display":

            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

            for index, item in enumerate(todo_list):
                item = item.strip("\n")
                row = f"{index+1}) {item.capitalize()}"
                print(row)

        # edit the list
        case "edit":
            number = int(input("number of to-do to edit: "))
            number = number - 1

            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

                new_todo = input("enter new to-do: ")
                todo_list[number] = new_todo + "\n"

            with open ("todos.txt" , "w") as file:
                todo_list = file.writelines(todo_list)

        # complete a task
        case "complete":
            number = int(input("task to be marked as complete: "))

            with open("todos.txt" , "r") as file:
                todo_list = file.readlines()

            completed_todo = todo_list[number-1].strip("\n")
            todo_list.pop(number-1)

            with open ("todos.txt" , "w") as file:
                file.writelines(todo_list)

            completetion_message = f"the task: '{completed_todo}' was completed, and removed from list"
            print(completetion_message)

        # exit the loop, completing the list
        case "exit" | "finish":
            break
        
        # clearing the to-do list
        case "clear all":
            with open("todos.txt" , "r") as file:
                file.readlines()
                todo_list.clear()

                print("to-do list cleared")

            with open("todos.txt" , "w") as file:
                file.writelines(todo_list)

        # invalid commands
        case _:
            print("invalid request")