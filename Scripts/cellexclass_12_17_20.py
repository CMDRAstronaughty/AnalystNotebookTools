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
from tkinter.filedialog import askopenfilename, asksaveasfilename
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
# Tkinter GUI - Written in class to allow for dynamic attribution
# =============================================================================
class myApp:
    importedSheets = []
    headers = []
    reports = ['Cellbrite','Axiom','XRY','Viking']
    df = None
    
    def UploadAction(self):
        self.filename = askopenfilename()
        
    def SaveAction(self,df):
        self.savelocation = asksaveasfilename(defaultextension = '.csv')
        df.to_csv(self.savelocation,index = False, header = True)
    
    def sheetnames(self):
        self.xlssheets = xlrd.open_workbook(self.filename,on_demand=True)
        importedSheets = self.xlssheets.sheet_names()
        self.cbox_sheets.config(value=importedSheets) #updating the value of the combobox
        return importedSheets
                   
    def headernames(self):
        if self.reporttype.get(self.reporttype.curselection()) == self.reports[0]:
            self.df = pd.read_excel(self.filename,sheet_name = self.cbox_sheets.get(),header = 1, index_col=0)
            headers = list(self.df.columns)
            self.headers_select.delete(0,'end')
            for x,header in enumerate(headers):
                self.headers_select.insert(x,header)
        # elif self.reporttype.get(self.reporttype.curselection()) == self.reports[1]: #If report is Axiom
        # elif self.reporttype.get(self.reporttype.curselection()) == self.reports[2]: #If report is XRY
        # elif self.reporttype.get(self.reporttype.curselection()) == self.reports[3]: #If report is Viking
    
    def ExtractAction(self):
        global df
        if self.cbox_sheets.get() == 'Call Log':
            self.df = pd.read_excel(self.filename,sheet_name = self.cbox_sheets.get(),header = 1, index_col=0)
            datedrop = self.df.drop(columns='Date')
            df = datedrop.dropna(axis='columns')
            df.insert(0,'From_Identifier','')
            df.insert(1,'From_Name','')
            df.insert(2,'To_Identifier','')
            df.insert(3,'To_Name','')
            df.insert(5,'Date','')
            df.insert(7,'Time_Zone','')
            
            df['From_Identifier'] = df['Parties'].str.extract(fromIdentifierRegex,expand = True)
            df['From_Identifier'] = df['From_Identifier'].str.extract(onlyNumbersRegex,expand=True)
            df['From_Identifier'].fillna('', inplace = True)
            
            df['To_Identifier'] = df['Parties'].str.extract(toIdentiferRegex,expand = True)
            df['To_Identifier'] = df['To_Identifier'].str.extract(onlyNumbersRegex,expand = True)
            df['To_Identifier'].fillna('', inplace = True)
            
            df['Date'] = df['Time'].str.extract(dateRegex,expand = True)
            
            df['Time_Zone'] = df['Time'].str.extract(TimeZoneRegex,expand = True)
            
            df['Time'] = df['Time'].str.extract(timeRegex,expand = True)
            
            df['From_Name'] = df['Parties'].str.extract(allFromRegex,expand = True)
            df['From_Name'] = [re.sub('From:  ','',str(x)) for x in df['From_Name']]
            df['From_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in df['From_Name']]
            df['From_Name'].replace('nan',np.nan, inplace = True)
                    
            df['To_Name'] = df['Parties'].str.extract(allToRegex,expand = True)
            df['To_Name'] = [re.sub('To:  ','',str(x)) for x in df['To_Name']]
            df['To_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in df['To_Name']]
            df['To_Name'].replace('nan', np.nan, inplace = True)
            
            df.drop('Parties',axis=1,inplace=True)
            return df
            
    def __init__(self,master):
        self.filename = None
        self.master = master
        master.title('E.D.N.A. - Extraction of Data for Notebook Analysis')
        master.geometry('540x670')
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
                                text = '1) Select the file you want to import',
                                font=(None,12,'bold')).pack()
        
        self.uploadButton = Button(master = self.frame2a,
                                   text = 'Import',
                                   command = lambda:self.UploadAction()).pack(padx=5,pady=5)
        
        self.reporttype = Listbox(master=self.frame2a,height=4,selectmode=SINGLE,exportselection = False)
        for x,reports in enumerate(self.reports):
            self.reporttype.insert(x,reports)
        
        self.reporttype.pack(padx=5,pady=5)
        #---------------------------------------------------------------------#
        # Selecting Sheets to work with:
        #---------------------------------------------------------------------#
        self.sheetLabel = Label(master = self.frame2b,
                                text = '2) Select the sheet to extract',
                                font=(None,12,'bold')).pack(padx=15)
        
        self.cbox_sheets = Combobox(master = self.frame2b,
                                    values = self.importedSheets,
                                    postcommand = self.sheetnames)
        self.cbox_sheets.pack(padx=5,pady=5)
        
        #---------------------------------------------------------------------#
        # Selecting Headers to Work with:
        #---------------------------------------------------------------------#
        self.headerLabel = Label(master = self.frame2r,
                                  text = '3) Select the header with data',
                                  font=(None,12,'bold')).pack(padx=15)
            
        self.headers_button = Button(master = self.frame2r, text = 'Show Headers',command = self.headernames).pack(padx=5,pady=5)
        self.headers_select = Listbox (master = self.frame2r,exportselection = False,selectmode=MULTIPLE)
        self.headers_select.pack(padx=5,pady=5)
        
        #---------------------------------------------------------------------#
        # Frame 3 - Extract The Data
        #---------------------------------------------------------------------#
        self.frame3a = Frame(master = self.frame3)
        self.frame3b = Frame(master = self.frame3)
        
        self.frame3a.pack()
        self.frame3b.pack()
            
        self.extractlabel = Label (master=self.frame3a,
                                   text = '4) Extract File & Data to CSV',
                                   font=(None,12,'bold')).pack(padx=5,pady=5)
        
        self.extractbutton = Button(master=self.frame3a,
                                    text = 'Extract',
                                    command = lambda:self.ExtractAction()).pack(padx=5,pady=5)
        
        self.saveLocationLabel = Label(master=self.frame3b,
                                text = '5) Save Location Select',
                                font=(None,12,'bold')).pack(padx=5,pady=5)
        
        self.savebutton = Button(master=self.frame3b,
                                  text = 'Save',
                                  command=lambda:self.SaveAction(df)).pack(padx=5,pady=5)
              
if __name__ == '__main__':
    root = Tk()
    my_gui = myApp(root)
    root.mainloop()