# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:16:23 2018

@author: warat
implements spreadsheetGenerator to generate weekly attendance reports including:
    date of meeting
    name of member
    dues paid at this meeting
    class
"""
        

class Member:
    def __init__(self, **kwargs):
        name = kwargs["name"].split(" ")
        self.firstName = name[0].capitalize()
        self.lastName = name[1].capitalize()
        self.duesPaid = kwargs["duesPaid"]
        self.form = kwargs["form"]