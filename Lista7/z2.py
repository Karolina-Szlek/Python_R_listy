import requests
import difflib
import time
from threading import Thread

def pobierz_adres(adres):

    strona = requests.get(adres)
    strona = str(strona.content)
    return strona.split()


def wypisz_bledy(lista_bledow, adres_strony):
    
    for line in lista_bledow:
        if line[0] == '-':
            print(adres_strony, "\n zmiana:  ", line, "\n \n")

 
    
def monit(adres, powtorzen, sek):

    strona = pobierz_adres(adres)


    for i in range(powtorzen):

        time.sleep(sek)
        zaktualizowana_strona = pobierz_adres(adres)

       
        diffinstance = difflib.Differ()
        difflist = list(diffinstance.compare(strona, zaktualizowana_strona))

        #print(i,'_'*10, adres, '_'*10)
        wypisz_bledy(difflist, adres)

        strona = zaktualizowana_strona


lista_adresow = ['https://sites.google.com/a/cs.uni.wroc.pl/aisd/', 'https://timestampgenerator.com/']
#monit('https://timestampgenerator.com/', 3, 10)
lista_watkow = []
for adres in lista_adresow:
    lista_watkow.append(Thread(target = monit, args = (adres, 3, 10)))
for watek in lista_watkow:
    watek.start()
    
    
    