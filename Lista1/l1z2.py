


def min_coins(n,amount):# coin walue lista wartosci, n ilośc nominałów, amount do zapłaty)

    coin_value = [20,10,5,2,1]
    for i in range(0,n):
        while amount >= coin_value[i] :
    
      
            amount= amount - coin_value[i]
            
            print(coin_value[i])


min_coins(5,43)

def min_coins(n,amount):# coin walue lista wartosci, n ilośc nominałów, amount do zapłaty)

    pay = []
    coin_value = [20,10,5,2,1]
    for i in range(0,n):
        while amount >= coin_value[i] :
    
      
            amount= amount - coin_value[i]
            pay.append(coin_value[i])

    
    o=0
    t=0
    f=0
    ten=0
    twenty=0


    for i in range (len(pay)):
        if pay[i] == 1:
            o=o+1
        if pay[i] == 2:
            t=t+1
        if pay[i] == 5:
            f=f+1
        if pay[i] == 10:
            ten=ten+1
        if pay[i] == 20:
            twenty=twenty+1



    print ("To pay we need:")
    print ("1zł x",o)
    print ("2zł x",t)
    print ("5zł x",f)
    print ("10zł x",ten)
    print ("20zł x",twenty)

min_coins(5,43)
