#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 03:06:28 2019

@author: donghoon
@Project Name: Contiguous Allocation Memory Mangement

Requirment:
    -input: Randomly generated input file
    -Allocate process to space where it best fits.
    -Coalescing
    -Compaction (Brute force case and efficient case each)
"""
class Process:
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        self.limit=initializer[1]-initializer[0]
        self.name=initializer[2]
        self.type="Process"
    
    def GetBase(self):
        return self.base
    
    def GetEnd(self):
        return self.end

class EmptySpace:
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        self.limit=initializer[1]-initializer[0]
        self.name=initializer[2]
        self.type="Empty Space"
        
class Memory:
    """
    Operation:
        Add process 
        Delete process
    """
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        self.ProcessList=[]
    
    def Iterator(self):
        #initialize empty space after operation
        Base=self.base
        for i in self.ProcessList:
            if(i.GetBase()-Base>0):
                
            
    
    def Coalescing(self):
        return 
    
    def Compaction(self):   
        return
    
    