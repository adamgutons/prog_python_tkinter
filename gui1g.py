from Tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello gui world')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('gui1g.py')
root.mainloop()