# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:48:56 2020

@author: dhk1349
"""

n = int(input()) #목표채널 
m = int(input())
broken=[int(i) for i in input().split()] #망가진 버튼 
normal=[i for i in range(10)] #사용가능한 버튼 
ans=abs(n-100)  #시작 시 정답 


for i in broken:
    normal.remove(i)


tempnum=0
iternum=1

def solve(lst, target):
    #가장 유사한 숫자를 뱉
    














while n!=0:
    val=n%10
    n=n/10
    
    if val not in normal:
            
    
    tempnum+=(iternum*val)
    iternum*=10
