import sys
from Tkinter import *

class HelloCallable:
	def __init__(self):
		self.msg = "Hello world AGAIN"

	def __call__(self):
		print(self.msg)
		sys.exit()

widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()