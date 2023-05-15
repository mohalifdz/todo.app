FILEPATH = 'todos_item.txt'

def get_todos(filepath=FILEPATH):
    """To read a text file and return the
    to-do list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#  to know or inform the function in 3x string
#  print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """ To write to-do items in list """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# for testing if the function is working

if __name__ == "__main__":
    print('Hello')
    print(get_todos())