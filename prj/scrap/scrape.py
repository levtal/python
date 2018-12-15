from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
print (soup.prettify().encode('utf8'))
match = soup.title.text
print('Title =',match)
 
#header = soup.find_all('header',class_='entry-header')
for article in  soup.find_all('header',class_='entry-header'):
    hd = article.h2.a.text
    #header = soup.find("header", {"class": "entry-header"})
     #print('header = ',header.encode('utf8') )
    print()
    print( hd.encode('utf8'))
 #21
# https://www.youtube.com/watch?v=ng2o98k983k