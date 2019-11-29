#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 02:27:49 2019

@author: donghoon
"""
import module
import Manager_module
import Input_module

def ConnectionModule(InstanceNum, ProcessMaxList, ProcessResourceList):
    ProcessList=[]
    ResourceList=[]
    for i in range(len(InstanceNum)):
        ResourceList.append(module.Resource("R"+str(i), InstanceNum[i]))
    for i in range(len(ProcessMaxList)):
        ProcessList.append(module.Process("P"+str(i), ProcessMaxList[i]))
    
    manager=Manager_module.Manager(ResourceList, ProcessList)
    print("*****Initializing modules completed*****")
    print("**********Requesting Resources***********")
    index=0
    for i in range(len(ProcessResourceList)):
        manager.ResourceRequest("P"+str(i), ProcessResourceList[i])
        index=i
    manager.PrintInfo()
  
    print("from process 0 to ",str(index),", choose process to execute (ex. P1, P2...)", sep="")
    startprocess=input(">>")
    manager.SafetyCheck(startprocess)
    result, path=manager.GetResult()
    print(result)
    print(path)
    
if __name__=="__main__":
    print("=======================================")
    print("1. User Mode\n2. Random Generate Mode")
    print("=======================================")
    gettype=input(">>Input(1 or 2): ")

    if gettype=="1":
        InstanceNum, ProcessMaxList, ProcessResourceList=Input_module.InputMode()
    elif gettype=="2":
        InstanceNum, ProcessMaxList, ProcessResourceList=Input_module.RandomeInputGenerator()
    else:
        print("Illegal input!")
        exit(1)
    ConnectionModule(InstanceNum, ProcessMaxList, ProcessResourceList)
    