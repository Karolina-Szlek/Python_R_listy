import itertools



def to_number(st,d):#bierze słownik i słowo - zwraca liczbę ze słowa
    return "".join([d[s] for s in st.lower()])


def kryptorytm(a,b,c):
    letters = set()
    for letter in (a+b+c).lower():
        letters.add(letter)
    letters = list(letters)
    perms = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
    #print (perms)
    for perm in perms:
        d = {a:i for a,i in zip(letters,perm)}#robi słownik dla każdej premutacji
        if eval(f"{int(to_number(a,d))} + {int(to_number(b,d))} == {int(to_number(c,d))}"):#jeżeli dla słownika działa, zwróć słownik
            return d

a,b,c = "KIOTO","OSAKA","TOKIO"
ans = kryptorytm(a,b,c)
na,nb,nc = to_number(a,ans),to_number(b,ans),to_number(c,ans)
print("Solution: ",end="")
print("\n")
for char,n in ans.items():#items dla słowników 
    print(f"{char} = {n}, ")
   # print("\n")
print("\n")
print("  KIOTO")
print("+ OSAKA")
print("--------")
print("  TOKIO")


print("\n")
print(" ",na)
print("+",nb)
print("--------")
print(" ",int(na)+int(nb))
print(nc)