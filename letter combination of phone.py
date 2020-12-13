# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:43:41 2020

@author: dhk13
"""
class Solution: 
    def __init__(self):
        cursor=97
        self.totallst=[]
        for i in range(2, 10):
            numlst=[]
            if(i==7 or i==9):
                num=4
            else:
                num=3
            for j in range(num):
                numlst.append(cursor)
                cursor+=1
            self.totallst.append(numlst)
            
            
    def recursive(self, digit, datalst):#digit은 남은 숫자
        if len(digit)==0:
            return datalst
        else:
            if len(datalst)==0: #처음이라 리스트가 비어있으면
                for i in self.totallst[int(digit[0])-2]:
                    datalst.append(chr(i))
                return self.recursive(digit[1:], datalst)
            else:
                nxtdatalst=[]
                for i in datalst:
                    for j in self.totallst[int(digit[0])-2]:
                        nxtdatalst.append(i+chr(j))
            
            
                return self.recursive(digit[1:], nxtdatalst)
        
        
    def letterCombinations(self, digits):
        datalst=[]
        return self.recursive(digits, datalst)
        
a=Solution()
print(a.letterCombinations("23"))