from Tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text="Basic demos").pack()
		for (k,v) in demos.items():
			Button(self, text=k, command=v).pack(side=TOP, fill=BOTH)
		Quitter(self).pack(side=TOP, fill=BOTH)



if __name__ == '__main__':
	Demo().mainloop()