FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the
    list of to-do items
    """
    with open(filepath, 'r') as file_local:  # with context menu for file handling
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":      # will only run if running this script direct
    print("Hello from functions. ")
    print(get_todos())