'''
Analyst Notebook Cleaner Tool GUI
Developed by: J24 - Intelligence Data Science Team (IDST)
Deverloper: Sai Myint, Data Analyst - IDST
Version: V-1.0(A)

Module: NotebookCleaner.py
'''

import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from NotebookCleaner import dropColumns,readExcel, fromToIdentifier

root = tk.Tk()
root.withdraw()

userFileImport = askopenfilename()
fileType = os.path.splitext(userFileImport)[1]
x = dropColumns(readExcel(userFileImport))

fromID = fromToIdentifier(x)