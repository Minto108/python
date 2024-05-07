import tkinter as tk
import time

root = tk.Tk()
root.title("To Do List")
root.geometry("550x400")

tasks = []

def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task = task_listbox.get(selected_task_index)
        tasks.remove(selected_task)
        task_listbox.delete(selected_task_index)

def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

def clear_tasks():
    tasks.clear()
    task_listbox.delete(0, tk.END)

def start_pomodoro():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task = task_listbox.get(selected_task_index)
        pomodoro_label.config(text=f"Pomodoro for {selected_task}")
        pomodoro_label.after(1000, pomodoro_timer)

def pomodoro_timer():
    text = pomodoro_label["text"]
    words = text.split(" ")
    if len(words) >= 4:
        minutes = int(words[3])
        if minutes > 0:
            minutes -= 1
            pomodoro_label.config(text=f"Pomodoro for {minutes} minutes")
            pomodoro_label.after(60000, pomodoro_timer)
        else:
            pomodoro_label.config(text="Pomodoro complete!")
    else:
        print("Error: pomodoro_label text is not in the correct format")

task_label = tk.Label(root, text="Enter a task:",fg="red",font="Roboto 16 bold")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = tk.Entry(root)
task_entry.grid(row=0, column=1, padx=5, pady=5,columnspan=3)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, padx=5, pady=5)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task,font="Roboto 10 bold")
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Task", command=delete_task,font="Roboto 10 bold")
delete_btn.grid(row=1, column=0, padx=5, pady=5)

view_btn = tk.Button(button_frame, text="View Tasks", command=view_tasks,font="Roboto 10 bold")
view_btn.grid(row=2, column=0, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks,font="Roboto 10 bold")
clear_btn.grid(row=3, column=0, padx=5, pady=5)

start_pomodoro_btn = tk.Button(button_frame, text="Start Pomodoro", command=start_pomodoro,font="Roboto 10 bold")
start_pomodoro_btn.grid(row=4, column=0, padx=5, pady=5)

task_listbox = tk.Listbox(root, height=5)
task_listbox.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

pomodoro_label = tk.Label(root, text="")
pomodoro_label.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(1, weight=1)

root.mainloop()