# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:35:22 2019

@author: dhk1349
"""

class PeriodicTask:
    ExeTime=-1
    Period=-1
    def __init__(self, exe, period):
        self.ExeTime=exe
        self.Period=period
        self.Counter=0
    
    def AddCount(self):
        self.Counter+=1
    
    def AddTask(self):
        
    
    def GetPeriod(self):
        return self.Period
    