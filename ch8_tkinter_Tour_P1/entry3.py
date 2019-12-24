from Tkinter import *
from quitter import Quitter 

fields = 'Name', 'Job', 'Pay'

def fetch(variables):
	for variable in variables:
		print 'Input => "%s"' % variable.get()

def makeform(root, fields):
	form = Frame(root)
	left = Frame(form)
	rite = Frame(form)
	form.pack(fill=X)
	left.pack(side=LEFT)
	rite.pack(side=RIGHT, expand=YES, fill=X)

	variables = []
	for field in fields:
		lab = Label(left, width=5, text=field)
		ent = Entry(rite)
		lab.pack(side=TOP)
		ent.pack(side=TOP, fill=X)
		svar = StringVar()
		ent.config(textvariable=svar)
		svar.set('enter here')
		variables.append(svar)
	return variables

if __name__ == '__main__':
	root = Tk()
	vars = makeform(root, fields)
	Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT, expand=YES, fill=BOTH)
	Quitter(root).pack(side=RIGHT, expand=YES, fill=BOTH)
	root.bind('<Return>', (lambda event: fetch(vars)))
	root.mainloop()