zakupy = [0.2, 0.5, 4.59, 6]

def vat_faktura(lista):
    pay= 0
    for i in range(0, len(lista)):
        pay = pay + lista[i]
    pay = pay * 0.23
    print (pay)

vat_faktura(zakupy)

def vat_paragon(lista):
    pay= 0
    for i in range(0, len(lista)):
        pay = pay + (lista[i] * 0.23)

    print (pay)

vat_paragon(zakupy)

zakupy = [0.2, 0.5, 4.59, 6]
