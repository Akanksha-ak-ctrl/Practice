import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create the entry widget for displaying input and output
        self.entry = tk.Entry(root, width=20, font=('Arial', 14), bd=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons for digits 0-9 and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
          command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

