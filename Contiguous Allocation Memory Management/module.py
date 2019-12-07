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
    
    
Detecting coalescing = make self.var that counts the length of processlist and emptylist
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
    def GetName(self):
        return self.name
    def GetLimit(self):
        return self.limit
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
        self.Coalescing=False
        
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
        index=1
        self.EmptyList=[]
        
        for i in self.ProcessList:
            if(i.GetBase()-Base<0):
                #print ("Illegal Allocation of Memory")
                return 0
            elif(i.GetBase()>Base+1):
                if Base==0:
                    self.EmptyList.append(EmptySpace([Base, i.GetBase()-1, "Empty -"+str(index)]))
                else:
                    self.EmptyList.append(EmptySpace([Base+1, i.GetBase()-1, "Empty -"+str(index)]))
                index+=1
            Base=i.GetEnd()
        if len(self.ProcessList)==0:
            #print("making empty space2")
            self.EmptyList.append(EmptySpace([self.base, self.end, "Empty -"]))
        else:
            if(self.end-Base>0):
                #print("making empty space3")
                self.EmptyList.append(EmptySpace([Base+1, self.end, "Empty -"+str(index)]))
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
            if(i.GetLimit()+1>=(data[0])):
                #process can fit into this space
                if bestmin==-1:
                    #print("1")
                    bestmin=i.GetLimit()-data[0]+1
                    bestindex=i.GetName()
                elif bestmin>(i.GetLimit()-data[0]+1):
                    #best fits so far
                    bestmin=i.GetLimit()-data[0]+1
                    bestindex=i.GetName()
                #else:
                    #print("NONE of them above")
        if bestindex==-1:
            print("Illegal situation")
            return 0
        else:
            #print("Bestmin: ", str(bestmin), "\nBestindex: ", str(bestindex))
            EmptyObj=self.SearchEmptyObject(bestindex)
            Base=EmptyObj.GetBase()
            print("Best Fit: Allocated at address ", Base,"K",sep="")
            self.ProcessList.append(Process([Base, Base+data[0]-1,"Process-"+data[1]]))
            self.ProcessList.sort(key=lambda x: x.GetBase())
            
    def DeleteProcess(self, data):
        """
        data:
            name
        """
        CoalescingList=[]
        self.Coalescing=False
        process=self.SearchProcess("Process-"+data)
        pbase=process.GetBase()
        pend=process.GetEnd()
        if process!=0:
            print("FREE REQUEST: ", process.GetName()[-1:]," (",process.GetLimit()+1,"K)", sep="")
            print("Best Fit: Freed at address ",process.GetBase(),"K",sep="")
            CoalescingList.append(process.GetBase())
            self.ProcessList.remove(process)
            
            #Empty space가 인접해있는지 확인
            for i in self.EmptyList:
                if i.GetEnd()+1==pbase or i.GetBase()-1==pend:
                    self.Coalescing=True
                    CoalescingList.append(i.GetBase())
            CoalescingList.sort()
            if self.Coalescing==True:
                print("\tCoalescing blocks at address ", end="", sep="")
                tempstr=""
                for i in CoalescingList:
                    tempstr+=(" "+str(i)+"K, ")
                print (tempstr[:-2])
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
    
    def PrintEmptyInfo(self):        
        EmptySpace=0
        for i in self.EmptyList:
            EmptySpace+=(i.GetLimit()+1)
        print("\t", EmptySpace, "K free, ",len(self.EmptyList), " block(s), average size= ",round(EmptySpace/len(self.EmptyList)),"K\n", sep="")
    
    def PrintStatus(self):
        Processbool=False
        Emptybool=False
        Processindex=0
        Emptyindex=0
        while ((not Processbool) or (not Emptybool)):
            if Processbool==False:
                ProcBase=self.ProcessList[Processindex].GetBase()
            else:
                ProcBase=self.end+1
            if Emptybool==False:
                EmptyBase=self.EmptyList[Emptyindex].GetBase()
            else:
                EmptyBase=self.end+1
                
            if(ProcBase<EmptyBase):
                self.ProcessList[Processindex].PrintInfo()
                Processindex+=1
            else:
                self.EmptyList[Emptyindex].PrintInfo()
                Emptyindex+=1
            if(len(self.ProcessList)==Processindex):
               Processbool=True
            if(len(self.EmptyList)==Emptyindex):
               Emptybool=True
           
class Manager:
    def __init__(self):
        self.Memory=Memory([0, 255])
    
    def Execute(self):
        fd=open('input.txt','r')
        data=fd.readline()
        data=data.split()
        #print(data)
        self.Memory.InitializeEmptySpace()
        for i in range(0, len(data), 2):
            if int(data[i+1])==0:
                #erase process
                self.Memory.DeleteProcess(data[i])
            else:
                print("REQUEST ",data[i], ": ", data[i+1],"K", sep="" )
                self.Memory.AddProcess([int(data[i+1]), data[i]])
            self.Memory.InitializeEmptySpace()
            self.Memory.PrintEmptyInfo()
            #self.Memory.PrintStatus()
            self.Memory.InitializeEmptySpace()
        print("*****Final Result*****")
        #self.Memory.InitializeEmptySpace()
        self.Memory.PrintStatus()
        
if __name__=="__main__":
    a=Manager()
    a.Execute()
        
        
        
        
        
        
        
        
        
        
        
        