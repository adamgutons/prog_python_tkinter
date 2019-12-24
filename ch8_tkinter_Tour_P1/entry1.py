from Tkinter import *
from quitter import Quitter

def fetch():
	print 'Input => %s' % ent.get()
	ent.insert(END, 'x')
	ent.insert(0, 'x')
	ent.delete(0, END)

root = Tk()
ent = Entry(root)
ent.insert(2, 'Type words here')
ent.pack(side=TOP, fill=X)

ent.focus()
ent.bind('<Return>', (lambda event:fetch()))
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()