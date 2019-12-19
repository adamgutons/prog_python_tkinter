from tkFileDialog import askopenfilename
from tkColorChooser import askcolor
from tkMessageBox import askquestion, showerror
from tkSimpleDialog import askfloat

demos = {
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda:askquestion('Warning', 'You typed shit.\nConfirm?'),
	'Error': lambda:showerror('Error!', 'Nigga deeed'),
	'Input': lambda:askfloat('Entry', 'Enter money bitch')	
}


"""
python 3

from Tkinter.fielddialog import askopenfilename
from Tkinter.colorchooser import askcolor
from Tkinter.messagebox import askquestion, showerror
from Tkinter.simpledialog import askfloat

demos = {
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda:askquestion('Warning', 'You typed shit.\nConfirm?'),
	'Error': lambda:showerror('Error!', 'Nigga deeed'),
	'Input': lambda:askfloat('Entry', 'Enter money bitch')	
}

"""