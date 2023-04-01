"""
Zadání:
Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.
Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz.
"""
jmeno='eva'
adresa=jmeno+'@czechitas.cz'
print(adresa)

"""
Nepovinný bonus:
Tuto část můžeš řešit, pokud už máš první část úkolu hotovou a chceš si ještě něco procvičit.

Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:

všechna písmena velká (vypíše např. JANA MALÁ)
všechna písmena malá (vypíše např. jana malá)
standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
iniciály (vypíše např. J. M.)
křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?).
"""
jmeno=input('Zadej jmeno:')
if jmeno.isalpha():
    prijmeni=input('Zadej prijmeni:')
    if prijmeni.isalpha():
        jmeno_prijmeni=jmeno+' '+prijmeni
        # všechna písmena velká (vypíše např. JANA MALÁ)
        print(jmeno_prijmeni.upper())
        # všechna písmena malá (vypíše např. jana malá)
        print(jmeno_prijmeni.lower())
        # standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
        print(jmeno[0].upper()+jmeno[1:].lower()+' '+prijmeni[0].upper()+prijmeni[1:].lower())
        # iniciály (vypíše např. J. M.)
        print(jmeno[0].upper()+'.'+prijmeni[0].upper()+'.')
        # křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
        if len(jmeno)>5:
            print(jmeno[0].upper()+'. '+prijmeni[0].upper()+prijmeni[1:].lower())
        else:
            print(jmeno[0].upper()+jmeno[1:].lower()+' '+prijmeni[0].upper()+prijmeni[1:].lower())
    else:
        print('Prijmeni obsahuje jine znaky nez pismena')
else: 
    print('Jmeno obsahuje jine znaky nez pismena')