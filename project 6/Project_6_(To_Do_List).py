import customtkinter as ctk
import json
import os
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "project 4/tasks.json"
task_list = []

def add_task():
    task = task_entry.get().strip()
    due = due_entry.get().strip()
    priority = priority_entry.get().strip().capitalize()

    if task:
        task_list.append({"task": task, "due": due, "priority": priority, "done": False})
        update_display()
        task_entry.delete(0, "end")
        due_entry.delete(0, "end")
        priority_entry.delete(0, "end")

def mark_complete():
    try:
        index = int(task_display.index("insert").split('.')[0]) - 1
        task_list[index]["done"] = True
        update_display()
    except:
        messagebox.showwarning("Error", "Select a task line.")

def delete_task():
    try:
        index = int(task_display.index("insert").split('.')[0]) - 1
        del task_list[index]
        update_display()
    except:
        messagebox.showwarning("Error", "Select a task line.")

def update_display():
    task_display.delete("1.0", "end")
    for idx, task in enumerate(task_list):
        status = "[✓]" if task["done"] else "[ ]"
        line = f"{idx+1}. {status} {task['task']} (Due: {task['due']}, Priority: {task['priority']})\n"
        task_display.insert("end", line)

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(task_list, f)
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    global task_list
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            task_list = json.load(f)
        update_display()

app = ctk.CTk()
app.title("Task Manager")
app.geometry("500x500")
app.resizable(False,False)

task_entry = ctk.CTkEntry(app, placeholder_text="Enter Task", width=300)
task_entry.pack(pady=10)

due_entry = ctk.CTkEntry(app, placeholder_text="Due Date (Optional)", width=300)
due_entry.pack(pady=5)

priority_entry = ctk.CTkEntry(app, placeholder_text="Priority (Low/Medium/High)", width=300)
priority_entry.pack(pady=5)

add_button = ctk.CTkButton(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_display = ctk.CTkTextbox(app, width=450, height=250)
task_display.pack(pady=10)

mark_button = ctk.CTkButton(app, text="Mark Complete", command=mark_complete)
mark_button.pack(pady=5)

delete_button = ctk.CTkButton(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

save_button = ctk.CTkButton(app, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

load_tasks()
app.mainloop()
