import time

#perfect numbers


#wersja 1:  while, if, append

def prefekt(limit):
    n = 1
    result=[]
    while n <= limit:
        sum = 0
        divisor = 1
        while divisor < n:
            if not n % divisor:#reszta to 0
                sum += divisor
            divisor = divisor + 1
        if sum == n:
            result.append(n)
        n = n + 1
    return(result)




t=time.time()
prefekt(1000)
t2=time.time() -t
print(t2)

#wersja 2:list comprehension
t3=time.time()

print([x for x in range(1,1000) if sum(y for y in range(1,x) if x%y==0)==x])

t4=time.time() -t3
print(t4)


'''def ifactors(n):
    return [i for i in range(2, n/2+1) if n % i == 0]------daje nam dzielniki
def perfect(n):
    return [i for i in range(2, n+1) if sum(ifactors(i)) + 1 == i] '''




#wersja 3: implementacja funkcyjna, map, filter,reduce ...

def perf(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
 


t5=time.time()
print (list(filter(perf, range(1, 1000))))
t6=time.time() -t5
print(t6)



