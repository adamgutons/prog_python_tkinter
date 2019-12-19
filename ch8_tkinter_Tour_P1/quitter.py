from Tkinter import *
from tkMessageBox import askokcancel

class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		widget = Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT, expand=YES, fill=BOTH)

	def quit(self):
		ans = askokcancel('Verify exit', "Really quit?")
		if ans: 
			Frame.quit(self)
		else:
			return 56


if __name__ == '__main__':
	Quitter().mainloop()