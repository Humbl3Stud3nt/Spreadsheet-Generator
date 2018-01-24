# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:34:02 2018

@author: warat
"""
import scienceClub
import spreadsheetGenerator

NAME_QUERY = "Enter name of member: "
FORM_QUERY = "Enter member form in format <grade level>-<class number>:\n"
DUES_QUERY = "Enter dues given this meeting: $"

TITLES = ("FIRST NAME", "LAST NAME", "FORM", "DUES")

memberList = []

class Prompt():
    """
    base class for Prompts
    """
    def __init__(self, query, data=None):
        self.query = query
        self.data = data
    
    def getInfo(self):
        self.data = (input(self.query))
        return self.data
    
    def checkCondition(self):
        """
        Overwrite me
        Returns result of checkCondition
        """
        # if <condition>:
        #   return self.data
        # else:
        #   return checkCondition(self.getInfo())
        return None

    def exitEntry(self):
        """
        Overwrite me
        handles special cases where input triggers ending of the loop
        """
        return False
    
    
class NamePrompt(Prompt):
    def __init__(self, query=NAME_QUERY, data=None):
        Prompt.__init__(self, query, data)
        
    def exitEntry(self):
        if self.getInfo() == "":
            return True
        else:
            return False
        
    def checkCondition(self, data):
        if type(data) == str and " " in data and data.index(" ") != 0:
            return self.data
        else:
            data = self.getInfo()
            return self.checkCondition(data)


class FormPrompt(Prompt):
    def __init__(self, query=FORM_QUERY, data=None):
        Prompt.__init__(self, query, data)
        
    def checkCondition(self):
        # return self.getInfo()[0].isnumeric() and self.getInfo()[1] == "-" and self.getInfo()[2].isnumeric()
        return self.data[0].isnumeric() and self.data[1] == "-" and self.data[2].isnumeric()
        if self.data[0].isnumeric() and self.data[1] == "-" and self.data[2].isnumeric():
            return self.data
        else:
            self.getInfo()
            return self.checkCondition()


class DuesPrompt(Prompt):
    def __init__(self, query=DUES_QUERY, data=None):
        Prompt.__init__(self, query, data)
        
    def checkCondition(self):
        # return type(self.getInfo()) == int or type(self.getInfo())
        if (type(self.data) == int or type(self.data) == float) and self.data >= 0:
            return self.data
        else:
            self.getInfo()
            return self.checkCondition()


def infoPrompt(*prompts):
    allInfo = ()

    def infoIter(prompt):
        response = prompt.checkCondition(prompt.getInfo())

        if prompt.exitEntry():
            if exitQuery():
                return 0
        else:
            return response

    for prompt in prompts:
        info = infoIter(prompt)
        if info == 0:
            return 0
        allInfo += (info,)
    return allInfo 
            
        
def exitQuery(flag=False):
    exitCommand = input("Are you sure you want to exit? Yes/No\n")
    if exitCommand.lower() == "yes":
        flag = True
        return flag
    elif exitCommand.lower() == "no":
        flag = False
        return flag
    else:
        print("Enter either Yes or No.")
        return(exitQuery())
        

def main():
    print("To exit, when prompted for member name, leave the entry-field blank.\n\n")
    
    while True:

        info = infoPrompt(NamePrompt(), FormPrompt(), DuesPrompt())
        
        if info == 0:
            break
        
        else:
            infoDict = {"name":info[0], "form":info[1], "duesPaid":info[2]}
            memberList.append(scienceClub.Member(infoDict))
            
            
            
    
if __name__ == "__main__":
    main()
                
            
    