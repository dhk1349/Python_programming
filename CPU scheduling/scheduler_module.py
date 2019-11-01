# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""
import task_module

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

class PollingService:
    """
    Polling Service
    Polling server가 excecution time과 Period를 가진다.
    그리고 주기가 돌아올 때마다 Aperiodic task가 쌓여있으면,
    execution time을 할애해서  Aperiodic task를 수행한다.

    Periodic task는 주기가 짧은 task가 우선 순위를 가지고 수행된다.

    Requirement for Execution of this class
    push Periodic task objects
    Push Aperiodic task objects
    Initialize Polling server information
    
    Calculate Hyperparameter
    
    Then CalTask
    
    ***현재 상태: periodic task는 제대로 작동
    ***작동가능 여부 확인하는 공식 아직 미구현
    ***aperiodic task 미적
    """
    Name=""
    PeriodicTasks=[]

    AperiodicTasks=[]

    PSExeTime=1 #Polling server exetime
    PSPeriod=5  #Polling server period, PushTime에 맞게 AP task를 넣어줘야한다.

    HyperPeriod=0
    TaskQueue=[]
    def __init__(self):
        self.Name="Polling Service"

    def PushPeriodicTask(self,TaskObj):
        self.PeriodicTasks.append(TaskObj)
        self.PeriodicTasks.sort(key=lambda object:object.GetPeriod())
        print (self.PeriodicTasks)
    
    def PushAPeriodicTask(self, TaskObj):
        self.AperiodicTasks.append(TaskObj)
        
    def CalHyperPeriod(self):
        HyperPeriod=self.PSPeriod
        for i in range(len(self.PeriodicTasks)):
            self.HyperPeriod=lcm(HyperPeriod, self.PeriodicTasks[i].GetPeriod())
        self.HyperPeriod=int(self.HyperPeriod)
        print("HyperPEriod is ",self.HyperPeriod)
        
    def PollServerTask(self):
        PSExe=self.PSExeTime
        for i in range(len(self.AperiodicTasks)):
            if(self.AperiodicTasks[i].ExeTask(PSExe)==1):
                print("Executed ",i,"th AP task")
        if (PSExe==self.PSExeTime):
            return True
        return False
        
    def CalTask(self):
        for i in range(self.HyperPeriod):#iterating one cycle of HyperPerid
            print("Time ",i)
            if i%self.PSPeriod==0:
                result=self.PollServerTask()
                i= i +self. PSExeTime-1 #Just in case Polling server exetime is bigger than 1
                if result==True:
                    time=[1]
                    for i in range(len(self.PeriodicTasks)):
                        if(self.PeriodicTasks[i].ExeTask(time)==1):
                            print("Executed ",i,"th Periodic task\n\n")
            else:
                time=[1]
                for i in range(len(self.PeriodicTasks)):
                    if(self.PeriodicTasks[i].ExeTask(time)==1):
                        print("Executed ",i,"th Periodic task\n\n")
        


class DefferableService:
    def __init__(self):
        self.name="DifferableService"
        
if __name__=="__main__":
    print("Test Execution on scheduler_module.py")
    test1=PollingService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.CalHyperPeriod()
    test1.CalTask()
    
    