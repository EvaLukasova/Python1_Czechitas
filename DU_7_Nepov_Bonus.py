""" Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.
Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return. """
class Auto:
    def __init__(self,registracni_znacka,typ_vozidla,najete_km, stav_tachometru):
        self.registracni_znacka=registracni_znacka 
        self.typ_vozidla=typ_vozidla
        self.najete_km=najete_km
        self.stav_tachometru=stav_tachometru
        self.dostupne=True
    def pujc_auto(self):
        if self.dostupne==True:
            self.dostupne=False
            print(f'Potvrzuji zapujceni vozidla')
        else:
            print(f'Vozidlo neni k dispozici')
    def get_info(self):
        print( f'{self.typ_vozidla} s registracni znackou {self.registracni_znacka} ma najeto {self.stav_tachometru} km')
    def vrat_auto(self,novy_stav_tachometru, pocet_dni):
        self.dostupne=True
        self.stav_tachometru=novy_stav_tachometru
        
        if pocet_dni<7: 
            cena=400*pocet_dni
        else:
            cena=300*pocet_dni
        return f'Poplatek za pujceni auta {self.registracni_znacka} cini {cena}'
 
peugeot=Auto('4A2 3020','Peugeot 403 Cabrio',47534, 12358)
skoda=Auto('1P3 4747','Škoda Octavia',	41253, 10515)

znacka=input('Pro zapůjčení zvolte značku Škoda nebo Peugeot: ')
if znacka=='Škoda':
    vuz=skoda 
elif znacka=='Peugeot':
    vuz=peugeot
try:
    vuz.get_info()
    vuz.pujc_auto()
except:
    print ('Tato znacka není v nabidce')

znacka=input('Znacka vraceneho auta: ')
najeto=input('Najete km: ')
pocet_dni=int(input('Pocet dni zapujcky: '))
if znacka=='Škoda':
    vuz=skoda 
elif znacka=='Peugeot':
    vuz=peugeot
else: 
    print ('Tato znacka není nase')
print(vuz.vrat_auto(najeto, pocet_dni))
 