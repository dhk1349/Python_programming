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
        self.TaskQueue=0
        self.Counter=0
        self.InstanceNum=0
    
    def AddCount(self):
        self.Counter+=1
    
    def AddTask(self):
        self.TaskQueue+=self.ExeTime
        if(self.TaskQueue>self.ExeTime):
            print ("Something Wrogn with Task")
        self.InstanceNum+=1
        
    def GetRemainingTask(self):
        return self.TaskQueue
        
    def GetPeriod(self):
        return self.Period
    
    def PrintInfo(self):
        print ("==========Executed Task==========")
        print ("Task name: ",self.Name)
        print ("Instance Number: ",self.InstanceNum)
        print("Time: ",self.Counter)
        print("Remaining time: ",self.TaskQueue)
        print ("=================================")
    
    def ExeTask(self, exe):
        if(self.Counter%self.GetPeriod()==0):
            self.AddTask()
        
        if (exe[0]>0 and self.TaskQueue>0):
            self.TaskQueue-=1
            exe[0]-=1
            self.PrintInfo()
            self.Counter+=1
            return 1
        self.Counter+=1
        return 0

class APeriodicTask:
    def __init__(self, exe):
        self.TaskQueue=exe
        
    def GetRemainingTask(self):
        return self.Exetime
    
    def ExeTask(self, exe):
        if (exe>0 and self.TaskQueue>0):
            self.TaskQueue-=1
            exe-=1
            return 1
        return 0