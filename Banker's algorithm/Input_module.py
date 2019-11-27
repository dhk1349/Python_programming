# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:27:49 2019

@author: dhk1349
"""

def Check(Resourcelst, processmaxlst, processresourcelst):
    #Things need to be checked 
    



def InputMode():
    ResourcesNum=int(input("Enter Number of Resources: "))
    InstanceNum=input("Enter numbers of Instance for each resource: ")
    ProcessNum=int(input("Enter Number of Processes"))
    
    ProcessResourceList=[]
    ProcessMaxList=[]
    
    print("**********Setting Max Resource**********")
    for i in range(ProcessNum):
        temp=input(str(i+1)+". Set Max Resources to Process")
        ProcessMaxList.append(temp)        
    print("*****************************************\n")
    
    print("**********Allocating Resources**********")
    for i in range(ProcessNum):
        temp=input(str(i+1)+". Allocate Resources to Process")
        ProcessResourceList.append(temp)
    print("*****************************************\n")
    

