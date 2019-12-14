from Tkinter import *

Label(text='Another minimal gu').pack()
Label(text='Another Label').pack()
"""
we call mainloop w/ or w/out a widget b/c we didn't pass 
any parent arguments to the labels. Defaults to None, which defaults
to the the automatically created Tk object
"""
mainloop()