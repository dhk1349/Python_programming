#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:22:28 2019

@author: donghoon
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
        
    def GetStatus(self):
        return self.Status
    
    def GetState(self):
        return self.State
    
    def GetOrder(self):
        return self.Order
    
    def PrintInfo(self):
        for i in self.State:
            print(i)
            
class Manager:
    def __init__(self, ResourceLst, ProcessLst):
        #Requirement: resource list in process obj has to be
        #same order wirh resource list list in Manager obj
        self.Resources=ResourceLst
        self.Processes=ProcessLst
        self.Register=Register(len(ProcessLst))

    def GetResource(self, name):
        for i in range(len(self.Resources)):
            if self.Resources[i].GetName()==name:
                return self.Resources[i], i
        return None, None
    
    def GetProcess(self, name):
        for i in range(len(self.Processes)):
            if self.Processes[i].GetName()==name:
                return self.Processes[i],i
        return None,None
           
    def ResourceRequest(self,processname, instnums): #return 1 if succeed
        #check if resource can is suficient
        for i in range(len(instnums)):
            if (self.Resources[i].CheckUseResource(instnums[i])==0):
                return 0   
        for i in range(len(instnums)):
            self.Resources[i].UseResource(instnums[i])
        #bring process and check
        process,Null=self.GetProcess(processname)
        if process==None:
            return 0
        return process.Allocate(instnums)
    
    def PrintInfo(self):
        for i in self.Resources:
            print(i.GetName())
            print(i.GetCurResource())
        for i in self. Processes:
            print(i.GetName())
            print(i.GetCurrentState())
    def GetRegInfo(self):
        print (self.Register.GetStatus())
        print (self.Register.GetOrder())
        
    def SafetyCheck(self, processname):
        
        #Recursive function
        
        NeedList=[]
        (process,index)=self.GetProcess(processname)
        for i in range(len(process.GetMaxResource())):
            NeedList.append(process.GetMaxResource()[i]-process.GetCurrentState()[i])
        ###
        print("comparing")
        for i in range(len(NeedList)):
            print (NeedList[i], " and ", self.Resources[i].GetCurResource())
        ###
        #Compare with available list
        #if not enough return 0 and exit
        for i in range(len(NeedList)):
            if NeedList[i]>self.Resources[i].GetCurResource():
                print(processname, " returned 0")
                return 0
        
        #Can safely execute this proccess
        templist=process.ReleaseResources()
        print(processname, " success")
        print("available")
        for i in range(len(self.Resources)):
            print(self.Resources[i].AddResource(templist[i]))
        self.Register.CheckSuccess(index)
        
        print(self.Register.GetStatus())

        if self.Register.GetStatus()=='Fail':
            return 0
        elif self.Register.GetStatus()=='Success':
            print('exiting function with success')
            return 1
        self.Register.ResetFail()
        
        for i in range(len(self.Register.GetState())):
            if self.Register.GetState()[i]=='Wait':
                print ('function for ', self.Processes[i].GetName())
                result=self.SafetyCheck(self.Processes[i].GetName())
                #print(processname,result)
        
    def Calculate():
        #Put Resources Obj 
        #Put Processes Obj
        #Request Resources
        #Do SafetyCheck
        return 0
       
if __name__=="__main__":       
    A=Resource('A', 10)
    B=Resource('B', 5)
    C=Resource('C', 7)
    P0=Process('p0', [7, 5, 3])
    P1=Process('p1', [3, 2, 2])
    P2=Process('p2', [9, 0, 2])
    P3=Process('p3', [2, 2, 2])
    P4=Process('p4', [4, 3, 3])
    manager=Manager([A,B,C], [P0, P1, P2, P3, P4])
    #manager.PrintInfo()
    
    manager.ResourceRequest('p0', [0,1,0])
    manager.ResourceRequest('p1', [2,0,0])
    manager.ResourceRequest('p2', [3,0,2])
    manager.ResourceRequest('p3', [2,1,1])
    manager.ResourceRequest('p4', [0,0,2])
    #manager.PrintInfo()

    manager.ResourceRequest('p1', [1,0,2])
    manager.SafetyCheck('p1')
    print (manager.GetRegInfo())

    
 