from Tkinter import *

"""
root = Tk()
labelfont = ('times', 20, 'overstrike')
widget = Label(root, text="Hello config world!")
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
"""

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=80, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()