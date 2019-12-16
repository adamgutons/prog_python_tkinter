from Tkinter import *

class Hello(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		self.data = 42
		self.make_widgets()

	def make_widgets(self):
		widget = Button(self, text='Hello command world', command=self.message)
		widget.pack(side=LEFT)

	def message(self):
		self.data += 1
		print 'Hello from frame world %s!' % self.data

if __name__ == '__main__':
	Hello().mainloop()
