# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:49:54 2019

@author: dhk13
"""

from scheduler_module import *



if __name__=="__main__":
    print ("Test cases on test_module.py")
    
    test1=PollingService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test1.CalHyperPeriod()
    test1.CalTask()
    
    test2=DefferableService()
    test2.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test2.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test2.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test2.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test2.CalHyperPeriod()
    test2.CalTask()
    
    