#prime numbers
import time
#wersja 1:  while, if, append
def primes_n(n):
    l=[]
    for val in range(0, n): 
        if val > -1:#jakby od 1, to nie wypisze 0, 1
            for n in range(2, val): 
                if (val % n) == 0: 
                        break
            else: 
                l.append(val) 
    return l


t=time.time()
print(primes_n(1000))
t2=time.time() -t
print(t2)


#wersja 2:list comprehension

n=1000

t3=time.time()

print([x for x in range(0, n)
     if all(x % y != 0 for y in range(2, x))])
t4=time.time() -t3
print(t4)





#wersja 3: implementacja funkcyjna, map, filter,reduce ...



primelist = lambda n : [x for x in range(0, n) if not 0 in map(lambda z : x % z, range(2,x))]


t5=time.time()
print (list( primelist(1000)))
t6=time.time() -t5
print(t6)
