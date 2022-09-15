
#AKUMULATOR
# nie dziala


def sudan(x, y, n ):
     if n == 0:
          return (x+y)
     if n is not 0 and y == 0 and x >= 0:
        return x
     else:
          return sudan(sudan(x, y-1, n), (sudan(x,y-1,n)+y) , n-1)
          


print ("\nThe result of your inputs according to the Ackermann Function is:")
print ("\n")
print (sudan(6, 5, 0)) #11
print (sudan(14, 14, 1)) #262128
print (sudan(7, 4, 1)) #759
print (sudan(1, 1, 2)) #759



def sudan1(x, y, n, acu ):
    acc = acu
    if n == 0:
        acc = x+y
        return acc
    if n is not 0 and y == 0 and x >= 0:
        acc = x
        return acc
    else:

        return sudan1(sudan1(x, y-1, n, acc ), (sudan1(x,y-1,n, acc)+y) , n-1, acc )