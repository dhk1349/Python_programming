# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:33:26 2020

@author: dhk13
"""

import numpy as np

x1=np.array([1536/10000, 3456/10000, 3456/10000, 1296/10000, 256/10000])

log2x1=np.log2(x1)


x2=np.array([2500/10000, 3750/10000, 2500/10000, 625/10000, 625/10000])
log2x2=np.log2(x2)

x3=np.array([3456/10000, 3456/10000, 1536/10000, 256/10000, 1296/10000])
log2x3=np.log2(x3)


entropy1=-sum(x1*log2x1)

entropy2=-sum(x2*log2x2)

cross_ent1=entropy1+sum(x1*np.log2(x1/x2))

cross_ent2=entropy1+sum(x1*np.log2(x1/x3))

print(entropy1)
print(entropy2)

print(cross_ent1)
print(cross_ent2)



#########################################
################KL#######################

KL1=sum(x1*np.log2(x1/x2))

KL2=sum(x1*np.log2(x1/x3))

print(KL1)

print(KL2)

print((6*(1/4*(-3.2)**2-1)**2-6*(1/4*(-3.2)**2-1))*3.2)









