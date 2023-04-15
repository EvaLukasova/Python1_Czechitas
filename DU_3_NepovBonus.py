""" Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně
Výsledný slovník ulož jako JSON do souboru znamky.json """
import json

with open('body.json', encoding='utf-8') as file:
    pisemky = json.load(file)

with open('bonusy.json', encoding='utf-8') as file:
    bonus_body = json.load(file)

znamky={}
for student, body in pisemky.items():
    if student in bonus_body.keys():
        body_celkem=pisemky[student]+bonus_body[student]
    else:
        body_celkem=pisemky[student]
    if body_celkem>=90:
        znamka=1
    elif body_celkem>=70:
        znamka=2
    elif body_celkem>=50:
        znamka=3
    elif body_celkem>=30:
        znamka=4
    else:
        znamka=5
    znamky.update({student:znamka})
    
with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump (znamky, file)
    
        
