# TO DO LIST MANAGER

#### Video Demo:

https://youtu.be/VVepAYXMWIk

#### Description:

This project is a simple Todo List Manager implemented in Python. It allows users to manage their todo items by performing various operations such as viewing todos, adding a new todo, marking a todo as done, and quitting the program.

Here's a description of each component of the project:

#### show_menu() function:

 This function displays the main menu of the Todo List Manager, showing the available options for the user.

#### view_todos(todo_list) function:

This function takes a list of todos as input and displays them in a formatted manner. It iterates over the todo list, prints the index, status (done or not done), and task for each todo item.

#### add_todo(todo_list, task) function:

 This function adds a new todo item to the todo list. It takes the todo list and the task description as input, creates a new todo dictionary with the task and a "done" status set to False, and appends it to the todo list.

#### mark_todo_as_done(todo_list, index) function:

This function marks a todo item as done. It takes the todo list and the index of the todo item as input. If the index is valid, it retrieves the corresponding todo item from the list and updates its "done" status to True. If the todo item is already marked as done, it prints a message indicating that it is already done. If the index is invalid, it prints an error message.

#### main() function:

This is the main function that runs the Todo List Manager. It initializes an empty todo list and enters a loop to continuously display the menu, prompt for user input, and perform the selected operation based on the user's choice. It continues to execute until the user chooses to quit the program.

The project provides a basic command-line interface for managing todo items. Users can view their todos, add new todos, mark todos as done, and quit the program.

