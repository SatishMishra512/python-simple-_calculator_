import tkinter as tk
from tkinter import messagebox

class Calculator:
    def _init_(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x400")
        self.master.resizable(False, False)

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_display = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 24), justify="right", bd=5)
        result_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.master, text=button, command=cmd, font=('Arial', 18), width=5, height=2).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(self.master, text='C', command=self.clear, font=('Arial', 18), width=5, height=2).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # Configure grid weights
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                messagebox.showerror("Error", "Invalid input")
                self.result_var.set("")
        else:
            current = self.result_var.get()
            self.result_var.set(current + key)

    def clear(self):
        self.result_var.set("")

if _name_ == "_main_":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()