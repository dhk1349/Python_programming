# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:14:25 2020

@author: dhk13
"""

#############################
##############1번##############
#############################



season=input("어떤 계절인가요?")
temp=int(input("몇 도인가요?"))

if(season=="summer"):
    if(temp>=30):
        print("hot")
    elif(temp<=29 and temp>=20):
        print("warm")
    elif(temp<=19):
        print("cool")
    
elif(season=="winter"):
    if(temp>=10):
        print("warm")
    elif(temp<=9):
        print("cold")
    
else:
    print("Exception")
    
    
    
    


#############################
##############2번##############
#############################

code=input("국가코드: ")
if(code=="K"):
    print("내국인")
elif(code=="E" or code=="U"):
    print("서양인")
elif(code=="J" or code=="C"):
    print("동양인")
else:
    print("Exception")




