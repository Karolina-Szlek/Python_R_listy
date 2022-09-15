#!/usr/bin/env python
 
from lxml import html
import urllib
import re
import requests
from bs4 import BeautifulSoup
from collections import Counter
 
def update2(key, list_of_pages, new):
    amount = slownik_d_s[new][key]
    begining = list()
    i = 0
    while i < len(list_of_pages): 
        if slownik_d_s[list_of_pages[i]][key] > amount:
            begining.append(list_of_pages[i])
        else:
            begining.append(new)
            begining = begining + list_of_pages[i:]
            return begining
        i += 1
    begining.append(new)  
    return begining  

def indeks(adres,depth):
    licznik = 0
    strona = urllib.request.urlopen(adres)
    html = strona.read()
    st = BeautifulSoup(html, 'html.parser')
    for link in st.findAll('a', attrs={'href': re.compile("^https://")}):
        if licznik < 4: 
            if ((depth>0) and (link.get('href') not in slownik_d_s)): 
                l=link.get('href')
                print(l) 
                licznik += 1 
                indeks(l, depth-1)
            
            
    data = st.findAll(text=True)
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        '\n' ,
        '.' ,
        ',',
    ]
    for t in data:
	    if ((t.parent.name not in blacklist) and (t not in blacklist)):
		    output += '{} '.format(t)


    text_list = dict(Counter(list(output.split(' '))))
    slownik_d_s.update({adres : text_list})
    print(adres) 
    for word in output.split(' '):

        if (word in slownik_slow):
            lista = slownik_slow[word]
            if not(adres in lista):
                l= update2(word, lista, adres)
                #slownik_slow.update({word: l}) 
                slownik_slow[word] = l
        else:
            l = list()
            l.append(adres)
            slownik_slow.update({word: l}) 
    return slownik_d_s


     
slownik_d_s = {}
slownik_slow = {}

ad = 'https://usefulangle.com/post/193/javascript-read-local-file'
print(ad)
indeks(ad,2)

print("---------------------------------")
print("lista stron zawierających słowo 'of'")
print(slownik_slow['of'])

print("---")
print(slownik_d_s['https://usefulangle.com/post/193/javascript-read-local-file']['of'])

print(slownik_d_s['https://usefulangle.com/css']['of'])


"""

for link in strona.findAll('a', attrs={'href': re.compile("^http://")}):
      print (link.get('href'))
#adres strony z horoskopem
urlwyborcza = 'http://horoskopy.gazeta.pl/horoskopy-magia/bliznieta/dzienny/'
#składam adres strony i daty w celu pobierania aktualnego horoskopu
urlwyborcza += data
 
#ścieżka do elementu XPATH
xpathwyborcza = '//*[@id="holder_230"]/div/p[1]/text()'
#pobiera stronę z horoskopem
pagewyborcza = requests.get(urlwyborcza)
#parsuje stronę
tree= html.fromstring(pagewyborcza.text)
# wyszukuje interesujący nas element
textwyborcza = tree.xpath(xpathwyborcza)
# wyświetla w yniki działania
print(data)
print (textwyborcza)
"""