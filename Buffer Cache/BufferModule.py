#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:12:23 2019

@author: donghoon


Scenario
#1 Requesting block that is in the freelist and queue
#2 Requesting block that is not in the queque and freelist
#3 Requesting block that is not in the queque and freelist but free block is in delayed write
#4 Requesting block that is not in the queque and freelist no free block left
#5 Requesting block but block is in use
"""
import copy
import module
import time
import random

class BufferCache:
    def __init__(self, ModNum):
        self.FreeList=[module.CDLL()]
        self.ModNum=ModNum
        self.ModList=[]
        for i in range(ModNum):
            self.ModList.append(module.CDLL())
        
    def Initialize(self,BlockNumList):
        for i,j in BlockNumList:
            mod=i%len(self.ModList)
            #putevery Block in HashQueue
            if j==0:
                status="Free"
            elif j==-1:
                status="Delay"
            else:
                status="Busy"
            #print(i, "mod ->", mod)
            #print("Status: ", status)
            block=module.Node(element=i, status=status, time=j)
            self.ModList[mod].PushBack(block)
            if block.status=="Free" or block.status=="Delay": #if free
                self.FreeList[0].PushBack(copy.deepcopy(block))

    def PrintAll(self):
        for i in range(len(self.ModList)):
            print("blkno ", i, " mod ", len(self.ModList))
            self.ModList[i].PrintList()
            print("================\n")
        print("Free List") 
        self.FreeList[0].PrintList()
        print("\n\n")
    
    def SearchHash(self, blkNum):
        mod=blkNum%self.ModNum
        result=self.ModList[mod].SearchNode(blkNum)
        if result!=False:
            print(result.element," is " ,result.status,".", sep="")
            return result
        print("Block ", blkNum, " is not Found.", sep="")
        return False
    
    def FreeBlock(self):
        for i in self.ModList:
           for j in i.GetZeroCount():
               #j is node
               print(j.element," is free")
               self.FreeList[0].PushBack(copy.deepcopy(j))
               
    def UnlockBusy(self):
        """
        result=self.SearchHash(blknum)
        cnt=random.randrange(1,11)
        while cnt!=0:
            print("Waiting Block to be Free")
            time.sleep(1)
            cnt-=1
        result.SetStatus("Free")
        """
        flag=False
        index=1
        while flag==False:
            print("Waiting Block to be Free... (", index, "sec)")
            time.sleep(1)
            index+=1
            for i in self.ModList:
                flag=i.ReduceCount() or flag
        #print("Before free block")
        #self.PrintAll()
        self.FreeBlock()
        
    def GetBlock(self, blknum):
        print("*******************************")
        print("Requesting Block ", blknum,"...")
        result=self.SearchHash(blknum)
        if result!=False:
            if result.status=="Busy":#scenario5
                print("Block is now busy")
                while result.status!="Free":
                    result.time-=1
                    print("Waiting..")
                    time.sleep(1)
                    if result.time==0:
                        print("Block is now free!")
                        result.status="Free"
                result.time=random.randrange(1,11)
                result.SetStatus("Busy")
                print("*******************************\n")

            else:#scenario1
                result.status="Busy"
                self.FreeList[0].RemoveNode(result.element)
                print("*******************************\n")
                return result
        else:
            if(self.FreeList[0].EndNode.element=="Head"):#it means freelist is empty
                print("Free list is empty. Must wait")
                self.UnlockBusy()
                while True:
                    block=self.FreeList[0].RemoveNode(self.FreeList[0].HeadNode.next.element)
                    self.ModList[block.element%self.ModNum].RemoveNode(block.element)
                    if block.status=="Delay":
                        print("asynchronous write buffer to disk")
                        print("Delayed write for ", block.element)
                        continue
                    else:
                        print("Removing Block ", block.element)
                        block.SetElement(blknum)
                        block.SetTime(random.randrange(1,11))
                        block.SetStatus("Busy")
                        self.ModList[blknum%self.ModNum].PushBack(block)
                        print("*******************************\n")
                        return block
                
            else:#free list not empty
                while True:
                    block=self.FreeList[0].RemoveNode(self.FreeList[0].HeadNode.next.element)
                    self.ModList[block.element%self.ModNum].RemoveNode(block.element)
                    if block.status=="Delay":
                        print("asynchronous write buffer to disk")
                        print("Delayed write for ", block.element)
                        continue
                    else:
                        print("Removing Block ", block.element)
                        block.SetElement(blknum)
                        block.SetTime(random.randrange(1,11))
                        block.SetStatus("Busy")
                        self.ModList[blknum%self.ModNum].PushBack(block)
                        print("*******************************\n")
                        return block
                        
        

if __name__=="__main__":
    
    #inputlist=[(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)] #S1, S2
    #inputlist=[(10,1),(5,-1), (3,1), (11,0), (6,0), (8, 1)] #S3
    #inputlist=[(10,2),(5,2), (3,3), (11,5), (6,3), (8, 5)] #S4
    inputlist=[(10,2),(5,2), (3,0), (11,5), (6,3), (8, 5)] #S5
    buf=BufferCache(3)
    buf.Initialize(inputlist)
    
    #buf.SearchHash(11)
    #buf.GetBlock(11) #S1
    #buf.GetBlock(1) #S2 S3 S4
    buf.GetBlock(10) #S5
    buf.PrintAll()
    
    
    