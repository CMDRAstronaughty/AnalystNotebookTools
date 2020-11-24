'''
Analyst Notebook Cleaner Tool GUI
Developed by: J24 - Intelligence Data Science Team (IDST)
Deverloper: Sai Myint, Data Analyst - IDST
Version: V-1.0(A)

Module: NotebookCleaner.py
'''
def UploadAction(event=None):
    tkinter.filedialog.askopenfilename()
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
root.geometry('500x500')
root.resizable(False,False)
root.iconbitmap('D:\Documents\IDSTProjects\AnalystNotebok\Images\edna.ico')

# ===================================================
# Title Layout Section (Buttons, Text & Objects)
# ===================================================
#topFrame = Frame(master=root,relief=RAISED,borderwidth=1)
#topFrame.pack(side=TOP)

appTitle = Label(master=root,text='U.S. Special Operations Command',font=(None,20))
jdogTitle = Label(master=root,text='Joint Document & Media Exploitation Group (JDOG)',font=(None,11))
idstTitle = Label(master=root,text='Intelligence Data Science Team (IDST)',font=(None,11))
blankspace1 = Label(master=root,text='')
blankspace2 = Label(master=root,text='')
appTitle.pack()
jdogTitle.pack()
idstTitle.pack()
blankspace1.pack()
blankspace2.pack()

# ===================================================
# Second Frame Section - Import Button
# ===================================================
secondFrame = Frame(master=root,relief=RAISED,borderwidth=1)
secondFrame.pack()

importLabel = Label(master = secondFrame,text='Select the file you would like to ingest:', font=(None,12))
importButton = Button (master = secondFrame,text='Import',command=UploadAction,compound=RIGHT)
blankspace3 = Label(master=secondFrame,text='')
blackspace31 = Label(master=root,text='')

importLabel.pack()
importButton.pack()
blankspace3.pack()
blackspace31.pack()
# ===================================================
# Middle Frame Section - Extraction Type Radio Button
# ===================================================
middleFrame = Frame(master=root,relief=RAISED,borderwidth=1)
middleFrame.pack()

v = IntVar()

testLabel = Label(master=middleFrame,text="Select the CELLEX Data you would like to extract:",font=(None,12),wraplength=278)
callLog = Radiobutton(master = middleFrame,text='Call Logs', variable=v,value=1)
SMS = Radiobutton(master = middleFrame,text='SMS/MMS', variable=v,value=2)
Chats = Radiobutton(master = middleFrame,text='Chats', variable=v,value=3)
Contacts = Radiobutton(master = middleFrame,text='Contacts', variable=v,value=4)

testLabel.pack()
callLog.pack()
SMS.pack()
Chats.pack()
Chats.pack()
Contacts.pack()

blankspace4 = Label(master=root,text='').pack()
blankspace5 = Label(master=root,text='').pack()

# ===================================================
# Bottom Frame Section - File Save Location - Submit
# ===================================================
rightFrame = Frame(master=root,relief=RAISED,borderwidth=1)
rightFrame.pack()

submitButton = Button(master=rightFrame,text='Extract!')
submitButton.pack()

# ===================================================
# Running Root window for loop
# ===================================================
if __name__ == '__main__':
    root.mainloop()