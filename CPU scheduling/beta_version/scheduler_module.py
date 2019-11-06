# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""
import importlib
import task_module
import random
import math

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
    
    ResultList=[]
    TotalResult=[]
    def __init__(self):
        self.Name="Polling Service"
    
    def SetServer(self, inputlst):
        self.PSExeTime=inputlst[0]
        self.PSPeriod=inputlst[1]
        
    def PushPeriodicTask(self,TaskObj):
        self.PeriodicTasks.append(TaskObj)
        self.PeriodicTasks.sort(key=lambda object:object.GetPeriod())
        #print (self.PeriodicTasks)
    
    def PushAPeriodicTask(self, TaskObj):
        self.AperiodicTasks.append(TaskObj)
    
    def Interrupter(self, time):#fnc for interruption and pushing aperiodic task
        #해당 시간(time)에 들어올 aptask가 있는지 확인하고 pollservertasks에 추가
        for i in self.AperiodicTasks:
            if time==i.GetInterruptTime():
                self.PollServerTasks.append(i)
    
    def CalHyperPeriod(self):
        self.HyperPeriod=self.PSPeriod
        for i in range(len(self.PeriodicTasks)):
            #print(,"",)
            #print(self.PeriodicTasks[i].GetPeriod())
            self.HyperPeriod=lcm(self.HyperPeriod, self.PeriodicTasks[i].GetPeriod())
        self.HyperPeriod=int(self.HyperPeriod)
        self.ResultList=[0]*self.HyperPeriod
        self.TotalResult=[" "]*self.HyperPeriod
        print("HyperPEriod is ",self.HyperPeriod)
        
    def PollServerTask(self, puttimehere):      
        PSExe=[self.PSExeTime]
        time=puttimehere
        for i in range(len(self.PollServerTasks)):
            while True:
                a=self.PollServerTasks[i].ExeTask(exe=PSExe, Totallist=self.TotalResult, time=time)
                if a==0:
                    break
                elif a==1:
                    self.ResultList[time]=[self.PollServerTasks[i].GetName(), self.PollServerTasks[i].GetInterruptTime()]
                    time+=1
        if (PSExe[0]==self.PSExeTime):
            return True
        return False
        
    def CalTask(self):
        for i in range(self.HyperPeriod):#iterating one cycle of HyperPerid
            print("Time ",i)
            self.Interrupter(i)
            if i%self.PSPeriod==0:
                result=self.PollServerTask(i)
                i= i +self. PSExeTime-1 #Just in case Polling server exetime is bigger than 1
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if result==True:
                        self.PeriodicTasks[j].ExeTask(exe=time, Totallist=self.TotalResult, time=i)
                        """
                        if(self.PeriodicTasks[j].ExeTask(exe=time, Totallist=self.TotalResult, time=i)==1):
                            print("Executed ",j,"th Periodic task.\n\n")
                        """
                    else:
                        self.PeriodicTasks[j].AddCount()
            else:
                print("no polling period")
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if(self.PeriodicTasks[j].ExeTask(exe=time, Totallist=self.TotalResult, time=i)==1):
                        print("Executed ",j,"th Periodic task\n\n")
        print (self.TotalResult)
        return self.ResultList, self.TotalResult, self.HyperPeriod
            
