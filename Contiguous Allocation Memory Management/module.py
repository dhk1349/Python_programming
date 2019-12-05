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
    def PrintInfo(self):
        print("===========")
        print(self.name)
        print(self.base)
        print(self.end)
        print("===========")

        
class EmptySpace:
    def __init__(self, initializer):
        self.base=initializer[0]
        self.end=initializer[1]
        self.limit=initializer[1]-initializer[0]
        self.name=str(initializer[2])
        self.type="Empty Space"
        
    def GetBase(self):
        return self.base
    def GetEnd(self):
        return self.end
    def GetLimit(self):
        return self.limit
    def GetName(self):
        return self.name
    
    def PrintInfo(self):
        print("===========")
        print(self.name)
        print(self.base)
        print(self.end)
        print("===========")
        
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
        self.EmptyList=[]
        
    def SearchEmptyObject(self,name):
        for i in self.EmptyList:
            if name==i.GetName():
                return i
        return 0
    
    def SearchProcess(self,name):
        for i in self.ProcessList:
            if name==i.GetName():
                return i
        return 0
            
    def InitializeEmptySpace(self):
        #initialize empty space after operation
        Base=self.base
        index=0
        self.EmptyList=[]
        
        for i in self.ProcessList:
            if(i.GetBase()-Base>0):
                print("making empty space1")
                #self.EmptyList.append(EmptySpace([Base+1, i.GetBase(), "Empty-"+str(index)]))
                #index+=1
            elif(i.GetBase()-Base<0):
                print ("Illegal Allocation of Memory")
                self.EmptyList=[]
                return 0
            Base=i.GetEnd()
        
        if len(self.ProcessList)==0:
            print("making empty space2")
            self.EmptyList.append(EmptySpace([self.base, self.end, "Empty Base"]))
        else:
            if(self.end-Base>0):
                print("making empty space3")
                self.EmptyList.append(EmptySpace([Base+1, self.end, "Empty-"+str(index)]))
                index+=1
            
    def AddProcess(self, data):
        """
        data:    
            [size, name]
        Add Process with Best Fit
        """
        bestmin=-1
        bestindex=-1
        for i in self.EmptyList:
            if(i.GetLimit()>(data[0])):
                #process can fit into this space
                if bestmin==-1:
                    #print("1")
                    bestmin=i.GetLimit()-data[0]
                    bestindex=i.GetName()
                elif bestmin>(i.GetLimit()-data[0]):
                    #print("2")
                    #best fits so far
                    bestmin=i.GetLimit()-data[0]
                    bestindex=i.GetName()
                #else:
                    #print("NONE of them above")
        if bestindex==-1:
            print("Illegal situation")
            return 0
        else:
            print("Bestmin: ", str(bestmin), "\nBestindex: ", str(bestindex))
            EmptyObj=self.SearchEmptyObject(bestindex)
            Base=EmptyObj.GetBase()
            """
            for i in range(len(self.ProcessList)):
                #iterates to insert
                if self.ProcessList[i].GetBase()>Base:
                    #initialize process
                    print("Process Added")
                    self.ProcessList.insert(i, Process([Base, Base+data[0], "process-"data[1]]))
                    break
            if(len(self.ProcessList)==0):
                print("Process Added")
                self.ProcessList.append(Process([Base, Base+data[0],"Process-"+data[1]]))
            """
            self.ProcessList.append(Process([Base, Base+data[0]-1,"Process-"+data[1]]))
            self.ProcessList.sort(key=lambda x: x.GetBase())
            
    def DeleteProcess(self, data):
        """
        data:
            name
        """
        process=self.SearchProcess(data)
        if process!=0:
            self.ProcessList.remove(process)
            return 1
        return 0
            
    def Coalescing(self):
        print ("Coalescing")
        """
        InitializeEmptySpace함수가 이미 이 역학을 해주는 듯 하다.
        """
        return 
    
    def Compaction(self): 
        print("Compaction")
        return
    
    def PrintStatus(self):
        """
        이건 나중에,,
        while True:
            EmptyIndex=0
            ProcessIndex=0
            
            
            if(EmptyIndex==len(self.ProcessList) and ProcessIndex==len(self.ProcessList)):
                break
        """
        for i in self.EmptyList:
            i.PrintInfo()
        for i in self.ProcessList:
            i.PrintInfo()

class Manager:
    def __init__(self):
        self.Memory=Memory([0, 255])
    
    def Execute(self):
        fd=open('input.txt','r')
        data=fd.readline()
        data=data.split()
        #print(data)
        
        for i in range(0, len(data), 2):
            print("input: ",data[i], ", ", data[i+1] )
            
            if int(data[i+1])==0:
                #erase process
                self.Memory.InitializeEmptySpace()
                self.Memory.DeleteProcess(data[i])
            else:
                #add Process
                #print("adding")
                self.Memory.InitializeEmptySpace()
                self.Memory.AddProcess([int(data[i+1]), data[i]])
            self.Memory.InitializeEmptySpace()
            self.Memory.PrintStatus()
        self.Memory.InitializeEmptySpace()
        self.Memory.PrintStatus()
if __name__=="__main__":
    a=Manager()
    a.Execute()
        
        
        
        
        
        
        
        
        
        
        
        