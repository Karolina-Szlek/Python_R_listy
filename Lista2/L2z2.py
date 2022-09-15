class Formula:

    def oblicz(self, dict):
        return ()
                 
    def __str__(self):
        return ("")

    def free(self):
        return set()



class T(Formula):
    def oblicz(self, dict):
        return True

    def __str__(self):
        return("True")



class F(Formula):
    def oblicz(self, zmienna):
        return False

    def __str__(self):
        return("False")



'''   def free(self):
        return {} nie potrzebny free bo i tak jest w formule, a to dziedziczy - tak samo w true'''

class And(Formula):
    

    def __init__(self, left, right):
        self.right = right
        self.left = left

    def oblicz(self, dict):
        x = self.right.oblicz(dict)
        y = self.left.oblicz(dict)
        return ( x and y)

    def __str__(self):
        return ("(%s & %s)"%(self.left, self.right)) 

    def free(self):
        x = self.left.free()
        y = self.right.free()
        return x.union(y)


class Or(Formula):
	
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def oblicz(self, dict):
        x = self.right.oblicz(dict)
        y = self.left.oblicz(dict)
        return (x or y)


    def __str__(self):
        return ("(%s v %s)"%(self.left, self.right)) 

    def free(self):
        x = self.left.free()
        y = self.right.free()
        return x.union(y)

class Impl(Formula):

    def __init__(self, left, right):
        self.right = right
        self.left = left


    def oblicz(self, dict):
        x = self.left.oblicz(dict)
        y = self.right.oblicz(dict)
        if x:
            return y
        else:
            return True


    def __str__(self):
        return ("(%s -> %s)"%(self.left, self.right)) 


    def free(self):
        x = self.left.free()
        y = self.right.free()
        return x.union(y)


class Impl_Impl(Formula):
	
    def __init__(self, left, right):
        self.right = right
        self.left = left


    def oblicz(self, dict):
        x = self.left.oblicz(dict)
        y = self.right.oblicz(dict)
        return(x == y)



    def __str__(self):
        return ("(%s <-> %s)"%(self.left, self.right)) 


    def free(self):
        x = self.left.free()
        y = self.right.free()
        return x.union(y)

class Not(Formula):

    def __init__(self, middle):
        self.middle = middle
    
    def oblicz(self, dict):
        x = self.middle.oblicz(dict)
        return(not x)

    def __str__(self):
        return ("~(%s)"%(self.middle)) 

    def free(self):
        x = self.middle.free()
        return x


class Zmienna(Formula):



    def __init__(self, middle):
        self.middle = middle

    def oblicz(self, dict):
         return(dict[self.middle])


    def __str__(self):
        return ("%s"%(self.middle))  

    def free(self):
        return {self.middle}






def poscibility(lista, acc):
    if len(lista)==0:
        yield acc
    else:
        for val in [True, False]:
            acc_ = acc.copy()
            acc_[lista[0]] = val
            yield from poscibility(lista[1:], acc_)

#yield to generator, jak listy leniwe - nie oblicza jak nie musi- acc na początku lista pusta robisz kopie acc, 
# bierzesz pierwszy elem w tej kopi zrób z niego prawdę, a potem dobierz do niego wszystkie elem na ogonie listy
#zweaca nam liste słowników, przez to się na początku wywalało true i false, bo myślalo, że dostało słownik, a tam miał być set 

def taut(form):
    lis = list(form.free())
    p = poscibility(lis, {})
    for i in p:
        if not form.oblicz(i):
            return("Nie jest to tautologia")
    return("Tautologia")
        
        



'''p = poscibility(["x","y","z"], {})
for i in p:
    print(i)'''




wyra = Impl(Zmienna("x"), And(Zmienna("y"), T()))


print(wyra.oblicz({"x":False, "y":True}))
print(wyra)
#print(wyra.free())
print(taut(wyra))



wyra1=Impl(And (F(), (Zmienna("y"))), T())

print(wyra1.oblicz({"y":True}))
print(wyra1)
print(taut(wyra1))