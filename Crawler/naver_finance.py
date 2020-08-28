# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:10:25 2020

@author: dhk13
"""

import requests
from bs4 import BeautifulSoup as soup

url="https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258"
txt=requests.get(url).text

soup=soup(txt, "html5lib")
print(len(soup.body('ul')[5]))
#print(soup.body.ul)
print(len(soup.body('ul')[5].find('dl')))
#print(soup.body('ul')[5].find_all('dt'))
for i,content in enumerate(soup.body('ul')[5].find('dl')):
    if(i%2==1):
        print(content.attrs)
        print(content)
    