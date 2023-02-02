import tkinter as tk
import os
import tkinter.messagebox

# Create the window
# adds a task to the list of tasks. The task is taken from the task_entry widget
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks_to_file(tasks)

# view the list of tasks
# view_tasks() is called when the program starts and when a task is added, edited, or deleted
def view_tasks():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

# edit a task from the list of tasks
# edit_task() is called when the Edit Task button is clicked
def edit_task():
    if task_list.curselection():
        index = task_list.curselection()[0]
        new_task = task_entry.get()
        tasks[index] = new_task
        view_tasks()
        save_tasks_to_file(tasks)
    else:
        tkinter.messagebox.showerror("Error", "No task selected to edit")

# delete a task from the list of tasks
# delete_task() is called when the Delete Task button is clicked
def delete_task():
    if task_list.curselection():
        index = task_list.curselection()[0]
        result = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete this task?")
        if result:
            tasks.pop(index)
            view_tasks()
            save_tasks_to_file(tasks)
    else:
        tkinter.messagebox.showerror("Error", "No task selected to delete")

# save the tasks to a file
# save_tasks_to_file() is called when the program starts and when a task is added, edited, or deleted
def save_tasks_to_file(tasks):
    with open("todo_list_tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# load the tasks from a file
# load_tasks_from_file() is called when the program starts
def load_tasks_from_file():
    tasks = []
    try:
        with open("todo_list_tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

# clear all tasks from the list of tasks
# clear_all_tasks() is called when the Clear All Tasks button is clicked
def clear_all_tasks():
    result = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if result:
        task_list.delete(0, tk.END)
        tasks.clear()
        save_tasks_to_file(tasks)

# create the GUI
root = tk.Tk()
# root.geometry("400x400")
root.title("To-Do List")

# load the tasks from a file
tasks_file = "todo_list_tasks.txt"
# condition to check if the file exists
if os.path.exists(tasks_file):
    tasks = load_tasks_from_file()
else:
    tasks = []

# create the widgets
task_entry = tk.Entry(root, width=50)
# pack() method is used to display the widget
task_entry.pack()

# create the listbox
task_list = tk.Listbox(root)
# pack() method is used to display the widget
task_list.pack(fill=tk.BOTH, expand=True)

# create the scrollbar
# tk.Scrollbar() gets the task_list widget as an argument
scrollbar = tk.Scrollbar(task_list)
# pack() method is used to display the widget
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# configure the scrollbar
view_button = tk.Button(root, text="View Tasks", command=view_tasks)
# pack() method is used to display the widget
view_button.pack()

# button to add a task
# add_task() is called when the Add Task button is clicked
add_button = tk.Button(root, text="Add Task", command=add_task)
# pack() method is used to display the widget
add_button.pack()

# button to edit a task
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
# pack() method is used to display the widget
edit_button.pack()

# button to delete a task
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
# pack() method is used to display the widget
delete_button.pack()

# button to clear all tasks, calls clear_all_tasks()
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
# pack() method is used to display the widget
clear_button.pack()

# root.mainloop() is used to run the application
root.mainloop()