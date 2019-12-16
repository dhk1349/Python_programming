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
            if j==1:
                status="Free"
            elif j==2:
                status="Delay"
            else:
                status="Busy"
            print(i, "mod ->", mod)
            block=module.Node(element=i, status=status)
            self.ModList[mod].PushBack(block)
            if block.element!="Busy": #if free
                self.FreeList[0].PushBack(copy.deepcopy(block))
            self.PrintAll()

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
            print(result.element, result.status," Found")
            return result
        return False
    
    def UnlockBusy(self, blknum):
        result=self.SearchHash(blknum)
        cnt=random.randrange(1,11)
        while cnt!=0:
            print("Waiting Block to be Free")
            time.sleep(1)
            cnt-=1
        result.SetStatus("Free")
        
        
    def GetBlock(self, blknum):
        result=self.SearchHash(blknum)
        if result!=False:
            if result.status=="Busy":#scenario5
                print("Block is now busy")
            else:#scenario1
                result.status="Busy"
                self.FreeList.RemoveNode(result.element)
                return result
        else:
            if(self.FreeList.EndNode.element=="Head"):#it means freelist is empty
                print("Free list is empty. Must wait")
            else:
                while True:
                    block=self.FreeList.RemoveNode(self.FreeList.HeadNode.next.element)
                    
                    if block.status=="Delay":
                        print("asynchronous write buffer to disk")
                        continue
                    else:
                        block.SetStatus("Busy")
                        return block
                        
        
        
if __name__=="__main__":
    inputlist=[(10,1),(5,0), (3,1), (11,0), (6,0), (8, 1)]
    buf=BufferCache(3)
    buf.Initialize(inputlist)
    
    buf.SearchHash(11)
    