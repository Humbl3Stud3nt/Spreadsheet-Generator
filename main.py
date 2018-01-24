# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:34:02 2018

@author: warat
"""
import spreadsheetGenerator

NAME_QUERY = "Enter name of member: "
FORM_QUERY = "Enter member form in format <grade level>-<class number>:\n"
DUES_QUERY = "Enter dues given this meeting: $"

TITLES = ("FIRST NAME", "LAST NAME", "FORM", "DUES")

global memberList
memberList = []


class Member:
    def __init__(self, **kwargs):
        self.club = kwargs["club"]
        name = kwargs["name"].split(" ")
        self.firstName = name[0].capitalize()
        self.lastName = name[1].capitalize()
        self.duesPaid = kwargs["duesPaid"]
        self.form = kwargs["form"]


def genMember(infoDict):

    global memberList
    memberList.append(Member(infoDict))


def main():
    pass

    
if __name__ == "__main__":
    main()
                
            
    