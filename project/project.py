import sys


def show_menu():
    print("Todo List Manager")
    print("-----------------")
    print("1. View Todos")
    print("2. Add Todo")
    print("3. Mark Todo as Done")
    print("4. Quit")


def view_todos(todo_list):
    print("Todo List:")
    if not todo_list:
        print("")
        print("No todos.")
        print("")
    else:
        for index, todo in enumerate(todo_list, start=1):
            status = "[ ]"
            if todo["done"]:
                status = "[X]"
            print(f"{index}. {status} {todo['task']}")


def add_todo(todo_list, task):
    todo = {"task": task, "done": False}
    todo_list.append(todo)
    print("Todo added successfully.")


def mark_todo_as_done(todo_list, index):
    if 1 <= index <= len(todo_list):
        todo = todo_list[index - 1]
        if not todo["done"]:
            todo["done"] = True
            print("Todo marked as done.")
        else:
            print("Todo is already done.")
    else:
        print("Invalid todo index.")
            


def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_todos(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_todo(todo_list, task)
        elif choice == "3":
            index = int(input("Enter the todo index: "))
            mark_todo_as_done(todo_list, index)
        elif choice == "4":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
