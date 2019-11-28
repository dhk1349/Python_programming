# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:26:59 2019

@author: dhk1349
"""
import module
import Register_module

class Manager:
    def __init__(self, ResourceLst, ProcessLst):
        #Requirement: resource list in process obj has to be
        #same order wirh resource list list in Manager obj
        self.Resources=ResourceLst
        self.Processes=ProcessLst
        self.Register=Register_module.Register(len(ProcessLst))

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
    
    def GetResult(self):
        return self.Register.GetStatus(), self.Register.GetOrder()

       
       
if __name__=="__main__":       
    A=module.Resource('A', 10)
    B=module.Resource('B', 5)
    C=module.Resource('C', 7)
    P0=module.Process('p0', [7, 5, 3])
    P1=module.Process('p1', [3, 2, 2])
    P2=module.Process('p2', [9, 0, 2])
    P3=module.Process('p3', [2, 2, 2])
    P4=module.Process('p4', [4, 3, 3])
    manager=Manager([A,B,C], [P0, P1, P2, P3, P4])
    manager.PrintInfo()
    
    manager.ResourceRequest('p0', [0,1,0])
    manager.ResourceRequest('p1', [2,0,0])
    manager.ResourceRequest('p2', [3,0,2])
    manager.ResourceRequest('p3', [2,1,1])
    manager.ResourceRequest('p4', [0,0,2])
    manager.PrintInfo()

 