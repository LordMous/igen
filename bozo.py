'''fajl=open('számok.txt','r')
for sor in fajl:
    print(sor.strip())
fajl.close()

with open('számok.txt') as f:
    for sor in f:
        print(sor.strip())



f = open('eletkor.txt','r')
for sor in f:
    szam=int(sor)
    if szam > 18:
        print(szam, 'Felnőtt')
    else:
        print(szam, 'Fiatal')

f.close()


f = open('nevek.txt','r')
for sor in f:
    print(sor.strip())


f.close()


f = open('nevek.txt',encoding='UTF-8')
    #for sor in f:
      #  print(sor.strip(),end=' ')

for sor in f:
    vissza=sor.strip()[::-1]
    print(vissza)

f.close()




f=open('nevek.txt',encoding='UTF-8')
uj=open('abetus.txt','w',encoding='UTF-8')
for sor in f:
    if sor[0]=='A':
        uj.write(sor)

f.close()'''


f=open('számok.txt',encoding='UTF-8')
uj=open('paros.txt','w',encoding='UTF-8')
for sor in f:
    szam=int(sor)
    if szam%2==0:
        uj.write(sor)

f.close()