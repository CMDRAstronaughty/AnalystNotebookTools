'''
Analyst Notebook Cleaner Tool
Developed by: J24 - Intelligence Data Science Team (IDST)
Deverloper: Sai Myint, Data Analyst - IDST
Version: V-1.0(A)

Module - CLeanerGUI.py
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
From_name = r"\b(?!\From\b)\b(?!\To\b)\b(?!\S\d{6,11}\b)\w.*"
onlyNumbersRegex = r"(\S\d{6,11})"
# =============================================================================
# Defining Functions for use throughout
# =============================================================================
def readExcel(userFileImport):
    '''
    This function will read excel reports based off user file import
    Param:
    - userFileImport (str): Full filepath of user file
    '''
    return pd.read_excel(userFileImport, sheet_name='Call Log',header=1,index_col=0)
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
    return args['To_Identifier']




















