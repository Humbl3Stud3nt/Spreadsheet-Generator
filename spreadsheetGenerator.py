# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:14:06 2018

@author: warat

Problem Statement: Design a command line program that accepts input and stores it in an excel spreasheet

"""

import openpyxl
import datetime
#import os


def genSpreadsheet(spreadsheetTitle, titles):
    """
    Creates a spreadsheet and populates it with titles
    
    spreadsheetTitle -> title of spreadsheet
    titles -> list of titles for spreadsheet; for now must be 26 or fewer titles
    """
    
    # ensures that titles is a list or tuple
    
    try:
        assert type(titles) == list or type(titles) == tuple
        
    except:
        print("Please use a list or tuple")
        return None
     
    # ensures that there are 26 or fewer elements in titles        
    try:
        assert len(titles) <= 26
        
    except:
        print("Limit number of titles to 26")
        return None
    
    
    wb = openpyxl.Workbook()
    
    sheet = wb.get_sheet_by_name("Sheet")
    
    
    columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for index in range(0,len(titles)):
        sheet[columns[index] + "1"] = titles[index]
        
    currentDate = str(datetime.date.today())
    fileName = currentDate + ".xlsx"
    
    wb.save(fileName)

