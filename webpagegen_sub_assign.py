
'''
Python 3.10.0
Purpose: write a program that uses a GUI to allow a user to genearte a web page
    based on input text and display the page.
'''

import webbrowser
import os
import tkinter
from tkinter import *
from tkinter import scrolledtext


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(800, 400))
        self.master.title('HTML Generator')
        self.master.config(bg='lightblue')

        root.columnconfigure(0,weight=5)
        root.rowconfigure(0,weight=1)
        root.rowconfigure(1,weight=5)
        root.rowconfigure(2,weight=1)
        
        #HTML body text label field
        self.lblBodyText = Label(self.master, text='HTML Body Text:', \
            font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblBodyText.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        #HTML body text entry field using scrolledtext for better formatting
        self.entHTMLBodyText = scrolledtext.ScrolledText(self.master, \
            wrap=tkinter.WORD, width=40, height=7, font=("Helvetica", 16))
        self.entHTMLBodyText.grid(row=1, column=0, padx=(0,0), pady=(30,0))
        
        #generate btn
        self.btnGenerate = Button(self.master, text='Generate Web Page', \
            width=20, height=2, command=self.generate)
        self.btnGenerate.grid(row=2, column=0, padx=(0,0), pady=(30,30))


    #create generate btn fn
    def generate(self):
        #store user input into variable
        self.varHTMLBodyText = self.entHTMLBodyText.get("1.0", END)
        #check to see if html file exists and create it if not
        if not os.path.exists('webpagegen.html'):
            htmlFile = open("webpagegen.html","x")
        else:
            #open html file
            htmlFile = open("webpagegen.html","w")
        #write to html file
        htmlFile.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\t{}\n\t\t</h1>\n\t</body>\n</html>".format(self.varHTMLBodyText))
        #close html file
        htmlFile.close()
        #display html file in a new tab in default browser
        webbrowser.open("webpagegen.html",new=2,autoraise=True)



if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
