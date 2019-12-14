from Tkinter import *
"""
Yes and Both specify that the lable should grow along with the parent
if user chooses to expand the window

expand=YES 
	asks the packer to expand the allocated space for the widget in
	general into any unclaimed space in the widgets parent
fill option 
  	can be used to stretch the widget to occupy all of its allocated space
"""
Label(text='Helo GUI world!').pack(expand=YES, fill=BOTH)
mainloop()