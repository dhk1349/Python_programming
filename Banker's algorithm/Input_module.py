# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:27:49 2019

@author: dhk1349
"""
import random
import math
def parser(inputlst):
    result=[]
    for i in range(0,len(inputlst),2):
        result.append(int(inputlst[i]))
    return result
        
def InputMode():
    ResourcesNum=int(input("Enter Number of Resources: "))
    InstanceNum=input("Enter numbers of Instance for each resource: ")
    ProcessNum=int(input("Enter Number of Processes: "))
    
    ProcessResourceList=[]
    ProcessMaxList=[]
    
    print("**********Setting Max Resource**********")
    for i in range(ProcessNum):
        temp=input(str(i+1)+". Set Max Resources to Process: ")
        ProcessMaxList.append(parser(temp))        
    print("*****************************************\n")
    
    print("**********Allocating Resources**********")
    for i in range(ProcessNum):
        temp=input(str(i+1)+". Allocate Resources to Process: ")
        ProcessResourceList.append(parser(temp))
    print("*****************************************\n")
    
    print("result")
    print (ResourcesNum)
    print (InstanceNum)
    print (ProcessNum)
    print (ProcessResourceList)
    print (ProcessMaxList)

def LogScaleRandom(start, end, base):
    start=int(start)
    end=int(end)
    number=random.randrange(1, math.floor(pow(base, end-start)+1))
    return (end-math.ceil(math.log(number,base)))

def RandomeInputGenerator():
    #number of Resources: 3-100
    #number of Instances: ?
    #number of processes: 
    #number of Max resources for each process
    #number of request resources for each process
    #number=random.randrange(1, pow(3, 97)+1)
    #print(100-math.ceil(math.log(number,3)))
    ResourcesNum=LogScaleRandom(3, 100, 3)
    ProcessNum=LogScaleRandom(3, 100, 2)
    InstanceNum=[]
    print(ResourcesNum)
    print(ProcessNum)
    
    for i in range(ResourcesNum):
        InstanceNum.append(LogScaleRandom(4,100,2))
    print(InstanceNum)
    
    InstanceRecord=InstanceNum
    ProcessMaxList=[]
    ProcessResourceList=[]
    for i in range(ProcessNum):
        templst=[]
        templst2=[]
        for j in range(ResourcesNum):
            maxnum=LogScaleRandom(3,100,2)
            templst.append(maxnum)
            reqnum=LogScaleRandom(0, min(InstanceRecord[j], maxnum),1.3)
            InstanceRecord[j]-=reqnum
            templst2.append(reqnum)
        ProcessMaxList.append(templst)
        ProcessResourceList.append(templst2)
    print(ProcessMaxList)
    print(ProcessResourceList)
    
    
#InputMode()
RandomeInputGenerator()