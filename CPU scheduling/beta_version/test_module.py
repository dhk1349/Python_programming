# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:49:54 2019

@author: dhk13
"""

from scheduler_module import *
from imp import reload


def harmonize():
    lst1=[]
    
    return lst1
    
if __name__=="__main__":
    print ("Test cases on test_module.py")
    
    test1=PollingService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task C",3, 8))#내가 추가     
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test1.CalHyperPeriod()
    test1.CalTask()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    test2=DefferableService()
    test2.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test2.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test2.PushPeriodicTask(task_module.PeriodicTask("Task C",8, 8))#내가 추가
    test2.PushPeriodicTask(task_module.PeriodicTask("Task B",4, 6))#내가 추가
    test2.PushPeriodicTask(task_module.PeriodicTask("Task B",4, 6))#내가 추가 
    test2.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test2.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test2.CalHyperPeriod()
    test2.CalTask()
    
    #harmonize 할 수 있는 RANDOM generate set 만들어서 test진행하기 
    #rule
    #Server는 우선순위 때문에 period를 가장 작게 설정해야한다.
    #periodic task의 Exetime은 각 task는 period보다는 훨씬 작아야한다.
    #주기들을 harmonize시켜야한다. => LCM을 미리 정해두면 될 듯  
    
    #AP task의 exetime을 1~2^period의 임의 정수 선정 후 밑이 2인 로그를 씌운다. 
    #그러면 10에 가까운 수가 많이 나온다. 
    #그러면 로그 씌운 값을 최 댓값에서 뺀다면? 될 듯
    
    
    