'''
CELLEX Data Extractor
Developed by: J24-IDST
Developer: Sai Myint, CTR, Data Analyst

Version: 1.10.1

Developer Note:
    - This script has been written using packages only available on Anaconda
    - This script can be ran in any IDE or text editor
    - This script is not meant to be used as a module, this is stand-alone
'''
# =============================================================================
# Importint Basic Libraries
# =============================================================================
import pandas as pd
import os
import xlrd
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import tkinter as tk
import re
import numpy as np

# =============================================================================
# Basic Regexes - Need to update it to not use REGEX's for Future Proof
# =============================================================================
toIdentiferRegex = r"(\w[To]\W\s{2}\S\d{6,11})"
fromIdentifierRegex = r"(\w{4}\W\s{2}\S\d{6,11})"
allToRegex = r"(^\w{2}\W\s{2}...{2,30})"
allFromRegex = r"(\w{4}\W\s{2}...{2,30})"
onlyNumbersRegex = r"(\S\d{6,11})"
dateRegex = r"([\d]{1,2}/[\d]{1,2}/[\d]{4})"
timeRegex = r"(\d{1,2}\:\d{1,2}\:\d{1,2}\s\w+)"
TimeZoneRegex = r"(UTC[+]\d)"

# =============================================================================
# Global Variables
# =============================================================================
importedSheets = []
headers = []
us_sheet = None
us_headers = []
extractselect = None
deviceIMEI = None
df = None
filename = None

# =============================================================================
# Functions
# =============================================================================
def UploadAction(event=None):
    global filename
    filename = askopenfilename()
    
    
def sheetnames(filepath = filename):
    """
    
    
    Parameters
    ----------
    filepath : String, optional
        DESCRIPTION. The default is filename. Full file path of import

    Returns
    -------
    sheetnames.
    
    """
    global importedSheets
    xlssheets = xlrd.open_workbook(filepath,on_demand=True)
    importedSheets = xlssheets.sheet_names()

def headers(filepath = filename,us_sheet=us_sheet):
    """
    
    
    Parameters
    ----------
    filepath : String, optional
        Full file path of xls(x) file to import.
    us_sheet : String, optional
        User selected sheet to extract from.

    Returns
    -------
    Headers of sheetname.

    """
    df = pd.read_excel(filepath,sheet_name = us_sheet,header = 1,
                       index_col=0)
    return list(df.columns),df

def CallLog():
    """


    Returns
    -------
    calllog_df : DataFrame
        Extracted Call Log DataFrame.

    """
    calllog_df = df[df.columns.intersection(us_headers)]
    calllog_df.insert(0,'From_Identifier','')
    calllog_df.insert(1,'From_Name','')
    calllog_df.insert(2,'To_Identifier','')
    calllog_df.insert(3,'To_Name','')
    calllog_df.insert(5,'Date','')
    calllog_df.insert(7,'Time_Zone','')
    
    calllog_df['From_Identifier'] = calllog_df['Parties'].str.extract(fromIdentifierRegex,expand = True)
    calllog_df['From_Identifier'] = calllog_df['From_Identifier'].str.extract(onlyNumbersRegex,expand=True)
    calllog_df['From_Identifier'].fillna('', inplace = True)
    
    calllog_df['To_Identifier'] = calllog_df['Parties'].str.extract(toIdentiferRegex,expand = True)
    calllog_df['To_Identifier'] = calllog_df['To_Identifier'].str.extract(onlyNumbersRegex,expand = True)
    calllog_df['To_Identifier'].fillna('', inplace = True)
    
    calllog_df['Date'] = calllog_df['Time'].str.extract(dateRegex,expand = True)
    
    calllog_df['Time_Zone'] = calllog_df['Time'].str.extract(TimeZoneRegex,expand = True)
    
    calllog_df['Time'] = calllog_df['Time'].str.extract(timeRegex,expand = True)
    
    calllog_df['From_Name'] = calllog_df['Parties'].str.extract(allFromRegex,expand = True)
    calllog_df['From_Name'] = [re.sub('From:  ','',str(x)) for x in calllog_df['From_Name']]
    calllog_df['From_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in calllog_df['From_Name']]
    calllog_df['From_Name'].replace('nan',np.nan, inplace = True)
    
    calllog_df['To_Name'] = calllog_df['Parties'].str.extract(allToRegex,expand = True)
    calllog_df['To_Name'] = [re.sub('To:  ','',str(x)) for x in calllog_df['To_Name']]
    calllog_df['To_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in calllog_df['To_Name']]
    calllog_df['To_Name'].replace('nan', np.nan, inplace = True)
    
    calllog_df.drop('Parties',axis=1,inplace=True)  
    return calllog_df

# =============================================================================
# Tkinter GUI
# =============================================================================
root = Tk()
root.title("E.D.N.A - Extraction of Data for Notebook Analysis")
root.geometry('600x600')
# root.resizable(False,False)
root.iconbitmap('D:\Documents\IDSTProjects\AnalystNotebok\Images\edna.ico')
# =============================================================================
# Creating Frames for Objects & Labels
# =============================================================================
Frame1 = Frame(master = root,relief=RAISED,borderwidth=1)
Frame2 = Frame(master = root,relief=RAISED,borderwidth=1)
Frame3 = Frame(master = root,relief=RAISED,borderwidth=1)

Frame1.pack(padx=10,pady=10)
Frame2.pack(padx=10,pady=10)
Frame3.pack(padx=10,pady=10)
# =============================================================================
# Frame 1 - Title & Logo Frame
# =============================================================================
appTitle = Label(master=Frame1,text='U.S. Special Operations Command',font=(None,20,'bold'))
jdogTitle = Label(master=Frame1,text='Joint Document & Media Exploitation Group (JDOG)',font=(None,11))
idstTitle = Label(master=Frame1,text='Intelligence Data Science Team (IDST)',font=(None,11))

appTitle.grid(row=0,column=1)
jdogTitle.grid(row=1,column=1)
idstTitle.grid(row=2,column=1)
# =============================================================================
# Frame 2 - Import, Sheet & Header Selections
# =============================================================================
Frame2A = Frame(master = Frame2)
Frame2B = Frame(master = Frame2)
Frame2C = Frame(master = Frame2)
Frame2A.pack(side=TOP)
Frame2B.pack(side=LEFT)
Frame2C.pack(side=RIGHT)

ImportLabel = Label(master=Frame2A,text='Select the file you want to import',font=(None,11,'bold'))
ImportButton = Button(master=Frame2A,text='Import',command=UploadAction)

ImportLabel.grid(row=0,column=1)
ImportButton.grid(row=1,column=1)

show_sheets = Button (master = Frame2B,
                      text = 'Show Sheets',
                      command = lambda:sheetnames(filename)).pack()

#Creat Comobobox
n = StringVar()
sheetchosen = Combobox(Frame2B,values=importedSheets)
sheetchosen.pack()
# =============================================================================
# Frame 3 - Extract & Save
# =============================================================================









# =============================================================================
# Tkinter Loop
# =============================================================================
if __name__ == '__main__':    
    root.mainloop()
