class DeferrableService:
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
    ResultList=[]
    TotalResult=[]
    def __init__(self):
        self.name="DifferableService"
    
    def SetServer(self, inputlst):
        self.ConstDSExe=inputlst[0]
        self.DSPeriod=inputlst[1]
    
    def PushPeriodicTask(self,TaskObj):
        self.PeriodicTasks.append(TaskObj)
        self.PeriodicTasks.sort(key=lambda object:object.GetPeriod())
        #print (self.PeriodicTasks)
    
    def PushAPeriodicTask(self, TaskObj):
        self.AperiodicTasks.append(TaskObj)
    
    def Interrupter(self, time):#fnc for interruption and pushing aperiodic task
        value=False
        for i in self.AperiodicTasks:
            if time==i.GetInterruptTime():
                self.DeferrableServerTasks.append(i)
                value=True
        return value
    
    def CalHyperPeriod(self):
        self.HyperPeriod=self.DSPeriod
        for i in range(len(self.PeriodicTasks)):
            #print(self.PeriodicTasks[i].GetPeriod())
            self.HyperPeriod=lcm(self.HyperPeriod, self.PeriodicTasks[i].GetPeriod())
        self.HyperPeriod=int(self.HyperPeriod)
        self.ResultList=[0]*self.HyperPeriod
        self.TotalResult=[" "]*self.HyperPeriod
        print("HyperPEriod is ",self.HyperPeriod)

    def InitializeServer(self):
        self.DSExeTime[0]=self.ConstDSExe
        self.CacheDS=self.ConstDSExe
    
    def DeferrableTask(self, puttimehere):
        """
        time=puttimehere
        for i in range(len(self.DeferrableServerTasks)):
            while True:
                if self.DeferrableServerTasks[i].ExeTask(exe=self.DSExeTime, Totallist=self.TotalResult, time=time)==0:
                    break
                else:
                    self.ResultList[time]=[self.DeferrableServerTasks[i].GetName(), self.DeferrableServerTasks[i].GetInterruptTime()]
                    time+=1
        tic=self.CacheDS-self.DSExeTime[0]
        self.CacheDS=self.DSExeTime[0]
        return tic
        """
        for i in range(len(self.DeferrableServerTasks)):
            if(self.DeferrableServerTasks[i].ExeTask(exe=self.DSExeTime)==1):
                self.TotalResult[puttimehere]=[self.DeferrableServerTasks[i].GetName(), self.DeferrableServerTasks[i].GetInterruptTime()]
                self.ResultList[puttimehere]=[self.DeferrableServerTasks[i].GetName(), self.DeferrableServerTasks[i].GetInterruptTime()]
                return 1
        return 0        
    
    def CalTask(self):
        for i in range(self.HyperPeriod):#iterating one cycle of HyperPerid
            print("Time ",i)
            self.Interrupter(i)
            if i%self.DSPeriod==0:#해당 if 문은 필요하 없다. interrrupt가 리턴하는 값으로 조건 변경
               self.InitializeServer()
                #이부분이 달라져야한다. 
                #interrupt 들어올 때마다
            tic=self.DeferrableTask(i)
            if (tic==0):#if Defferable server did nothing
                time=[1]
                for j in range(len(self.PeriodicTasks)):
                    if(self.PeriodicTasks[j].ExeTask(exe=time)==1):
                        self.TotalResult[i]=[self.PeriodicTasks[j].GetName(), self.PeriodicTasks[j].GetInstanceNum()]
                    """
                    if(self.PeriodicTasks[j].ExeTask(exe=time, Totallist=self.TotalResult, time=i)==1):
                        continue

                        #print("Executed ",j,"th Periodic task\n\n")
                    """
            else: #if server did sth
                for k in range(len(self.PeriodicTasks)):
                    self.PeriodicTasks[k].AddCount()
                        
        print (self.TotalResult)
        return self.ResultList, self.TotalResult, self.HyperPeriod

def CalAveWaitingTime(resultlist):
    tasklist=dict()
    waitlist=[]
    for i in range(len(resultlist)):
        if type(resultlist[i]) is list:#AP task가 존재
            if tasklist.get(resultlist[i][0])==None:#아직 없음
                if i==resultlist[i][1]:
                    tasklist[resultlist[i][0]]=[resultlist[i][1]]                
                else:
                    tasklist[resultlist[i][0]]=[resultlist[i][1], i]
            else:#뭔가 있음 
                #print(tasklist.get(resultlist[i][0]), "여기다가 추가할 거", tasklist.get(resultlist[i][0]).append(i))
                temp=tasklist.get(resultlist[i][0])
                temp.append(i)
                tasklist[resultlist[i][0]]=temp
    for i in list(tasklist.values()):
        total=0
        if len(i)==1:
            waitlist.append(total)
            #print("appending", total)
            continue
        for j in range(len(i)):#이러면 리스트가 반환
            if j==0:#first element
                continue
            else:
                total=total+(i[j]-i[j-1])
        #print("appending", total)
        waitlist.append(total)
    #print("Wait lsit" , waitlist)
    #result=sum(waitlist)*1.0/len(waitlist)*1.0
    #print("acg wait time ", result)
    #print (tasklist)
    if len(waitlist)!=0:
        AvgWaitingTime=sum(waitlist)/len(waitlist)
    else:
            AvgWaitingTime=0
    waitlist=[sum(waitlist), len(waitlist)]
    print("Average Waiting Time: ", AvgWaitingTime)
    return waitlist

