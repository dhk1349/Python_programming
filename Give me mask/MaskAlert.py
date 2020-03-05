# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:15:58 2020

@author: dhk1349
"""
import requests
from bs4 import BeautifulSoup
import webbrowser
import time, random


well="http://www.welkeepsmall.com/shop/shopbrand.html?type=X&xcode=023"
html=requests.get(well)


#print(html.text)
while True:
    if (html.status_code==200):
        soup=BeautifulSoup(html.text,'html.parser',from_encoding='utf-8')
        table=soup.find("body").find("div",{"id":"contentWrapper"}).find("table")
        items=table.find_all("td")
        #print(table)
        
        for i in range(4,len(items)):
            #print(i)
            print(items[i].find("li",{"class":"soldout"}))
            if(items[i].find("li",{"class":"soldout"})==None or items[i].find("li",{"class":"soldout"}).text!="SOLD OUT"):
                #print("NONE find")
                webbrowser.open(".\play_this_song.mp3")
                break
        print("+++++++++++++++++++++++++++++++++++++")
        time.sleep(random.randrange(60,80))

        
        """
        if (items!=None):
            f=open("body.txt",'w')
            for i in items:
                print(i)
            f.close()
        else:
            print("Nothing")
        """
    else:
        print(html.status_code)
        time.sleep(random.randrange(60,80))
        continue