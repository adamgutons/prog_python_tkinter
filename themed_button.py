from Tkinter import *

def onSpam():
	print 'spam click'

class ThemedButton(Button):
	def __init__(self, parent=None, **configs):
		Button.__init__(self, parent, **configs)
		self.pack()
		self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)

root = Tk()
B1 = ThemedButton(root, text='spam', command=onSpam)
B2 = ThemedButton(root, text='eggs')
B1.pack()
B2.pack(expand=YES, fill=X)
root.mainloop()


