#program that allows you to select which TAFE project to launch

import tkinter as tk

root = tk.Tk()
root.title('AT2 Project Launcher')

# Sets up the command that launches the Project Python Files
def a_start():
    import A_Task2_Project
    print("launched A")
def b_start():
    import B_Task2_Project
    print("launched B")
def c_start():
    import C_Task2_Project
    print("launched C")

# Creates the Buttons to select the Python Files and makes them run the appropriate command
button_a = tk.Button(root, text="A: Simple Contacts", command = a_start)
button_a.pack()
button_b = tk.Button(root, text="B: Task Manager",command = b_start)
button_b.pack()
button_c = tk.Button(root, text="C: Inventory Manager",command = c_start)
button_c.pack()


root.mainloop()