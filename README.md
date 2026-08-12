# python-todo-list
A command-line To-Do List application built with Python.

## Version 1.0 Features

- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- Exit the application

  ## Version 1.1 Improvements

- Prevent empty tasks from being added.
- Display task numbers when viewing tasks.
- Validate task numbers before completing or deleting.
- Handle empty task list when completing or deleting tasks.
- Validate menu option input (1–5).

  ### Version 1.2

* Added `try` / `except` exception handling for invalid input
* Improved input validation for menu options, task completion, and deletion
* Handles letters, special characters, decimals, and blank input without crashing
* Re-prompts the user after invalid input
* Removes unnecessary leading and trailing spaces from tasks
* Improved consistency across task input functions

  ## Version 2.0

* Added task editing
* Added task search
* Prevents empty edited tasks
* Preserves completed status when editing
* Prevents completing tasks more than once
* Updated menu for new features

  ## Version 3.0

* Added JSON file handling for persistent task storage
* Added `save_tasks()` and `load_tasks()` functions
* Tasks are automatically loaded when the program starts
* Tasks are saved after adding, completing, deleting, and editing



