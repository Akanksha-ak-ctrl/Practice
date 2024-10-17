import tkinter as tk

def on_check_changed():
    if check_var1.get():
        label.config(text="Option 1 selected")
    else:
        label.config(text="Option 1 deselected")

def on_check2_changed():
    if check_var2.get():
        label.config(text="Option 2 selected")
    else:
        label.config(text="Option 2 deselected")

# Create the main window
root = tk.Tk()
root.title("Check Button Example")

# Define BooleanVar variables to track check button states
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()

# Create check buttons
check_button1 = tk.Checkbutton(root, text="Option 1", variable=check_var1, command=on_check_changed)
check_button2 = tk.Checkbutton(root, text="Option 2", variable=check_var2, command=on_check2_changed)

# Create a label to display the selected options
label = tk.Label(root, text="")
label.pack()

# Pack the check buttons
check_button1.pack()
check_button2.pack()

# Start the Tkinter event loop
root.mainloop()
