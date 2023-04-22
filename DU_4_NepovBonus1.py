""" Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".
Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace """
def chck_tlphn_nmbr(usr_nmbr):
    usr_nmbr=usr_nmbr.replace(' ','')
    try: 
        int(usr_nmbr)
        tst_ok=len(usr_nmbr)==9 or (len(usr_nmbr)==13 and usr_nmbr[0:4]=='+420')        
    except:
        tst_ok=False
    return tst_ok

def sms_prc(sms):
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