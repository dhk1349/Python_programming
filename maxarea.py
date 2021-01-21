# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:23:45 2020

@author: dhk13
"""

data=[6,4,3,1,4,6,99,62,1,2,6]
data=[2,3,4,5,18,17,6]

class Solution:
    def maxArea(self, height):
        """
        width를 기준으로 width가 한 칸 작아질 때마다 height가 무조건 커져야함.
        """
        width=len(height)-1
        window=1
        Areaset=[width,  min(height[0],height[width])]
        MaxArea=Areaset[0]*Areaset[1]
                 
        while(width!=1):
            window+=1
            width-=1
            
            if(MaxArea/width > max(height[:])):
                print(MaxArea/width)
                break
            
            for i in range(window): #[0,1]
                 tmp=min(height[i], height[width+i])
                 if tmp>Areaset[1]:
                    newArea=tmp*width
                    if MaxArea<newArea:
                        MaxArea=newArea
                        Areaset=[width, tmp]
        return MaxArea, Areaset
A=Solution()
print(len(data))
print(A.maxArea(data))