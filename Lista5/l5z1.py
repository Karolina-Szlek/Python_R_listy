from time import time
#from texttable import Texttable


def primes_im(n):
    l=[]
    for val in range(2, n): 
        if val > -1:#jakby od 1, to nie wypisze 0, 1
            for n in range(2, int(i ** 0.5) + 1): 
                if (val % n) == 0: 
                        break
            else: 
                l.append(val) 
    return l



def primes_lc(n):
    return([x for x in range(2, n)
        if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))])


def primes_fun(n):
    return([x for x in range(0, n) if not 0 in map(lambda z : x % z, range(2,int(n ** 0.5) + 1))])


def is_prime(n):    
    for d in range(2, int(n ** 0.5) + 1):        
        if n % d == 0:            
            return False    
    return True

class Primes:

    def __init__(self,max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:#przekracza limit
            raise StopIteration
        elif is_prime(self.number):#jak pierwsza - zwróć
            return self.number
        else:
            self.__next__()#jak nie - patrz kolejna


res = [["Czas","Imperatywna","Funkcyjna","Skladana","Iterator"]]
i = 10

while i <= 128000:
    t00 = time()
    primes_im(i)
    t01 = time() - t00

    t10 = time()
    primes_fun(i)
    t11 = time() - t10

    t20 = time()
    primes_lc(i)
    t21 = time() - t20

    t30 = time()
    primes = Primes(i)
    for e in primes:
        pass
    t31 = time() - t30

    res.append([i,t01,t11,t21,t31])
    i *= 10



for i in res:
    print(i) 
    #print('\n')

#t = Texttable()
#t.add_rows(res)
#print(t.draw())