


def pierwiastek (n):
    sum = 0
    k = 0
    while sum < n: #n, czy k ?
        k += 1
        sum += (2*k -1)
    
    if sum == n:
        return k
    else:
        return k-1





print ("pierwiastek z 4:" , str(pierwiastek(4)))
print ("pierwiastek z 9:" , str(pierwiastek(9)))
print ("pierwiastek z 24:" , str(pierwiastek(24)))# 4.898
print ("pierwiastek z 25:" , str(pierwiastek(25)))
print ("pierwiastek z 269:" , str(pierwiastek(269)))# 16.401