# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:40:24 2019

@author: dhk1349
"""
class Resource:
    def __init__(self,name, num):
        self.Name=name
        self.InstanceNum=num
        self.CurNum=num
        
    def CheckUseResource(self, num):
        if self.InstanceNum-num!=0:
            #self.CurNum-=num
            return 1
        else:
            return 0 
           
    def UseResource(self, num):
        if self.InstanceNum-num!=0:
            self.CurNum-=num
            return 1
        else:
            return 0
    
    def AddResource(self, num):
        self.CurNum+=num
        return self.CurNum
    
    def GetName(self):
        return self.Name
    
    def GetMaxResource(self):
        return self.InstanceNum
    
    def GetCurResource(self): #remaining Resource
        return self.CurNum
    
class Process:
    def __init__(self,name, max_lst):
        self.Name=name
        self.MaxList=max_lst
        self.CurrentList=[0]*len(max_lst)
    
    def CheckAllocate(self, lst):
        for i in range(len(self.MaxList)):
            if self.CurrentList[i]+lst[i]>self.MaxList[i]:
                return 0
        #for i in range(len(self.MaxList)):
        #    self.CurrentList[i]+=lst[i]
        return 1
    
    def Allocate(self, lst):
        for i in range(len(self.MaxList)):
            if self.CurrentList[i]+lst[i]>self.MaxList[i]:
                return 0
        for i in range(len(self.MaxList)):
            self.CurrentList[i]+=lst[i]
        return 1
    
    def ReleaseResources(self):
        temp=self.CurrentList
        self.CurrentList=[0]*len(self.MaxList)
        return temp
    
    def GetName(self):
        return self.Name
    
    def GetCurrentState(self):
        return self.CurrentList
    
    def GetMaxResource(self):
        return self.MaxList
        
#if __name__=="__main__":
