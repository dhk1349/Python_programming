# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:43:28 2020

@author: dhk13
"""

import requests
from bs4 import BeautifulSoup as soup
import openpyxl

#url=input("rul: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
url="https://www.amazon.com/s?k=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&ref=nb_sb_noss"
url2="https://www.amazon.com/s?k=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&ref=nb_sb_noss"
source=requests.post(url, headers=headers)
print(source)
if (source.status_code!=200):
    print("Illegal form of url")
    print(source.status_code)

    
soup=soup(source.text, 'html.parser')

header=soup.find('header').find('div',{'id':'nav-search'}).find('input',{'id':'twotabsearchtextbox'}).get('value')
print(header)

body=soup.find('div',{'class':'s-main-slot s-result-list s-search-results sg-row'}).find_all('div',{'data-component-type':'s-search-result'})


wb=openpyxl.Workbook()
sheet1=wb['Sheet']
sheet1['A1']=header
rownum=2
maxa=0
maxb=0
maxc=0
for item in body:
    print(item.find('h2').text.rstrip("\n"))
    sheet1['A'+str(rownum)]=item.find('h2').text.rstrip("\n")
        
    price=item.find('div',{"class":"sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"}).find('span',{'class':'a-offscreen'})
    if(price!=None):
        print(price.text)
        sheet1['B'+str(rownum)]=price.text
    else:
        sheet1['B'+str(rownum)]="NONE"
        
    print(item.find('img')['src'])
    sheet1['C'+str(rownum)]=item.find('img')['src']
    #print(item.find('div',{'class':'sg-row'}).find('span',{'class':'a-size-medium a-color-base a-text-normal'}).text)
    #print(item.find('span',{'class':'a-size-base a-color-secondary'}))
    
    if(maxa<len(item.find('h2').text.rstrip("\n"))):
        maxa=len(item.find('h2').text.rstrip("\n"))
    if(maxb<len(sheet1['B'+str(rownum)].value)):
        maxb=len(sheet1['B'+str(rownum)].value)
    if(maxc<len(item.find('img')['src'])):
        maxc=len(item.find('img')['src'])
    rownum+=1
    
sheet1.column_dimensions['A'].width = int(maxa*0.15)
sheet1.column_dimensions['B'].width = maxb
sheet1.column_dimensions['C'].width = maxc


wb.save('./'+header+'_AMAZON'+'.xlsx')
wb.close()