
'''
Python 3.10.0
Purpose: write a program that uses a GUI to allow a user to copy all files
    from a select folder to another select folder that have been modified
    w/i the last 24 hours.
'''

import os
import shutil
import tkinter
from tkinter import *
from tkinter import filedialog
import time
###

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.w = 600
        self.h = 200
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)
        self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.master.title('File Xfer Tool')

        self.folderPath1 = StringVar()
        self.folderPath2 = StringVar()
###
       
        #source folder text label field
        self.lblSrcFldr = Label(self.master, text='Source Folder:', \
            font=("Helvetica", 16))
        self.lblSrcFldr.grid(row=0, column=0, padx=(0,0), pady=(30,0))

        #source folder entry field
        self.entSrcFldr = Entry(self.master, width=40, text=self.folderPath1)
        self.entSrcFldr.grid(row=0, column=1, padx=(10,0), pady=(30,0))

        #source folder browse btn
        self.btnSrcFldrBrws = Button(self.master, text='Browse', \
            width=10, height=1, command=self.browse_btn1)
        self.btnSrcFldrBrws.grid(row=0, column=2, padx=(10,0), pady=(30,0))
###

        #destination folder text label field
        self.lblDestFldr = Label(self.master, text='Destination Folder:', \
            font=("Helvetica", 16))
        self.lblDestFldr.grid(row=1, column=0, padx=(38,0), pady=(30,0))

        #destination folder entry field
        self.entDestFldr = Entry(self.master, width=40, text=self.folderPath2)
        self.entDestFldr.grid(row=1, column=1, padx=(10,0), pady=(30,0))
        
        #destination folder browse btn
        self.btnDestFldrBrws = Button(self.master, text='Browse', \
            width=10, height=1, command=self.browse_btn2)
        self.btnDestFldrBrws.grid(row=1, column=2, padx=(10,0), pady=(30,0))
###

        #file check btn
        self.btnFileCheck = Button(self.master, text='File Check', \
            width=10, height=1,bg='lightblue', font=("Helvetica", 16),\
            command=self.move_files)
        self.btnFileCheck.grid(row=2, column=1, padx=(0,70), pady=(30,30))

    #create fns that will allow the user to browse to select a folder
    #and assign it to a variable.
    #i don't like that i basically used duplicate code, but i couldn't
    #think of another wat to do it using only 1 fn
    def browse_btn1(self):
        folderName = filedialog.askdirectory()
        self.folderPath1.set(folderName)

    def browse_btn2(self):
        folderName = filedialog.askdirectory()
        self.folderPath2.set(folderName)
###        

    #create fn that looks thru all files in source folder and moves any to
    #destination folder that were modified w/i last 24 hours
    def move_files(self):
        self.now = time.time()
        self.yesterday = self.now - 24*60*60

        self.source = self.folderPath1.get()
        self.destination = self.folderPath2.get()

        self.files = os.listdir(self.source)
                
        for i in self.files:
            if os.path.getmtime(self.source + '//' + i) > self.yesterday:
                shutil.move(self.source + '//' + i, self.destination)
###

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
