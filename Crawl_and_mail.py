# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:21:23 2021

@author: dhk1349
"""
import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from bs4 import BeautifulSoup as soup
import urllib
import time
import datatime

def crwal_and_mail(info):
    for url in info['urls']:
        req = urllib.request.Request(url, headers = header)
        html = urllib.request.urlopen(req)
        html = soup(html, 'html.parser')
        prod_name = url.split('/')[4]

        req_size = ['8', '8.5', '9', '9.5']
        available_sizes = []

        size_tag = html.find("div", class_="row dyanamic-attr")

        for size in req_size: 
            button = size_tag.find("button", {"title":size})
            if(button['class'][-1] == "selectable"):
                available_sizes.append(size)

        if len(available_sizes)>0:
            print(prod_name, available_sizes, url)
            #email function
            mail(info, prod_name, available_sizes, url)


def mail(info, prod_name, sizes, url):
    email = info['id']
    pw = info['pw']

    toAddr = info['dest']

    smtp = smtplib.SMTP('smtp.gmail.com', 587)   # 587: 서버의 포트번호
    smtp.ehlo()
    smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
    smtp.login(email, pw)
    
    for size in sizes:
        msg = MIMEMultipart()    #msg obj.
        msg['Subject'] = f"Restock Notification of {prod_name} {size}"
    
        # text msg
        part = MIMEText(url)
        msg.attach(part)   #msg에 part obj.를 추가해줌
    
        for addr in toAddr:
            msg["To"] = addr
            smtp.sendmail(email, addr, msg.as_string())
                #msg는 object이기 때문에 전송을 위해 .as_string()으로 문자열로 바꿔야함(parsing)
    smtp.quit()

if __name__=="__main__":
    infopath = "C:/Users/한동훈/Desktop"
    with open(os.path.join(infopath,'email.pkl'), 'rb') as f:
        info = pickle.load(f)
    header = {'User-Agent':'Chrome/66.0.3359.181'}
    
    while True:
        print(datatime.datetime.now())
        crwal_and_mail(info)
        time.sleep(60*30)  #sleep for 30 minutes
    for url in info['urls']:
        print(url)