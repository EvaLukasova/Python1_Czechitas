""" Zadání
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:
První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
Tipy:
Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420". """
def chck_tlphn_nmbr(usr_nmbr):
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
# nmbr='+420564247094'
tst_ok=chck_tlphn_nmbr(nmbr)

if tst_ok:
    txt = input('Zadej text SMS: ')
    # txt='Do Česka přichází soutěž Future Enterprise Awards. Pomozte vybrat tuzemské premianty v inovacích a digitalizaci.'
    txt_prc=sms_prc(txt)
    print (f'Za zpravu na {nmbr} zaplatis {txt_prc} Kc.')
