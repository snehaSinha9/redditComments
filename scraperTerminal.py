#!/usr/bin/python
#import gi
import requests
import re
from bs4 import BeautifulSoup


URL=input('Paste the URL of the Reddit post you want to follow: ')


headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(URL, headers= headers)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

div_Txt = soup.find_all("div",{'data-test-id':"comment"})
post_content =soup.div.find_all('h1')[0].get_text()
print("POST: %s" %post_content)


count = 0

for comment in div_Txt:
    text = comment.get_text() 
    count +=1
    print('%d.\t %s' %(count, text))
