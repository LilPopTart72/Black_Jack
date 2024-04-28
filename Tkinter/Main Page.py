from tkinter import *
import PIL

root = Tk()
img = ImageTk.PhotoImage(Image.open("True1.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()