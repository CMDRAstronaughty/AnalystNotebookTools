'''
Analyst Notebook Cleaner Tool
Developed by: J24 - Intelligence Data Science Team (IDST)
Deverloper: Sai Myint, Data Analyst - IDST
Version: V-1.0(A)

V1.0 : Tested with Cellbrite Reports
+++++++++++++++++++++++++++++++++++++++++++++++++++
Module - CLeanerGUI.py
===================================================
Written in Python 3.8 (Anaconda Distributable)
===================================================
License: NONE
===================================================
'''

# =============================================================================
# Importing Basic Libraries
# =============================================================================
import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re

# =============================================================================
# Regexes
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
# Defining Functions for use throughout
# =============================================================================
def readExcel(userFileImport):
    '''
    This function will read excel reports based off user file import
    Param:
    - userFileImport (str): Full filepath of user file
    '''
    df = pd.read_excel(userFileImport, sheet_name='Call Log',header=1,index_col=0)
    return df
def dropColumns(importedFile):
    '''
    Parameters
    ----------
    importedFile : DATAFRAME
        DROPS ANY COLUMNS WITH MISS OR EMPTY VALUES FOR SORTING
    Returns
    -------
    None.

    '''
    dateDrop = importedFile.drop(columns='Date')
    naDrop = dateDrop.dropna(axis = 'columns')
    naDrop.insert(0,'From_Identifier','')
    naDrop.insert(1,'From_Name','')
    naDrop.insert(2,'To_Identifier','')
    naDrop.insert(3,'To_Name','')
    naDrop.insert(5,'Date','')
    naDrop.insert(7,'Time_Zone','')
    return naDrop
def fromIdentifier(args):
    '''
    Parameters
    ----------
    args : DATAFRAME
        USES fromIdentifierRegex to pull from: numbers.
    Returns
    -------
    None
    '''
    args['From_Identifier'] = args['Parties'].str.extract(fromIdentifierRegex,expand = True)
    args['From_Identifier'] = args['From_Identifier'].str.extract(onlyNumbersRegex,expand=True)
    args['From_Identifier'].fillna('', inplace = True)
    return args['From_Identifier']
def toIdentifier(args):
    """
    Parameters
    ----------
    args : DATAFRAME
        Uses toIdentiferRegex to pull numbers and puts them in their
        own column in the dataframe.
    Returns
    -------
    None.
    """
    args['To_Identifier'] = args['Parties'].str.extract(toIdentiferRegex,expand = True)
    args['To_Identifier'] = args['To_Identifier'].str.extract(onlyNumbersRegex,expand = True)
    args['To_Identifier'].fillna('', inplace = True)
    return args['To_Identifier']
def dateParser (args):
    """
    Parameters
    ----------
    args : Column/Row for a Dataframe
        Splits the Date Time Group into its
        respective column/row.
    Returns
    -------
    Dataframe.
    """
    args['Date'] = args['Time'].str.extract(dateRegex,expand = True)
    return args['Date']
def timeZoneParser (args):
    """
    Parameters
    ----------
    args : Column/Row of a Dataframe
        Takes the UTC+ of a DTG group and puts it
        in the Timezone Column.
    Returns
    -------
    Dataframe.
    """
    args['Time_Zone'] = args['Time'].str.extract(TimeZoneRegex,expand = True)
    return args['Time_Zone']
def timeParser (args):
    """    
    Parameters
    ----------
    args : Column/Row of a Dataframe
        This function will take the time HH:MM:SS AM/PM and
        put it in the time column.
    Returns
    -------
    Dataframe
    """
    args['Time'] = args['Time'].str.extract(timeRegex,expand = True)
    return args['Time']
def fromName (args):
    """
    Parameters
    ----------
    *args : DATAFRAME
        Takes <name> from [From: #### <name>]
        and puts it in the From_Name column.
    Returns
    -------
    DataFrame.
    """
    args['From_Name'] = args['Parties'].str.extract(allFromRegex,expand = True)
    args['From_Name'] = [re.sub('From:  ','',str(x)) for x in args['From_Name']]
    args['From_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in args['From_Name']]
    args['From_Name'].replace('nan',np.nan, inplace = True)
    return args['From_Name']
def toName (args):
    """
    Parameters
    ----------
    args : DATAFRAME (STR)
        Takes <name> from .
    Returns
    -------
    None.
    """
    args['To_Name'] = args['Parties'].str.extract(allToRegex,expand = True)
    args['To_Name'] = [re.sub('To:  ','',str(x)) for x in args['To_Name']]
    args['To_Name'] = [re.sub(r'\S\d{6,11}\s','',str(x)) for x in args['To_Name']]
    args['To_Name'].replace('nan', np.nan, inplace = True)
    return args['To_Name']
def dropParties(args):
    return args.drop('Parties',axis=1,inplace=True)
def saveCSV(file):
    """
    Parameters
    ----------
    file : variable to pass into saving to CSV
        Saves panda dataframe to CSV.
    Returns
    -------
    None.
    """
    userFileSave = asksaveasfilename(defaultextension = '.csv')
    file.to_csv(userFileSave,index = False, header = True)

