import tkinter as tk

# Core window Initialize, Size, and Name!!!
root = tk.Tk()

root.geometry('800x500')
root.title("Calculator")

# Basic Text
label = tk.Label(root, text="Hello World", font=('Arial', 15))
label.pack(padx=20, pady=20)

# TextBox
textbox = tk.Text(root, height=3, font=('Arial', 15))
textbox.pack(padx=20, pady=20)

# single entry text line
myentry = tk.Entry(root)
myentry.pack()

# Button Basics
button = tk.Button(root, text="Click Me", font=('Arial', 18))
button.pack(padx=10, pady=10)

# The Frame and Grid layout for buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=1, pady=1)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=1, pady=1)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=1, pady=1)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, padx=1, pady=1)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=1, pady=1)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=1, pady=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=1, pady=1)

buttonframe.pack(fill="x")

# place function
anotherbtn = tk.Button(root, text="test", font=('Arial', 5))
anotherbtn.place(x=200, y=200, height=20, width=20)

# core window
root.mainloop()