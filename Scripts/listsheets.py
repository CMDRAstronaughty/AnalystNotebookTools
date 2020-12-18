import pandas as pd
import os
from tkinter.filedialog import askopenfilename
import tkinter as tk
import xlrd

# Step 1. Load File
root = tk.Tk()
importedFile = askopenfilename()

#Empty List of Sheets
sheets = []

#Retrieve Sheetnames
mySheets = xlrd.open_workbook(importedFile,on_demand=True)
print (mySheets.sheet_names())