def HarmonizedInputGenerator():
    DivisorSet=[[3, 5], [2, 2, 5], [2, 3, 5]]
    
    SelectLCM=random.randrange(0,3)
    SelectLCM=DivisorSet[SelectLCM]
    
    Task=random.randrange(2,5)
    Period=[0]*Task
    Task=[0]*Task
    
    #
    for i in range(len(Task)):
        temp=[0]*len(SelectLCM)
        for j in range(len(SelectLCM)):
            temp[j]=random.randrange(0,2)
        Task[i]=temp
    
    for i in range(len(Period)):
        temp=1
        for j in range(len(Task[i])):
            if Task[i][j]==1:
                temp*=SelectLCM[j]
        if temp==1:
            temp*=SelectLCM[0]
        Period[i]=temp
    
    Task=[0]*len(Period)
    for i in range(len(Period)):
        Task[i]=random.randrange(3, int(math.floor(2**Period[i])))
        Task[i]=(Period[i]-math.floor(math.log(Task[i] ,2)))
    
    AP=min(Period)
    APIndex=Period.index(AP)
    Server=[Task[APIndex], Period[APIndex]]
    Task.remove(Task[APIndex])
    Period.remove(Period[APIndex])
    
    for i in range(len(Task)):
        Task[i]=[Task[i],Period[i]]

    #print (Task) #Regular tasks
    #print (Server) #server spec
    
    APTask=[-1]*random.randrange(1,4)
    LCM=1
    for i in Task:
        LCM=lcm(LCM,i[1]) 
    for i in range(len(APTask)):
        temp=random.randrange(0,LCM)
        #if APTask.count(temp)>0:
            
        #else:
        APTask[i]=temp
    for i in range(len(APTask)):
        APTask[i]=[1, APTask[i]]
    #print (APTask)
    #[server, Task, APTask]
    #print ([Server, Task, APTask])
    APTask.sort(key=lambda list:list[1])
    return [Server, Task, APTask]

def check(inputlist):
    #Function that checks if it's possible to schedule tasks with given info
    """
    left_hand=self.ConstDSExe/self.DSPeriod
    for i in self.PeriodicTasks:
        temp=i.GetExeTime()/i.GetPeriod()
        left_hand+=temp
        #print(left_hand)
    TotalTask=(len(self.PeriodicTasks)+1)
    right_hand=TotalTask*(2**(1/TotalTask)-1)
    return left_hand<=right_hand        
    """
    left_hand=inputlist[0][0]/inputlist[0][1]
    for i in inputlist[1]:
        left_hand+=(i[0]/i[1])
    right_hand=(len(inputlist[1])+1)*(2**(1/(len(inputlist[1])+1))-1)
    #print("left", left_hand)
    #print("right", right_hand)
    return left_hand<=right_hand

def InputGenerator():
    while True:
        inputlist=HarmonizedInputGenerator()
        if(check(inputlist)):
            break
    #print ("inputlist is ", inputlist)
    print("Server ExeTime/Period: ", inputlist[0][0],"/",inputlist[0][1])
    print("Periodic Task[ExeTime, Period]: ",inputlist[1])
    print("APeriodic Task[ExeTime, ArrivalTime]: ",inputlist[2])
    return inputlist

def module(inputlist):
        
    if inputlist[0]=="PollingService":
        obj=PollingService()
        #print("Polling")
    elif inputlist[0]=="DeferrableService":
        obj=DeferrableService()    
        #print("Def")
    else:
        #print("None")
        return 0
    obj.SetServer(inputlist[1])
    
    for i in range(len(inputlist[2])):
        obj.PushPeriodicTask(task_module.PeriodicTask("Task "+str(i+1),inputlist[2][i][0], inputlist[2][i][1]))
    for i in range(len(inputlist[3])):
        obj.PushAPeriodicTask(task_module.APeriodicTask("APTask "+str(i+1), inputlist[3][i][0], inputlist[3][i][1]))
    obj.CalHyperPeriod()
    APresult, TotalResult, HP=obj.CalTask()
    AvgWaitTime=CalAveWaitingTime(APresult)
    return AvgWaitTime, TotalResult, HP

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
           
    test1=DeferrableService()
    test1.PushPeriodicTask(task_module.PeriodicTask("Task A",4, 10))
    test1.PushPeriodicTask(task_module.PeriodicTask("Task B",8, 20))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask A", 1, 5))
    test1.PushAPeriodicTask(task_module.APeriodicTask("APTask B", 1, 12))
    test1.CalHyperPeriod()
    test1.CalTask()
    """
    lst1=["DeferrableService", [[4,10],[8,20]],[[1,5],[1,12]]]
    lst2=["PollingService", [[4,10],[8,20]],[[1,5],[1,12]]]
    #현재 상황
    #input을 위처럼 리스트로 만들어 주면
    #결과 값으로 avg wait time을 계산해주낟.
    #더 구현해야할 것이. aptask와 ptask를 동시에 리턴하는 변수를 아직 안만들었다.
    #그리고 flask와 연결해야함.
    
    #module(lst1)    
    list3=InputGenerator()
    list3.insert(0, "DeferrableService")
    module(list3)
    