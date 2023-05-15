# import python moduls
# https://docs.python.org/3/py-modindex.html (ref index module di Python)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes (ref module time)


# buat module time di Python

import functions
import time

now = time.strftime('%d %B, %Y %H:%M:%S')
print('The time is below:')
print('Today is:', now)

while True:
    user = input('Choose add, show, edit, complete, or done: ')
    user = user.strip()  # Return a copy of the string with leading and trailing whitespace removed
    user = user.lower()

    if user.startswith('add'):
        todo = user[4:]  # slice the add argument

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # item = item.title()
            item = item.strip('\n')
            print(f'{index + 1}. {item}')
            # print(todos)

    elif user.startswith('edit'):
        try:
            number = int(user[5:])
            number = int(number) - 1

            todos = functions.get_todos()  # sama dengan umumnya

            change = input('what activities do you want to edit? ') + '\n'
            todos.__setitem__(number, change)

            print('These are the edited todo: ', todos)

            functions.write_todos(todos)
            # todos[number] = change

        except ValueError:
            print('Your command is not valid')
            continue

    elif user.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user[9:])
            number = int(number) - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            message = f'The todo that removed was {todo_to_remove}'
            print(message)
        except IndexError:
            print('Your number is not listed in todos')
            continue

        except ValueError:
            print('You are doing a wrong input')
            continue

    elif user.startswith('done'):
        break

    else:
        print('You out wrong command')

print('done bybe')
