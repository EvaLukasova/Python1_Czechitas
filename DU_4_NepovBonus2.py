""" Přidej svým funkcím typování, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.
K typování se dostaneme až v 5. lekci. Pokud chceš, můžeš úlohu řešit předem pomocí Čtení na doma """
def chck_tlphn_nmbr(usr_nmbr: str) -> bool:
    usr_nmbr=usr_nmbr.replace(' ','')
    try: 
        int(usr_nmbr)
        tst_ok=len(usr_nmbr)==9 or (len(usr_nmbr)==13 and usr_nmbr[0:4]=='+420')        
    except:
        tst_ok=False
    return tst_ok

def sms_prc(sms:str)-> float:
    cena=3
    if len(txt)%180==0:
        delka=len(txt)/180
    else:
        delka=(len(txt)-len(txt)%180)/180+1
    prc=delka*cena
    return prc


nmbr = input('Zadej telefonni cislo: ')
# nmbr='+420 564 247 094'
tst_ok=chck_tlphn_nmbr(nmbr)

if tst_ok:
    txt = input('Zadej text SMS: ')
    # txt='Do Česka přichází soutěž Future Enterprise Awards. Pomozte vybrat tuzemské premianty v inovacích a digitalizaci.'
    txt_prc=sms_prc(txt)
    print (f'Za zpravu na {nmbr} zaplatis {txt_prc} Kc.')