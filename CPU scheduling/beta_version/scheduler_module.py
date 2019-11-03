# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""
import importlib
import task_module

importlib.reload(task_module)

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
    
    ***현재 상태: periodic task는 제대로 작동, aperiodic task도 제대로 동작
    ***작동가능 여부 확인하는 공식 아직 미구현
    """
    Name=""
    PeriodicTasks=[]

    PollServerTasks=[]
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
    
    def Interrupter(self, time):#fnc for interruption and pushing aperiodic task
        #해당 시간(time)에 들어올 aptask가 있는지 확인하고 pollservertasks에 추가
        for i in self.AperiodicTasks:
            if time==i.GetInterruptTime():
                self.PollServerTasks.append(i)
    
    def CalHyperPeriod(self):
        HyperPeriod=self.PSPeriod
        for i in range(len(self.PeriodicTasks)):
            self.HyperPeriod=lcm(HyperPeriod, self.PeriodicTasks[i].GetPeriod())
        self.HyperPeriod=int(self.HyperPeriod)
        print("HyperPEriod is ",self.HyperPeriod)
        
    def PollServerTask(self):      
        PSExe=[self.PSExeTime]
        for i in range(len(self.PollServerTasks)):
            """
            if(self.PollServerTasks[i].ExeTask(PSExe)==1):
                print("Executed ",i,"th AP task")
            아래 while문으로 바꿈 
            """
            while True:
                a=self.PollServerTasks[i].ExeTask(PSExe)
                if a==0:
                    break
        if (PSExe[0]==self.PSExeTime):
            return True
        return False
        
    def Check(self):
        #Function that checks if it's possible to schedule tasks with given info
        left_hand=self.PSExeTime/self.PSPeriod
        for i in self.PeriodicTasks:
            temp=i.GetExeTime()/i.GetPeriod()
            left_hand+=temp
        TotalTask=(len(self.PeriodicTasks)+1)
        right_hand=TotalTask*(2**(1/TotalTask)-1)
        return left_hand<=right_hand
        
    def CalTask(self):
        if (self.Check()==False):
            print("This Task will Fail")
            return 0
        print("This may not Fail")
        for i in range(self.HyperPeriod):#iterating one cycle of HyperPerid
            print("Time ",i)
            self.Interrupter(i)
            if i%self.PSPeriod==0:
                result=self.PollServerTask()
                i= i +self. PSExeTime-1 #Just in case Polling server exetime is bigger than 1
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if result==True:
                        if(self.PeriodicTasks[j].ExeTask(time)==1):
                            print("Executed ",j,"th Periodic task.\n\n")
                    else:
                        self.PeriodicTasks[j].AddCount()
            else:
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if(self.PeriodicTasks[j].ExeTask(time)==1):
                        print("Executed ",j,"th Periodic task\n\n")
        


class DefferableService:
    """
    Key difference of DefferableService is that 
    defferable server is alive untill its capacity is exhausted
    """
    Name=""
    PeriodicTasks=[]

    DeferrableServerTasks=[]
    AperiodicTasks=[]

    DSExeTime=[0] #server exetime
    ConstDSExe=1
    CacheDS=0
    DSPeriod=5  #server period, PushTime에 맞게 AP task를 넣어줘야한다.

    HyperPeriod=0
    TaskQueue=[]
    def __init__(self):
        self.name="DifferableService"
    
    def PushPeriodicTask(self,TaskObj):
        self.PeriodicTasks.append(TaskObj)
        self.PeriodicTasks.sort(key=lambda object:object.GetPeriod())
        print (self.PeriodicTasks)
    
    def PushAPeriodicTask(self, TaskObj):
        self.AperiodicTasks.append(TaskObj)
    
    def Interrupter(self, time):#fnc for interruption and pushing aperiodic task
        for i in self.AperiodicTasks:
            if time==i.GetInterruptTime():
                self.DeferrableServerTasks.append(i)
                return True
        return False
    
    def CalHyperPeriod(self):
        self.HyperPeriod=self.DSPeriod
        print(self.HyperPeriod)
        for i in range(len(self.PeriodicTasks)):
            print(self.PeriodicTasks[i].GetPeriod())
            self.HyperPeriod=lcm(self.HyperPeriod, self.PeriodicTasks[i].GetPeriod())
        self.HyperPeriod=int(self.HyperPeriod)
        print("HyperPEriod is ",self.HyperPeriod)
        
    """    
    def PollServerTask(self):
        PSExe=[self.PSExeTime]
        for i in range(len(self.PollServerTasks)):
            if(self.PollServerTasks[i].ExeTask(PSExe)==1):
                print("Executed ",i,"th AP task")
        if (PSExe[0]==self.PSExeTime):
            return True
        return False
    """
    def InitializeServer(self):
        self.DSExeTime[0]=self.ConstDSExe
        self.CacheDS=self.ConstDSExe
    
    def DeferrableTask(self):
        #differabel server확인하는 함수 
        #capacity가 남아있는지 확인하고 수행여부 결정
        #수행할 task가 있나 확인 후, 수행할 수 있는 capacity가 존재하는지 확인.
        #수행하는게 없느면 False를 리턴할 것이다.
        #뭐라도 수행하면 True를 리턴할 것이다.
        
        for i in range(len(self.DeferrableServerTasks)):
            while True:
                if self.DeferrableServerTasks[i].ExeTask(self.DSExeTime)==0:
                    break
        tic=self.CacheDS-self.DSExeTime[0]
        self.CacheDS=self.DSExeTime[0]
        return tic
    
    def Check(self):
        #Function that checks if it's possible to schedule tasks with given info
        left_hand=self.ConstDSExe/self.DSPeriod
        for i in self.PeriodicTasks:
            temp2=i.GetPeriod()
            print("이건 됨 ", temp2)
            temp=i.GetExeTime()
            temp=temp/temp2
            left_hand+=temp
        TotalTask=(len(self.PeriodicTasks)+1)
        right_hand=TotalTask*(2**(1/TotalTask)-1)
        return left_hand<=right_hand
    
    #def CalAvgWaitingTime():   
    
    def CalTask(self):
        if(self.Check()==False):
            print("This Task will Fail")
            return 0
        print ("This may not Fail")
        for i in range(self.HyperPeriod):#iterating one cycle of HyperPerid
            print("Time ",i)
            self.Interrupter(i)
            if i%self.DSPeriod==0:#해당 if 문은 필요하 없다. interrrupt가 리턴하는 값으로 조건 변경
               self.InitializeServer()
                #이부분이 달라져야한다. 
                #interrupt 들어올 때마다
            tic=self.DeferrableTask()
            if (tic==0):#if Defferable server did nothing
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if(self.PeriodicTasks[j].ExeTask(time)==1):
                        print("Executed ",j,"th Periodic task\n\n")
            else: #if server did sth
                i+=tic
                for j in range(tic):
                    for k in range(len(self.PeriodicTasks)):
                        self.PeriodicTasks[k].AddCount()
        
if __name__=="__main__":
    print("Test Execution on scheduler_module.py")
    """
    test1=PollingService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test1.CalHyperPeriod()
    test1.CalTask()
    """
    test1=DefferableService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test1.CalHyperPeriod()
    test1.CalTask()    
    