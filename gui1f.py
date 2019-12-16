from Tkinter import *

"""
Widget objects intercept index operations and map them like a dict
so we can add text method by key
"""

widget = Label()
widget['text'] = 'Hello GUI world!'
widget.pack(side=TOP)
mainloop()
