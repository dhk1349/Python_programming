# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:25:35 2019

@author: dhk1349
"""

class Register:
    def __init__(self, length):
        self.State=['Wait']*length
        self.Status='Proceed'
        self.Order=""
        
    def StatusCheck(self):
        if 'Fail' not in self.State and 'Wait' not in self.State:
            self.Status='Success'
        elif "Wait" not in self.State:
            self.Status='Fail'
        elif 'Wait' in self.State:
            self.Status='Proceed'
        else:
            self.State='unexpected case'
            
    def ResetFail(self):
        for i in range(len(self.State)):
            if self.State[i]=='Fail':
                self.State[i]='Wait'
    
    def CheckSuccess(self, index):
        self.State[index]='Success'
        self.Order=self.Order+"  "+str(index)
        self.StatusCheck()

    def FinalCheck(self):
        if self.Status=="Proceed":
            self.Status='Fail'
        if self.Status=="Fail":
            self.Order=""
    def GetStatus(self):
        return self.Status
    
    def GetState(self):
        return self.State
    
    def GetOrder(self):
        return self.Order
    
    def PrintInfo(self):
        for i in self.State:
            print(i)

#if __name__=="__main__":
#    reg=Register(3)
#    reg.PrintInfo()
            
    """            
    input_lst=['Fail','Wait','Fail','Success','Fail']
    def StatusCheck(State):
        if 'Fail' not in State and 'Wait' not in State:
            Status='Success'
        elif "Wait" not in State:
            Status='Fail'
        elif 'Wait' in State:
            Status='proceed'
        else:
            Status='unexpected case'
        print(Status)
    StatusCheck(input_lst)
    """