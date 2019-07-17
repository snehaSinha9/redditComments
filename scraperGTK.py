#!/usr/bin/python
import gi
gi.require_version('Gtk','3.0')
import requests
import re
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
from gi.repository import Gtk
import time 

URL=input('Paste the URL of the Reddit post you want to follow: ')

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}



def getComments():
    page = requests.get(URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    divTxt = soup.find_all("div", {'data-test-id':"comment"})
    title = soup.div.find_all('h1')[0].get_text()
    count = 0
    message = ''

    for comment in divTxt:
        text = comment.get_text() 
        count +=1
        message = message + str(count) + '.\t'+ text + '\n'


    Gtk.init(None)
    Hello = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                              buttons=Gtk.ButtonsType.OK,
                              text=title,
                              secondary_text=message)

    Hello.run()

if __name__== "__main__":
    while(True):
        getComments()
        time.sleep(60)
