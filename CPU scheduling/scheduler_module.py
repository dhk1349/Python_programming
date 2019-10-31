# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:58:21 2019

@author: dhk13
"""

class PollingService:
    """
    Polling Service
    Polling server가 excecution time과 Period를 가진다.
    그리고 주기가 돌아올 때마다 Aperiodic task가 쌓여있으면,
    execution time을 할애해서  Aperiodic task를 수행한다.

    Periodic task는 주기가 짧은 task가 우선 순위를 가지고 수행된다.

    """
    Name=""
    PeriodicTask=[]
    PeriodicExeTime=[]

    AperiodicTask=[]
    AperiodicExeTime=[]
    AperiodicArrivalTime=[]

    PSExeTime=0
    PSPeriod=0

    HyperPeriod=0
    TaskQueue=[]
    def __init__():
        self.Name="Polling Service"

    def PushInfo():
        return 0

    def CalHyperPeriod():
        
    def CalTask():
        for i in range(self.HyperPeriod):


        return 0

class DefferableService:

    def __init__():
