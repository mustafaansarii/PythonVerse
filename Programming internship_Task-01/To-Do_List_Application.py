import tkinter as tk
from tkinter import simpledialog

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.task_listbox = tk.Listbox(self.master)
        self.task_listbox.pack(pady=10)
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()
        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.pack()
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()
        self.task_listbox.insert(tk.END, "[Incomplete] Add Your Task")
    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        if description:
            self.task_listbox.insert(tk.END, f"[Incomplete] {description}")
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            current_task = self.task_listbox.get(selected_task_index)
            new_status = simpledialog.askstring("Update Task Status", f"Update status for:\n{current_task}",
                                                initialvalue=current_task.split()[0][1:-1])
            if new_status and new_status.lower() in ["complete", "incomplete"]:
                updated_task = f"[{new_status.capitalize()}] {current_task.split(maxsplit=1)[1]}"
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()