# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:43:07 2020

@author: dhk13
"""

class Solution:
    def __init__(self):
        self.values={'M':1000, 'D':500, 'C':100, 'L': 50, 'X':10, 'V':5, 'I':1}
    def intToRoman(self, num: int) -> str:
        output=""
        lst=list(self.values.items())
        print(lst)
        while True:
            for idx, (char, val) in enumerate(lst):
                if(num==0):
                    return output
                
                elif(num//val > 0):
                    output+=char
                    num-=val
                    break
                elif(num//val == 0):
                    if(idx%2==0): #1로 시작하는 단위
                        if num//(val-lst[idx+2][1])!=0:
                            output+=lst[idx+2][0]
                            output+=lst[idx][0]
                            num-=(val-lst[idx+2][1])
                    else: #5로 시작하는 단위
                        if num//(val-lst[idx+1][1])!=0:
                            output+=lst[idx+1][0]
                            output+=lst[idx][0]
                            num-=(val-lst[idx+1][1])
                print(output, num)
        return output
    
a=Solution()
#print(a.values)
print(a.intToRoman(1994))
