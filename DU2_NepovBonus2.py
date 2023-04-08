""" Ve slovníku zde najdeš seznam slovníků s informacemi o státech světa. O každém státu tam vidíš následující informace:

název státu (name),
hlavní město (capital),
region (region),
subregion (subregion),
populace (population),
rozloha (area),
Giniho koeficient (gini).
Vytvoř program, který se uživatele zeptá na region, který ho zajímá. Následně projdi seznam a vypiš všechny státy, které leží v regionu. Pokud program žádný stát pro daný region nenajde, vypiš text "Neznámý region". """
# vstup: seznam zemi, omezila jsem delku
# uzivatelsky vstup: volba regionu
# vystup: nabidne nejdriv seznam regionu, pak po uzivatelske voble seznam zemi v regionu, neexistuje-li, defaultni hlaska
staty = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "region": "Asia",
        "subregion": "Southern Asia",
        "population": 27657145,
        "area": 652230.0,
        "gini": 27.8,
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "region": "Europe",
        "subregion": "Northern Europe",
        "population": 28875,
        "area": 1580.0,
    }
]
regiony=''
for zeme in staty:
    if zeme['region'] not in regiony:
        regiony=regiony+zeme['region']+', '
regiony=regiony[:-2]
print(f'Muzes vybirat z techto regionu: {regiony}')
oblast=input('Zadej region:')
vypis_zemi=''
for zeme in staty:
    if zeme['region']==oblast:
        vypis_zemi=vypis_zemi+zeme['name']+', '
vypis_zemi=vypis_zemi[:-2]
if vypis_zemi=='':
    print('V zadanem regionu nejsou zadne zeme')
else:
    print(f'V zadanem regionu jsou nasledujici zeme: {vypis_zemi}')