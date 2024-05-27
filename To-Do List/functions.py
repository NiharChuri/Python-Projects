def getTodos(filepath="todos.txt"):
    with open(filepath, "r") as local_file:
        local_todo_list = local_file.readlines()
    return local_todo_list


def writeTodos(todo_arg, filepath="todos.txt", ):
    with open (filepath , "w") as file:
        file.writelines(todo_arg)