'''
Analyst Notebook Cleaner Tool GUI
Developed by: J24 - Intelligence Data Science Team (IDST)
Deverloper: Sai Myint, Data Analyst - IDST
Version: V-1.0(A)

Module: NotebookCleaner.py
'''
# ===================================================
# Importing Libraries
# ===================================================
from tkinter import *
import tkinter
import NotebookCleaner

# ===================================================
# Creating base 'root' window
# ===================================================
root = Tk()
root.title("E.D.N.A - Extraction of Data for Notebook Analysis")
root.geometry('600x350')
root.configure(bg='grey')

# ===================================================
# Title Layout Section (Buttons, Text & Objects)
# ===================================================
topFrame = Frame(master=root)
topFrame.pack(side=TOP)

appTitle = Label(master=topFrame,text='U.S. Special Operations Command',bg='grey',fg='yellow',font=(None,20))
jdogTitle = Label(master=topFrame,text='Joint Document & Media Exploitation Group (JDOG)',bg='grey',fg='yellow',font=(None,11))
idstTitle = Label(master=topFrame,text='Intelligence Data Science Team (IDST)',bg='grey',fg='yellow',font=(None,11))

appTitle.pack(fill=X)
jdogTitle.pack(fill=X)
idstTitle.pack(fill=X)
# ===================================================
# Left Frame Section
# ===================================================
leftFrame = Frame(master=root)
leftFrame.pack(side=LEFT)

importLabel = Label(master = leftFrame,text='Select the file you would like to ingest:',bg='grey',fg='white', font=(None,12))
importButton = Button (master = leftFrame,text='Import',command=tkinter.filedialog.askopenfilename,compound=RIGHT)

importLabel.pack()
importButton.pack()
# ===================================================
# Middle Frame Section
# ===================================================
middleFrame = Frame(master=root)
middleFrame.pack(side=LEFT)

testLabel = Label(master=middleFrame,text="This is just a filler", bg='white',font=(None,12))
testLabel.pack()
# ===================================================
# Right Frame Section
# ===================================================
rightFrame = Frame(master=root)
rightFrame.pack(side=BOTTOM)

submitButton = Button(master=rightFrame,text='Extract!')
submitButton.pack()
# ===================================================
# Running Root window for loop
# ===================================================
if __name__ == '__main__':
    root.mainloop()