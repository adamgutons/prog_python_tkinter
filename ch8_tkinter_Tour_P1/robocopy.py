from Tkinter import *   #----> Import tkinter module
import subprocess       #----> Import subprocess module
import threading        #----> Import threading, used to avoid GUI lockup
                        #----> when making a subprocess call
import sys
import os

class Robocopy(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Move files', command=self.robo_this)
        widget.pack(side=BOTTOM, expand=YES, fill=BOTH)
        read_label = Label(self, text='')
        read_label.pack(side=BOTTOM, expand=YES, fill=BOTH)
        entry_label = Label(self, text='Source file(s)')
        entry_label.pack(side=TOP, expand=YES, fill=BOTH)
        server_path_entry = Entry(self)
        server_path_entry.pack(side=TOP, expand=YES, fill=BOTH)
        dest_label = Label(self, text='Destination folder')
        dest_label.pack(side=TOP, expand=YES, fill=BOTH)
        dest_path_entry = Entry(self)
        dest_path_entry.pack(side=TOP, expand=YES, fill=BOTH)



    def robo_this(self):
        server_path = server_path_entry.get()
        local_path = dest_path_entry.get()
        #geoDB = os.path.basename(server_path)
        #true_local = local_path + os.sep + geoDB
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        if os.path.exists(server_path) and os.path.exists(local_path):
            try:
                read_label.config(self, text="Beginning file transfer, this can take several minutes.\nPlease do not close the tool until transfer is complete.")
                args = ["robocopy", server_path, local_path, '/s']
                p = subprocess.call(args)
                if p:
                    read_label.config(self, text='File transfer complete...')
            except:
               read_label.config(self, text='Something went wrong...please check source and destination file paths')

if __name__ == '__main__':
    Robocopy().mainloop()
