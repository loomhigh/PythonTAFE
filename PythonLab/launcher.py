#program that allows you to select which TAFE project to launch

import tkinter as tk

root = tk.Tk()
root.title('Lab Launcher')

# Sets up the command that launches the Project Python Files
def a_start():
    import Lab1
    print("launched 1")
def b_start():
    import Lab2
    print("launched 2")
def c_start():
    import Lab3
    print("launched 3")

# Creates the Buttons to select the Python Files and makes them run the appropriate command
button_a = tk.Button(root, text="Lab1", command = a_start)
button_a.pack()
button_b = tk.Button(root, text="Lab2",command = b_start)
button_b.pack()
button_c = tk.Button(root, text="Lab3",command = c_start)
button_c.pack()


root.mainloop()