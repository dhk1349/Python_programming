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

class EmptySpace:
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        self.limit=initializer[1]-initializer[0]
        
class Memory:
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        
    def Coalescing(self):
        return 
    
    def Compaction(self):   
        return