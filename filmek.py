filmek=open('filmek.txt','r',encoding='utf-8')
regi=open('regifilmek.txt','w',encoding='utf-8')
lista=[]

class Filmek():
    def __init__(self,nev,kor,perc):
        self.nev=nev
        self.kor=int(kor)
        self.perc=int(perc)
    def __repr__(self):
        return f'{self.nev}{self.kor}{self.perc}'

def abetus(self):
    if self.nev[0] == "A":
        return self.nev

for sor in filmek:
    sor=sor.strip().split(';')
    lista.append(sor)

for sor in lista:
    film=Filmek(sor[0],sor[1],sor[2])
    if film.kor < 2000:
        regi.write(str(sor)+'\n')
