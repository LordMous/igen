'''
class Diak():
    def __init__(self,vnev, knev, pont):
        self.pont = pont
        self.knev = knev
        self.vnev = vnev
    def __repr__(self):
        return f'{self.knev} {self.vnev} {self.pont}'
    def vizsgal(self):
        if self.pont>20:
            return 'átment'
        else:
            return 'megbukott'

diak2=Diak('Nagy','Anna',11)
diak1=Diak('Kiss','Lajos', 34)

print(diak1, diak1.vizsgal())
print(diak2, diak2.vizsgal())
'''

#sajat tipus marka def ha 2000 alatt akkor veteran
class Auto():
    def __init__(self,tipus,marka,evjarat):
        self.tipus = tipus
        self.marka = marka
        self.evjarat = evjarat
    def __repr__(self):
        return f'{self.tipus} {self.marka} {self.evjarat}'
    def oreg(self):
        if self.evjarat<1993:
            return 'veterán'
        else:
            return 'fiatal'
auto1=Auto('Opel','Corsa',1999)
auto2=Auto('Trabant','601',1983)
print(auto1,auto1.oreg())
print(auto2,auto2.oreg())
