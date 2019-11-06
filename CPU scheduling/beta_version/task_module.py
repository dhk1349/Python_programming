# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:35:22 2019

@author: dhk1349
"""

class PeriodicTask:
    ExeTime=-1
    Period=-1
    def __init__(self, name, exe, period):
        self.Name=name
        self.ExeTime=exe
        self.Period=period
        self.TaskQueue=exe
        self.Counter=0
        self.InstanceNum=1
    
    def AddCount(self):
        self.Counter+=1
        if(self.Counter%self.GetPeriod()==0):
            self.AddTask()

    
    def AddTask(self):
        self.TaskQueue+=self.ExeTime
        if(self.TaskQueue>self.ExeTime):
            print ("Something Wrogn with Task")
        self.InstanceNum+=1
    def GetName(self):
        return self.Name
    
    def GetInstanceNum(self):
        return self.InstanceNum
        
    def GetRemainingTask(self):
        return self.TaskQueue
    
    def GetExeTime(self):
        return self.ExeTime
    
    def GetPeriod(self):
        return self.Period
    
    def PrintInfo(self):
        print ("==========Executed Task==========")
        print ("Task name: ",self.Name)
        print ("Instance Number: ",self.InstanceNum)
        print("Time: ",self.Counter)
        print("Remaining time: ",self.TaskQueue)
        print ("=================================")
    
    def ExeTask(self, exe, result=None, Totallist=None, time=None):
        if (exe[0]>0 and self.TaskQueue>0):
            self.TaskQueue-=1
            exe[0]-=1
            if (result != None):
                result=[self.Name, self.InstanceNum]
            #if (Totallist!=None):
            #    Totallist[self.Counter]=self.Name
            if (Totallist != None and time!=None):
                print(time,"번 째 인덱스에 넣을거임!")
                Totallist[self.Counter]=[self.Name, self.InstanceNum]
            self.PrintInfo()
            self.Counter+=1
            return 1
        #self.Counter+=1
        self.AddCount()
        return 0

class APeriodicTask:
    def __init__(self, name, exe, interrupt_time):
        self.Name=name
        self.TaskQueue=exe
        self.InterruptTime=interrupt_time
        
    def GetRemainingTask(self):
        return self.Exetime
    
    def GetInterruptTime(self):
        return self.InterruptTime
    
    def GetName(self):
        return self.Name
    
    def PrintInfo(self):
        print ("==========Executed Task==========")
        print ("Task name: ",self.Name)
        print("Remaining time: ",self.TaskQueue)
        print ("=================================")
    
    
    def ExeTask(self, exe, Totallist=None, time=None):
        if (exe[0]>0 and self.TaskQueue>0):
            self.TaskQueue-=1
            #왜 빼기 1을 하지? 이 부분이 이상해 . 1말고 capacity만큼빼줘야해.
            exe[0]-=1
            #if (Totallist != None):
            #    Totallist=self.GetName()
            if (Totallist!=None and time!=None):
                print(time,"번 째 인덱스에 넣을거임!")
                Totallist[time]=[self.Name, self.InterruptTime]
            self.PrintInfo()
            return 1
        return 0