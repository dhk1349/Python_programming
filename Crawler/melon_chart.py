from bs4 import BeautifulSoup as soup
import unicodedata
import urllib.request

def fill_str_with_space(input_s="", max_size=40, fill_char=" "):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)

url="https://www.melon.com/chart/index.htm"
#url2="https://www.naver.com"


headers = {'User-Agent': 'Mozilla/5.0',}
req=urllib.request.Request(url, headers=headers)
html=urllib.request.urlopen(req)


obj=soup(html.read(), "html.parser")
table=obj.find('div',{"class":"service_list_song type02 no_rank d_song_list"}).find('tbody').find_all("tr")

print(len(table))
for idx,i in enumerate(table):
    song=i.find('div',{"class":"ellipsis rank01"}).get_text().strip()
    singer=i.find('div',{"class":"ellipsis rank02"}).find('a').get_text().strip()
    album=i.find('div',{"class":"ellipsis rank03"}).get_text().strip()

    #print(f"{idx+1:4}위 | {song:50} | {singer:30} | {album:30}")
    print(f"{idx+1:4}위 | {fill_str_with_space(song, max_size=55)} | {fill_str_with_space(singer, max_size=30)} | {fill_str_with_space(album, max_size=30)}")
print(f"status code: {html.getcode()}")
