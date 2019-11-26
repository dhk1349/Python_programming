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
    
    def AddResource(self, num):
        self.InstanceNum+=num
        return self.InstanceNum
    
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
        self.CurrentList=[0]*len(max_lst)
        return temp
    
    def GetName(self):
        return self.Name
    
    def GetCurrentState(self):
        return self.CurrentList
    
    def GeMaxResource(self):
        return self.MaxList
        
if __name__=="__main__":
