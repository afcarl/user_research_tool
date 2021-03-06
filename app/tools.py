def process_todos(notes):
    todo_lists = []
    for note in notes:
        todo_list = []
        todos_found = False
        for line in note.note.split("\n"):
            if "to do" in line.lower() or "todo" in line.lower():
                todos_found = True
            if "end of to dos" in line.lower():
                todos_found = False
            if todos_found:
                if "*" in line: todo_list.append(line.replace("*",""))
        todo_lists.append(todo_list)
    return todo_lists
