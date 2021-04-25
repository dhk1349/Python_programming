# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:27:44 2021

@author: dhk1349
"""
import csv
wwith open("test.txt",'r') as file, open("testout.csv",'w') as outfile:
    for row in file:
        row=row.replace(",","")
        outfile.write(row.replace(' ', ','))