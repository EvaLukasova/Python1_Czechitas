""" Vyvíjíš software pro obcho
d s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem. """
# uživatelské vstupy: potávaný typ součástky, poptávaný počet kusů
# vstupy: skladové zásoby
# výstupy: informace o dosupnosti potávaného artiklu, aktualizace stavu zásob po prodeji
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky=input('Zadej kod soucastky:')
if kod_soucastky not in sklad:
    print ('Poptavana soucastka neni na sklade')
else:
    pocet_kusu=input('Zadej pocet kusu:')
    if not(type(int(pocet_kusu))==int):
        print('Pocet kusu musi byt nezaporné celé cislo.')
    else:
        if int(pocet_kusu)>int(sklad[kod_soucastky]):
            print('Poptavane mnozstvi neni na sklade.')
        if int(pocet_kusu)<int(sklad[kod_soucastky]):
            sklad[kod_soucastky]-=int(pocet_kusu)
            print(f'Skladove zasoby soucastky {kod_soucastky} snizeny na  {sklad[kod_soucastky]} kusu.')
        if int(pocet_kusu)==int(sklad[kod_soucastky]):
            sklad.pop(kod_soucastky)
            print(f'Skladove zasoby soucastky {kod_soucastky} snizeny na 0 kusu, soucastka vymazana.')
        