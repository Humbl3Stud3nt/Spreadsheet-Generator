# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:14:06 2018

@author: warat

Problem Statement: Design a command line program that accepts input and stores it in an excel spreasheet

"""

import openpyxl
from openpyxl.styles import NamedStyle, Font
import datetime
import club
# import os


def genSpreadsheet(memberList, directory=""):
    # ERROR HANDLING
    try:
        assert type(memberList) == list

    except AssertionError:
        print("memberList should be of type 'list'.")
        return 0

    for member in memberList:
        try:
            assert type(member) == club.Member

        except AssertionError:
            print("INCONSISTENT RECORDS\n"
                  "ABORTING SPREADSHEET CREATION")
            return 0

    clubName = memberList[0].club

    for member in memberList:
        try:
            assert member.club == clubName
        except AssertionError:
            print("INCONSISTENT CLUB\n"
                  "ABORTING SPREADSHEET CREATION")
            return 0

    wb = openpyxl.Workbook()

    sheet = wb.get_sheet_by_name("Sheet")

    def _indexToColumn(index):
        headerBases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        try:
            assert 0 <= index <= 26 and type(index) == int
        except AssertionError:
            print("Please limit number of attributes to 26")
            return 0

        return headerBases[index]

    attributes = club.Member().attributes

    titleFont = Font(bold=True, size=16)
    titleStyle = NamedStyle(font=titleFont)

    for i in range(len(attributes)):
        column = _indexToColumn(i)
        # print(column)
        sheet[column + "1"] = attributes[i]

        sheet.column_dimensions[column].width = 20

    for i in range(len(memberList)):
        row = str(i+2)
        sheet["A" + row] = memberList[i].firstName
        sheet["B" + row] = memberList[i].lastName
        sheet["C" + row] = memberList[i].form
        sheet["D" + row] = memberList[i].duesPaid

    currentDate = str(datetime.date.today())
    fileName = directory + clubName + "-" + currentDate + ".xlsx"

    wb.save(fileName)


clubList = []

for i in range(10):
    clubList.append(club.Member())

genSpreadsheet(clubList)
