from bs4 import BeautifulSoup
import requests

word ='divergence'
url = 'http://www.morfix.co.il/'+ word
try:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
except Exception as e:
     print('No Internet Connection','\n\n',e)

tr4 = soup.find('div',class_="translation translation_he heTrans")
try:
    out = tr4.text
except Exception as e:
    out  = None  #No p tab
print(out)