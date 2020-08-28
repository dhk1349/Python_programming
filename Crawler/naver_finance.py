# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:10:25 2020

@author: dhk13
"""

import requests
#from bs4 import BeautifulSoup as soup
import datetime
def replacer(data):
    result=data
    result=result.replace("?"," ")
    result=result.replace("\\"," ")
    result=result.replace("/"," ")
    result=result.replace("*"," ")
    result=result.replace("\""," ")
    result=result.replace("<"," ")
    result=result.replace(">"," ")
    result=result.replace("|"," ")
    result=result.replace(":"," ")
    result=result.replace("\t","")
    result=result.replace("\n","") 
    return result




url="https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258"
url2="https://finance.naver.com/news/mainnews.nhn?date="
date="2017-08-28"


def get_subarticle(url):
    #import requests
    import re
    from bs4 import BeautifulSoup as soup
    article=requests.get(url).text
    subsoup=soup(article, "html5lib")
    article_body=subsoup("body")[0].find("div",{"id":"wrap"}).find("div",{"id":"newarea"}).find("div",{"id":"contentarea"}).find("div",{"id":"contentarea_left"}).find("div",{"id":"content"}).text
    EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    article_body = EMOJI.sub(r'',article_body)
    
    
    """
    정규식 추가 필요 
    """
    
    
    
    return replacer(article_body.replace("\t","").replace("\n",""))
    

def save_by_date(url):
    #import requests
    from bs4 import BeautifulSoup as soup
    txt=requests.get(url).text
    soup=soup(txt, "html5lib")
    #print(soup.body.ul)

    container=soup.find('div',{'id':'contentarea_left'}).find('div',{'class':'mainNewsList'}).find('ul',{'class':'newsList'})
    #print(soup.body('ul')[5].find_all('dt'))
    for i,content in enumerate(container.find_all('li')):
        #print(content.attrs)
        if(content('dl')[0].find('dt',{'class':'thumb'})==None):
            #thumbnail이 없으면 제목이 dt가 됨 
            title=content('dl')[0].find('dt', {'class':'articleSubject'})
            ref=content('dl')[0].find('dt', {'class':'articleSubject'}).find('a').attrs['href']
        else:
            title=content('dl')[0].find('dd', {'class':'articleSubject'})
            ref=content('dl')[0].find('dt', {'class':'thumb'}).find('a').attrs['href']
        body=content('dl')[0].find('dd', {'class':'articleSummary'}).text.split("\n")
        #print(body)
        #print(body[3].strip('\t').replace(":", ";")+"_"+title.text.strip("\n"))
        
        url2="https://finance.naver.com"+ref
        article=get_subarticle(url2)
        print(article)
        print(url2)
        f=open(replacer(body[4].replace("\n", "\t").strip('\t').replace(":", "."))+"_"+replacer(title.text.replace("\n", "\t").strip('\t'))+".txt", 'w', encoding="utf-8")
        #title
        f.write(title.text.replace("\n", "\t").strip('\t').replace("\t","").replace("\n","")+"\n\n")
        #date
        f.write(body[4].replace("\t","").replace("\n","")+"\n\n")
        #content
        f.write(article)
        f.close()
date=datetime.date(2020,8,28)
save_by_date(url2+date.isoformat())

"""
date=datetime.date(2019,1,1)
for i in range(365):
    print(date.isoformat())
    save_by_date(url2+date.isoformat())
    date=date+datetime.timedelta(days=1)
"""