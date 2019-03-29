#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:15:24 2019

@author: donghoon
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import datetime


def urlcreate():
    now=datetime.datetime.now()
    nowdate=now.strftime('%Y%m%d')
    html="https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId="
    html_container=[]
    for i in range(0,6):
        html_container.append(html+str(i+100)+"&date="+nowdate)
    
    return html_container
#html=urlopen("https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=20190328")




def scraper(container):
    for i in container:
        obj=urlopen(i)
        news=soup(obj,"html.parser")
        
        news_title=news.find("body").find("div",{"id":"wrap"}).find("table",{"class":"container"}).find("td",{"class":"content"}).find("div",{"class":"content"}).find("div",{"class":"ranking_category"}).find("div",{"class":"ranking_category_inner"}).find("li",{"class":"ranking_category_item is_selected"})
        news_box=news.find("body").find("div",{"id":"wrap"}).find("table",{"class":"container"}).find("td",{"class":"content"}).find("div",{"class":"content"}).find("div",{"class":"ranking"}).find_all("li")#.find("ul",{"class":"ltype06_headline"})#.findAll("li")#.find("td",{"class":"content"}).findAll("div",{"class":"list_body newsflash_body"})
        print("*************************")
        print(nowdate)
        print(news_title.text[0:-4])
        for i in news_box:
            print(i.find("div",{"class":"ranking_text"}).find("div",{"class":"ranking_headline"}).text.strip())
            print(i.find("div",{"class":"ranking_text"}).find("div",{"class":"ranking_lede"}).text.strip())
            print(i.find("div",{"class":"ranking_text"}).find("div",{"class":"ranking_office"}).text)
            print(i.find("div",{"class":"ranking_text"}).find("div",{"class":"ranking_view"}).text)
            print("\n")
        print("*************************")


#article=container[0].find("tbody").find("td",{"class":"content"}).findAll("div",{"class":"list_body newsflash_body"})

#print(container)

scraper(urlcreate())