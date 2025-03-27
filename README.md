# Python Keywords Demonstration Project

This project demonstrates the use of all Python keywords through a Task Manager application.

## Description

The Task Manager is a command-line application that allows users to:
- Add, view, and remove tasks
- Mark tasks as complete
- Sort tasks by different criteria
- Save tasks to a file and load them later

## Python Keywords Used

This project demonstrates all the required Python keywords:

1. **and**: Used in logical conditions (`if verbose and debug_mode`)
2. **as**: Used in exception handling and with statements (`with open(filename, 'w') as f`, `except Exception as e`)
3. **assert**: Used to verify conditions (`assert isinstance(tasks, list)`)
4. **break**: Used to exit loops (`break` in the main loop when exiting)
5. **class**: Used to define the `Task` and `TaskManager` classes
6. **continue**: Used to skip iterations in loops (`continue` in command-line argument processing)
7. **def**: Used to define functions (`def main()`, `def add_task()`, etc.)
8. **del**: Used to delete tasks (`del tasks[index]`)
9. **elif**: Used in conditional statements (menu choices)
10. **else**: Used in conditional statements (menu choices)
11. **except**: Used in exception handling (`try/except` blocks)
12. **False**: Used as a boolean value (`completed=False`)
13. **finally**: Used in exception handling (`try/except/finally` block)
14. **for**: Used in loops (`for task in tasks`)
15. **from**: Used in imports (`from datetime import datetime`)
16. **global**: Used to access global variables (`global tasks, is_modified`)
17. **if**: Used in conditional statements (throughout the code)
18. **import**: Used to import modules (`import os, import json`)
19. **in**: Used in loops and membership tests (`for task in tasks`, `if choice in ['1', '2']`)
20. **is**: Used for identity comparison (`if task is None`)
21. **lambda**: Used for sorting tasks (`key=lambda task: task.title`)
22. **None**: Used as a null value (`description=None`)
23. **nonlocal**: Used in nested functions to modify outer scope variables (`nonlocal username`)
24. **not**: Used for logical negation (`if not tasks`)
25. **or**: Used in logical conditions (`debug_mode = False or os.environ.get('DEBUG') == 'True'`)
26. **pass**: Used as a placeholder in functions or classes
27. **raise**: Used to raise exceptions (`raise RuntimeError`)
28. **return**: Used to return values from functions (`return True`)
29. **True**: Used as a boolean value (`is_modified = True`)
30. **try**: Used in exception handling (`try/except` blocks)
31. **while**: Used for loops (`while True` in the main loop)
32. **with**: Used for context management (`with open(filename, 'w') as f`)
33. **yield**: Used in generator functions (`yield task`)

## How to Run

1. Clone this repository
2. Run the application:
   ```
   python task_manager.py
   ```
3. Follow the on-screen prompts to manage your tasks

## Features

- User login system
- Task creation with title, description, and priority
- Task completion tracking
- Multiple sorting options
- File-based persistence using JSON
- Error handling and recovery

## Requirements

- Python 3.6 or higher

