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
# toIdentiferRegex = r"(\w[To]\W\s{2}\S\d{6,11})"
# fromIdentifierRegex = r"(\w{4}\W\s{2}\S\d{6,11})"
# allToRegex = r"(^\w{2}\W\s{2}...{2,30})"
# allFromRegex = r"(\w{4}\W\s{2}...{2,30})"
# onlyNumbersRegex = r"(\S\d{6,11})"
# dateRegex = r"([\d]{1,2}/[\d]{1,2}/[\d]{4})"
# timeRegex = r"(\d{1,2}\:\d{1,2}\:\d{1,2}\s\w+)"
# TimeZoneRegex = r"(UTC[+]\d)"

# =============================================================================
# Tkinter GUI - Written in class to allow for dynamic attribution
# =============================================================================
class myApp:
    importedSheets = []
    us_sheets = None
    headers = []
    us_headers = None
    
    def UploadAction(self):
        self.filename = askopenfilename()
    
    def sheetnames(self):
        self.xlssheets = xlrd.open_workbook(self.filename,on_demand=True)
        importedSheets = self.xlssheets.sheet_names()
        self.cbox_sheets.config(value=importedSheets) #updating the value of the combobox
        return importedSheets
            
    def showsheets(self):
        return self.importedSheets()
    
    # def headernames(self):
    #     self.df = pd.read_excel(self.filename,sheet_name = )
    
    def __init__(self,master):
        self.filename = None
        self.master = master
        master.title('E.D.N.A. - Extraction of Data for Notebook Analysis')
        master.geometry('600x600')
        master.iconbitmap('D:\Documents\IDSTProjects\AnalystNotebok\Images\edna.ico')
        #---------------------------------------------------------------------#
        # Creating Basic Frame Structure
        #---------------------------------------------------------------------#
        self.frame1 = Frame(master=master,relief=RAISED,borderwidth=1)
        self.frame1.pack(padx=10,pady=10)
        
        self.frame2 = Frame(master=master,relief=RAISED,borderwidth=1)
        self.frame2.pack(padx=10,pady=10)
        
        self.frame3 = Frame(master=master,relief=RAISED,borderwidth=1)
        self.frame3.pack(padx=10,pady=10)
        #---------------------------------------------------------------------#
        # Frame 1 - Basic Titles for Application
        #---------------------------------------------------------------------#
        self.socom = Label(master=self.frame1,
                           text='U.S. Special Operations Command (USSOCOM)',
                           font=(None,14,'bold'))
        self.socom.pack()

        self.jdog = Label(master=self.frame1,
                          text='Joint Document & Media Exploitation Group (JDOG)',
                          font=(None,12))       
        self.jdog.pack()
    
        self.idst = Label(master=self.frame1,
                          text='Intelligence Data Science Team (IDST)',
                          font=(None,12))      
        self.idst.pack()
        #---------------------------------------------------------------------#
        # Frame 2 - Selecting Sheet and Header To Work with
        #---------------------------------------------------------------------#
        self.frame2a = Frame(master = self.frame2)
        self.frame2b = Frame(master = self.frame2)
        self.frame2r = Frame(master = self.frame2)
        self.frame2a.pack(side=TOP)
        self.frame2b.pack(side=LEFT)
        self.frame2r.pack(side=RIGHT)
        
        self.uploadLabel = Label(master = self.frame2a,
                                text = 'Select the file you want to import',
                                font=(None,12)).pack()
        self.uploadButton = Button(master = self.frame2a,
                                   text = 'Import',
                                   command = lambda:self.UploadAction()).pack()
        #---------------------------------------------------------------------#
        self.sheetLabel = Label(master = self.frame2b,
                                text = 'Select the sheet to extract',
                                font=(None,12)).pack(padx=15)
        
        # self.showsheets = Button (master = self.frame2b,
        #                           text = 'Extract Sheets',
        #                           command = self.sheetnames).pack()
        
        self.cbox_sheets = Combobox(master = self.frame2b,
                                    values = self.importedSheets,
                                    postcommand = self.sheetnames)
        self.cbox_sheets.pack()
        #---------------------------------------------------------------------#
        self.headerLabel = Label(master = self.frame2r,
                                  text = 'Select the header with data',
                                  font=(None,12)).pack(padx=15)
        
        #---------------------------------------------------------------------#
        # Frame 3 - Extract The Data
        #---------------------------------------------------------------------#

if __name__ == '__main__':
    root = Tk()
    my_gui = myApp(root)
    root.mainloop()
















