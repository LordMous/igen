'''vegyeslista=['alma',400,'körte',650,500,'narancs']
szamok=[]
lista=[]
#for vegyeslista in range(1):
#    if vegyeslista[0] == str:
#        számok.append(vegyeslista[0])
for i in vegyeslista:
    if type(i) == str:
        lista.append(i)
    else:
        szamok.append(str(i))

print(lista,szamok)
f = open('vegyeslista.txt','w',encoding='utf-8')
g = open('ugymondszamok.txt','w',encoding='UTF-8')
u = open('ugymondszavak.txt','w',encoding='UTF-8')
for sor in vegyeslista:
    f.write(str(sor)+"\n")
print(vegyeslista)


for sor in vegyeslista:
    if type(sor == str):
        u.write(sor+'\n')
    else:
        g.write(str(g)+'\n')



for vegyeslista in range(6):
    liista=int(vegyeslista)
    if liista[0] >= 0:
        számok.append(vegyeslista[0])'''

#1feladat
import random
lista=[]
for x in range(20):
    y=random.randint(1,30)
    lista.append(y)
print(lista)


#2feladat
legkisebb=lista[0]
for sor in lista:
    if sor < legkisebb:
        legkisebb = sor
print(f'{legkisebb} a legkisebb szám')

#3feladat
legnagyobb=lista[0]
for sor in lista:
    if sor > legnagyobb:
        legnagyobb = sor
print(f'{legnagyobb} a legnagyobb szám')

#4feladat
kisebb=0
nagyobb=0
for sor in lista:
    if sor < 15:
        kisebb+=1
    else:
        nagyobb+=1
print(f'{kisebb}db kisebb szám van és {nagyobb}db nagyobb szám')

#5feladat
for sor in range(len(lista)):
    print(sor, lista[sor])


#6feladat
f=open('veletlen.txt','w',encoding='UTF-8')
for x in lista:
    y=str(x)
    f.write(y+'\n')
f.close()

#7feladat
atlag=0
for sor in lista:
    atlag+=sor
print(atlag/len(lista))