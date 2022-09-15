import requests
import difflib
import time



def get_adres(adres):

    strona = requests.get(adres)
    strona = str(strona.content)
    return strona.split()

'''The GET method indicates that you’re trying to get or retrieve data from a specified resource.
his is the same type of request your browser sent to view this page, but the only difference is that
Requests can't actually render the HTML, so instead you will just get the raw HTML and the other response information.'''


def print_err(err_list):
    
    for line in err_list:
        if line[0] == '-':
            print(line)

    

def monit(adres_list, powtorzen, sek):

    strony = []

    for adres in adres_list:
        strony.append(get_adres(adres))# lista adresów, już po get_adres

    for i in range(powtorzen):

        time.sleep(sek)
        strony2 = []

        for j in range(len(adres_list)):
            strony2.append(get_adres(adres_list[j]))# lista adresów, już po get_adres, po sleep

            diffinstance = difflib.Differ()#twożenie obiektu Differ
            difflist = list(diffinstance.compare(strony[j], strony2[j]))#sprawdzam stronę początkową ze stroną po upływie czasu - wynik jako lista

            print('_'*10,i,'iter','_'*10, adres_list[j], '_'*10)#info
            print_err(difflist)#wypisuje, co było inne

        strony = strony2#każde iter porównywane z poprzednim, a nie stanem początkowym


#lista = ['https://sites.google.com/a/cs.uni.wroc.pl/aisd/', 'https://timestampgenerator.com/']
#lista = ['https://sites.google.com/a/cs.uni.wroc.pl/aisd/']
#lista = ['https://www.ii.uni.wroc.pl/~marcinm/']
lista = ['https://www.ii.uni.wroc.pl/~marcinm/', 'https://timestampgenerator.com/']
#lista = ['https://timestampgenerator.com/']

monit(lista, 3, 10)



#jak linijki są podobne, to po prostu je wypisze ...   '  ...   3.   Simple is better than complex.\n'
#jak linijki nie są takie same '-   1. Beatiful is better than ugly.\n', 
#                              '+   1. Beautiful is better than ugly.\n', '?         +\n'
#wypisze obie, ale tam gdzie miej tekstu zrobi '-' na pocątku


# jak różnią sią zawartością, a mają tą samą liczbę słów, to wtpisze tak :

#'-   1. Beartiful is better than ugly.\n', '?         ^\n', 
#'+   1. Beautiful is better than ugly.\n', '? 