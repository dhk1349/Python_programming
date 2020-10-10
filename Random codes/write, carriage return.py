# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:38:52 2020

@author: dhk1349
"""
import sys
import time
for i in range(10):
    sys.stdout.write(str(i))
    #sys.stdout.flush()
    sys.stdout.write(str(i))
    time.sleep(1)
    sys.stdout.write("\r")
    