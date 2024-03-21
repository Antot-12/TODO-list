import tkinter as tk
from tkinter import messagebox, font

def add_task():
    task = task_entry.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Попередження", "Завдання не може бути пустим.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning("Попередження", "Будь ласка, виберіть завдання для видалення.")

def clear_all_tasks():
    listbox_tasks.delete(0, tk.END)

def toggle_task_completion(event):
    if listbox_tasks.curselection():
        task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(task_index)
        if task_text.startswith("✓ "):
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task_text[2:])
        else:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, "✓ " + task_text)

# Створення вікна
window = tk.Tk()
window.title("To-Do List")
window.geometry("800x600")

# Великий шрифт для елементів
large_font = ('Verdana', 12)

# Темний фон та бірюзовий текст для заголовків та кнопок
window.configure(bg="#333333")
title_and_button_style = {"bg": "#333333", "fg": "#00FFFF", "font": large_font}

# Жовтий колір тексту для завдань
task_style = {"bg": "#333333", "fg": "#FFB400", "font": large_font}

# Рамки для компонентів
frame_input = tk.Frame(window, bg="#333333", pady=5)
frame_input.pack(fill=tk.X)

frame_tasks = tk.Frame(window, bg="#333333")
frame_tasks.pack(fill=tk.BOTH, expand=True)

frame_actions = tk.Frame(window, bg="#333333", pady=5)
frame_actions.pack(fill=tk.X)

# Заголовок для поля введення завдання
lbl_add_task = tk.Label(frame_input, text="Нове завдання:", **title_and_button_style)
lbl_add_task.pack(side=tk.LEFT, padx=5)

# Поле введення завдання
task_entry = tk.Entry(frame_input, width=50, **task_style)
task_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

# Кнопка додавання завдання
button_add_task = tk.Button(frame_input, text="Додати", command=add_task, **title_and_button_style)
button_add_task.pack(side=tk.RIGHT, padx=5)

# Список завдань
listbox_tasks = tk.Listbox(frame_tasks, height=20, width=50, **task_style)
listbox_tasks.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Прокрутка для списку завдань
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Додавання події для подвійного клацання по завданню для відзначення виконання
listbox_tasks.bind("<Double-1>", toggle_task_completion)

# Кнопки управління завданнями
button_delete_task = tk.Button(frame_actions, text="Видалити вибране завдання", width=23, command=delete_task, **title_and_button_style)
button_delete_task.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

button_clear_all_tasks = tk.Button(frame_actions, text="Очистити всі завдання", width=23, command=clear_all_tasks, **title_and_button_style)
button_clear_all_tasks.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5)

window.mainloop()
