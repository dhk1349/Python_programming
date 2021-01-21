# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:07:29 2020

@author: dhk13
"""

class Solution:
    def __init__(self):
        self.values={'M':1000, 'D':500, 'C':100, 'L': 50, 'X':10, 'V':5, 'I':1}
            
    def romanToInt(self, s: str) -> int:
        val=0
        g_cursor=0
        while True:
        #전체 윈도우
            if(g_cursor==len(s)-1):
                val+=self.values[s[g_cursor]]
                return val
            elif(g_cursor>len(s)-1):
                return val
            
            elif(self.values[s[g_cursor]]<self.values[s[g_cursor+1]]):#다음 자리의 기호가 더 큰경우 (빼야하는 경우)
                val+=(self.values[s[g_cursor+1]]-self.values[s[g_cursor]])
                g_cursor+=2
                
            elif(self.values[s[g_cursor]]>=self.values[s[g_cursor+1]]):
                val+=self.values[s[g_cursor]]
                g_cursor+=1
            

            
        return val 
    
a=Solution()

print(a.romanToInt("IX"))