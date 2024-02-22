import tkinter as tk
from tkinter import simpledialog as sd

class ToDoApp:
    def __init__(self, m):
        self.m = m
        self.m.title("To-Do List App by Mustafa")
        self.lb = tk.Listbox(self.m)
        self.lb.pack(pady=10)
        self.ab = tk.Button(self.m, text="Add Task", command=self.at)
        self.ab.pack()
        self.ub = tk.Button(self.m, text="Update Task", command=self.ut)
        self.ub.pack()
        self.qb = tk.Button(self.m, text="Quit", command=self.m.quit)
        self.qb.pack()
        self.lb.insert(tk.END, "[Incomplete] Add Your Task")     
    def at(self):
        d = sd.askstring("Add Task", "Enter task description:")
        if d:
            self.lb.insert(tk.END, f"[Incomplete] {d}")
    def ut(self):
        s = self.lb.curselection()
        if s:
            s = s[0]
            t = self.lb.get(s)
            ns = sd.askstring("Update Task Status", f"Update status for:\n{t}", initialvalue=t.split()[0][1:-1])
            if ns and ns.lower() in ["complete", "incomplete"]:
                ut = f"[{ns.capitalize()}] {t.split(maxsplit=1)[1]}"
                self.lb.delete(s)
                self.lb.insert(s, ut)
def main():
    r = tk.Tk()
    app = ToDoApp(r)
    r.mainloop()

if __name__ == "__main__":
    main()
