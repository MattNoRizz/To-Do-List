#!/usr/bin/env python3
# Task Manager Application
# This program demonstrates the use of all Python keywords

from datetime import datetime
import os
import json

# Global variables
tasks = []
is_modified = False
current_user = None

class Task:
    """Class to represent a task in our to-do list"""
    
    def __init__(self, title, description=None, due_date=None, priority="Medium", completed=False):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        
    def complete(self):
        """Mark the task as completed"""
        self.completed = True
        return self
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority})"
    
    def __repr__(self):
        return self.__str__()

class TaskManager:
    """Class to manage tasks"""
    
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        """Add a task to the list"""
        self.tasks.append(task)
        return True
        
    def remove_task(self, index):
        """Remove a task by index"""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False
    
    def get_tasks(self, show_completed=True):
        """Get all tasks, optionally filtering completed ones"""
        if show_completed:
            return self.tasks
        else:
            return [task for task in self.tasks if not task.completed]
    
    def sort_tasks(self, key_func=None, reverse=False):
        """Sort tasks using the provided key function"""
        if key_func is None:
            # Default sort by creation date
            key_func = lambda task: task.created_at
        
        self.tasks.sort(key=key_func, reverse=reverse)

def save_tasks(filename="tasks.json"):
    """Save tasks to a JSON file"""
    global tasks, is_modified
    
    if not is_modified:
        return True
    
    try:
        with open(filename, 'w') as f:
            # Convert tasks to dictionaries
            task_dicts = []
            for task in tasks:
                task_dict = task.__dict__.copy()
                # Convert datetime objects to strings
                task_dict['created_at'] = task_dict['created_at'].isoformat()
                if task_dict['due_date']:
                    task_dict['due_date'] = task_dict['due_date'].isoformat()
                task_dicts.append(task_dict)
            
            json.dump(task_dicts, f, indent=2)
        is_modified = False
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file"""
    global tasks
    
    if not os.path.exists(filename):
        return False
    
    try:
        with open(filename, 'r') as f:
            task_dicts = json.load(f)
            
        tasks = []
        for task_dict in task_dicts:
            task = Task(
                title=task_dict['title'],
                description=task_dict['description'],
                priority=task_dict['priority'],
                completed=task_dict['completed']
            )
            
            # Convert string dates back to datetime objects
            task.created_at = datetime.fromisoformat(task_dict['created_at'])
            if task_dict['due_date']:
                task.due_date = datetime.fromisoformat(task_dict['due_date'])
            
            tasks.append(task)
        return True
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return False

def login():
    """Simple login function to demonstrate nonlocal keyword"""
    username = input("Enter username: ")
    
    def validate_user():
        nonlocal username
        if not username:
            username = "guest"
        return username
    
    return validate_user()

def add_sample_tasks():
    """Add some sample tasks for demonstration"""
    global tasks, is_modified
    
    tasks.append(Task("Learn Python keywords", "Complete the Python keywords assignment", priority="High"))
    tasks.append(Task("Submit GitHub repository", "Upload the code and create README", priority="High"))
    tasks.append(Task("Review Python best practices", priority="Medium"))
    tasks.append(Task("Take a break", "Rest after completing the assignment", priority="Low"))
    
    is_modified = True

def display_menu():
    """Display the main menu"""
    print("\n===== Task Manager =====")
    print("1. View all tasks")
    print("2. View incomplete tasks")
    print("3. Add a new task")
    print("4. Mark task as complete")
    print("5. Remove a task")
    print("6. Sort tasks")
    print("7. Save tasks")
    print("8. Exit")
    return input("Choose an option (1-8): ")

def view_tasks(show_completed=True):
    """Display tasks to the user"""
    global tasks
    
    filtered_tasks = tasks if show_completed else [t for t in tasks if not t.completed]
    
    if not filtered_tasks:
        print("No tasks found!")
        return
    
    print("\n--- Tasks ---")
    for i, task in enumerate(filtered_tasks):
        print(f"{i+1}. {task}")

def add_task():
    """Add a new task"""
    global tasks, is_modified
    
    title = input("Enter task title: ")
    if not title:
        print("Task title cannot be empty!")
        return
    
    description = input("Enter task description (optional): ")
    priority = input("Enter priority (High/Medium/Low, default: Medium): ")
    
    if not priority or priority.lower() not in ["high", "medium", "low"]:
        priority = "Medium"
    else:
        priority = priority.capitalize()
    
    task = Task(title, description, priority=priority)
    tasks.append(task)
    is_modified = True
    print(f"Task '{title}' added successfully!")

def mark_complete():
    """Mark a task as complete"""
    global tasks, is_modified
    
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as complete: ")) - 1
        
        if 0 <= index < len(tasks):
            tasks[index].complete()
            is_modified = True
            print(f"Task '{tasks[index].title}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def remove_task():
    """Remove a task"""
    global tasks, is_modified
    
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        
        if 0 <= index < len(tasks):
            title = tasks[index].title
            del tasks[index]
            is_modified = True
            print(f"Task '{title}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def sort_tasks_menu():
    """Menu for sorting tasks"""
    global tasks, is_modified
    
    print("\n--- Sort Tasks ---")
    print("1. By title")
    print("2. By priority")
    print("3. By creation date")
    print("4. By completion status")
    
    choice = input("Choose sorting option (1-4): ")
    
    if choice == '1':
        tasks.sort(key=lambda task: task.title.lower())
    elif choice == '2':
        # Custom priority sorting (High > Medium > Low)
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        tasks.sort(key=lambda task: priority_order.get(task.priority, 3))
    elif choice == '3':
        tasks.sort(key=lambda task: task.created_at)
    elif choice == '4':
        tasks.sort(key=lambda task: (0 if task.completed else 1, task.title.lower()))
    else:
        print("Invalid option!")
        return
    
    is_modified = True
    print("Tasks sorted successfully!")

def main():
    """Main function to run the application"""
    global current_user, tasks, is_modified
    
    print("Welcome to Task Manager!")
    
    # Demonstrate assert keyword
    assert isinstance(tasks, list), "Tasks should be a list"
    
    # Demonstrate try/except/finally for loading tasks
    try:
        if load_tasks():
            print("Tasks loaded successfully!")
        elif not tasks:  # If no tasks loaded and tasks list is empty
            print("No saved tasks found. Adding sample tasks...")
            add_sample_tasks()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Initialization complete.")
    
    # Demonstrate the login function with nonlocal keyword
    current_user = login()
    print(f"Logged in as: {current_user}")
    
    # Main application loop
    while True:
        choice = display_menu()
        
        if choice == '1':
            view_tasks(True)
        elif choice == '2':
            view_tasks(False)
        elif choice == '3':
            add_task()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            remove_task()
        elif choice == '6':
            sort_tasks_menu()
        elif choice == '7':
            if save_tasks():
                print("Tasks saved successfully!")
            else:
                print("Failed to save tasks.")
        elif choice == '8':
            # Ask to save before exiting if there are unsaved changes
            if is_modified:
                save_choice = input("You have unsaved changes. Save before exiting? (y/n): ")
                if save_choice.lower() == 'y':
                    save_tasks()
            
            print("Thank you for using Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Demonstrate yield keyword with a generator function
def task_generator(tasks_list):
    """Generator that yields tasks one by one"""
    for task in tasks_list:
        yield task

# Entry point of the program
if __name__ == "__main__":
    # Demonstrate the or, and, not keywords
    debug_mode = False or os.environ.get('DEBUG') == 'True'
    verbose = True and debug_mode
    quiet_mode = not verbose
    
    # Demonstrate if/elif/else
    if debug_mode:
        print("Running in debug mode")
    elif verbose:
        print("Running in verbose mode")
    else:
        print("Running in normal mode")
    
    # Demonstrate for/in/break/continue
    for arg in os.sys.argv:
        if arg == '--help':
            print("Task Manager - A simple task management application")
            break
        elif arg == '--version':
            print("Task Manager v1.0")
            continue
        # Other arguments processing would go here
    
    # Demonstrate while
    retry_count = 3
    while retry_count > 0:
        try:
            main()
            break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            retry_count -= 1
            if retry_count > 0:
                print(f"Retrying... ({retry_count} attempts left)")
            else:
                print("Maximum retry attempts reached. Exiting...")
                # Demonstrate raise
                raise RuntimeError("Application failed after multiple retries") from e
