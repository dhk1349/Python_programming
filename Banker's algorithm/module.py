# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:40:24 2019

@author: dhk1349
"""

"""
성공적인 경로를 찾는 방법은 recursive한 함수를 통해서 구현한다. 
정의할 것은

자원의 종류와 갯수
프로세스의 갯수
프로세스의  Allocation, Max, Available, Need

들어오는 값은 특정 프로세스 x가 추가적인 자원의 요청 값 
  
그냥 instance를 오브젝트로 만들고, Reource를 스택으로 구현하면?
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
    
    def GetName(self):
        return self.Name
    
    def GetCurrentState(self):
        return self.CurrentList
    
    def GeMaxResource(self):
        return self.MaxList

class Register:
    def __init__(self, length):
        self.State=['w']*length
        self.Status='Proceed'
        
    def StatusCheck(self):
        if 'Fail' not in self.State and 'Wait' not in self.State:
            self.Status='Success'
        elif "Wait" not in self.State:
            self.State='Fail'
        elif 'Wait' in self.State:
            self.State='proceed'
        else:
            self.State='unexpected case'
        
class Manager:
    def __init__(self, ResourceLst, ProcessLst):
        #Requirement: resource list in process obj has to be
        #same order wirh resource list list in Manager obj
        self.Resources=ResourceLst
        self.Processes=ProcessLst

    def GetResource(self, name):
        for i in self.Resources:
            if i.GetName()==name:
                return i
        return None
    
    def GetProcess(self, name):
        for i in self.Pricesses:
            if i.GetName()==name:
                return i
        return None
           
    def ResourceRequest(self,processname, instnums): #return 1 if succeed
        #check if resource can is suficient
        for i in range(len(instnums)):
            if (self.Resources[i].CheckUseResource(instnums[i])==0):
                return 0
        #bring process and check
        process=self.GetProcee(processname)
        if process==None:
            return 0
        return process.Allocate(instnums)
    
    def PrintInfo(self):
        for i in self.Resources:
            print(i.GetName())
        for i in self. Processes:
            print(i.GetName())
    
    def SafetyCheck(self, processname):
        """
        Recursive function
        
        """
        NeedList=[]
        process=self.GetProcess(processname)
        for i in range(len(process.GetMaxResource())):
            NeedList.append(process.GetMaxResource()[i]-process.GetCurrentState()[i])
        #Compare with available list
        for i in range(len(NeedList)):
            if NeedList[i]>self.Resources[i]:
                return 0
"""       
A=Resource('A', 10)
B=Resource('B', 5)
C=Resource('C', 7)
P0=Process('p0', [7, 5, 3])
P1=Process('p1', [3, 2, 2])
P2=Process('p2', [9, 0, 2])
manager=Manager([A,B,C], [P0, P1, P2])
manager.PrintInfo()
"""
input_lst=['Fail','Wait','Fail']
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