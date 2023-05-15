FILEPATH = 'todos.txt'

def get_todos(filepath='Files/FILEPATH'):
    """To read a text file and return the
    to-do list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#  to know or inform the function in 3x string
#  print(help(get_todos))


def write_todos(todos_arg, filepath='Files/FILEPATH'):
    """ To write to-do items in list """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)