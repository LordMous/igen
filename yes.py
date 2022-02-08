
lista = ['Tudor','Vidor','Morgó','Szundi','Szende','Hapci','Kuka']
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista[2:])
törpe=input('Adj meg egy törpe nevet :')
if törpe in lista:
    print('Van benne')
else:
    print('Nincs benne')
lista.remove('Szende')
print(lista)
szereplők=['Hófehérke','Banya','Herceg']
mese=szereplők.copy()
print(mese)
mese.extend(lista)
print(mese)


def hossz_szerint(a):
    return len(a)
szinek=['piros','kék','sárga','piros','zöld','kék','fekete']
szinek.sort(key=hossz_szerint)
print(szinek)
szinek.sort(key=str.lower)
print(szi)


import random
lista=[]
összeg=0
for x in range(15):
    y=random.randint(1,50)
    lista.append(y)
    összeg+=y
print(lista)
print(összeg)
lista.sort(reverse=True)
print(lista)
print(lista[0])
print(lista[14])
