#coding=utf-8
import re,os
from urllib.request  import urlretrieve 
import requests
from bs4 import BeautifulSoup
import random
 
def geturl(url):
    html=requests.get(url).content
    soup=BeautifulSoup(html,'html')
    return soup
 
#抓取电影海报
soup=geturl('http://dianying.2345.com/list/kehuan-------5.html')
bookAlbum=soup.title.string.split('_')[0]
# print(bookAlbum)
tags=soup.find_all(class_='v_picConBox mt15')
# print(tags)
movies=[]
for tag in tags[0].find_all('li'): 
	pic=  tag.find("div",{"class": "pic"})  
	if  pic is None:
		continue
	text = tag.find("div",{"class": "txtPadding"}) 
	img_url = pic.img['data-src']
	title =text.span.em.a['title']
	# print(title,img_url)
	movies.append([title,img_url])
	# print(movies)
if not os.path.exists(bookAlbum):
    os.makedirs(bookAlbum)
    for movie in movies:
        num=random.randint(1,10000)
        strname=random.choice('abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLMZNXBCV')
        filename=os.path.join(bookAlbum,str(num)+strname+'.png')
        print(filename)
        with open(filename,'w') as f:
            urlretrieve('http:'+movie[1],filename)
            
 
