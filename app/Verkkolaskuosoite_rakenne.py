'''
Perusopintojen harjoitustyö
Verkkolaskuosoitteisto

MCV-mallin mukainen 'Controller' -osa

Ohjelma käyttää sanakirja-rakennetta tiedontallentamiseen

Tiedot tallentaan tiedostoon verkkolaskusoitteet.dat
picklellä pakattuna

Osioissa määritellään ohjelman seuraavat tiedonhallinta toiminnot:
-Tiedostosta lukeminen
-Tiedostoon tallentaminen
-Olion tallentaminen sanakirjaan (Y-tunnuksen perusteella)
-Haetaan olio sanakirjasta (Y-tunnuksen perusteella)
-Poistetaan olio sanakirjasta (Y-tunnuksen perusteella)
-Tulostetaan sanakirjan 


Created on 5.2.2014

@author: Juha-Pekka Moilanen
'''

from Verkkolaskuosoite_GUI import *
import pickle
import operator
from datetime import *

TIEDOSTO = 'verkkolaskuosoitteet.dat'
VALITTAJAT = 'maksuvalittajat.dat'

def avaaOsoitteet():   
    '''
    Avataan osoitteet sisältävä sanakirja.
    
    Avaa sanakirjatietorakenteen ohjelman käyttöön 
    moduulissa määritetystä tiedostosta 
    tai luo tyhjän sanakirjan, jos edellistä ei löydy.
    
    :return: sanakirja osoitetiedoista.
    '''
    try:
        #luetaan sarjallistettu data tiedostosta muuttujaan "tiedosto"
        tiedosto = open(TIEDOSTO, 'rb')
        #puretaan sarjallistus ja tallennetaan tiedostossa oleva
        #sanakirja muuttujaan "osoitteet"
        osoitteet = pickle.load(tiedosto)
        #suljetaan tiedosto
        tiedosto.close()
        return osoitteet
    
    
    #jos verkkolaskurekisteri.dat-tiedostoa ei ole
    #luodaan uusi tyhjäsanakirja
    except IOError:
        return {}
    
def avaaValittajaLista():
    '''
    Avaataan maksuvälittäjät sisältävä lista.
    
    Avaa listatietorakenteen ohjelman käyttöön
    moduulissa määritetystä tiedostosta
    tai luo tyhjän listan, jos edellistä ei löydy.
    
    :return: lista maksuvälittäjistä.
    '''
    try:
        #luetaan sarjallistettu data tiedostosta muuttujaan "tiedosto"
        tiedosto = open(VALITTAJAT, 'rb')
        #puretaan sarjallistus ja tallennetaan tiedostossa oleva
        #lista muuttujaan "valittajat"
        valittajat = pickle.load(tiedosto)
        #suljetaan tiedosto
        tiedosto.close()
        return valittajat
    
    
    #jos maksuvalittajat.dat-tiedostoa ei ole
    #luodaan uusi tyhjä lista
    except IOError:
        return []
            
def tallennaOsoitteet(osoitteet):
    '''
    Tallennetaan verkkolaskuosoitteet tiedostoon.
    
    Tallentaa parametrinä välitettävän sanakirjan (osoitteet) 
    moduulissa määritettyyn tiedostoon.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return: totuusarvo onnistuiko tallennus vai ei. 
    '''
    try: 
        tiedosto = open(TIEDOSTO, 'wb')
        pickle.dump(osoitteet, tiedosto)
        tiedosto.close()
        return True
        
    except IOError:
        return False 
    
def tallennaValittajat(valittajat):
    '''
    Talletaan välittäjälista tiedostoon.
    
    Tallentaa parametrinä välitettävän sanakirjan 
    moduulissa määritettyyn tiedostoon.
    
    :param valittajat: maksuvälittäjät listassa.
    
    :return: totuusarvo onnistuiko tallennus vai ei. 
    '''
    try: 
        tiedosto = open(VALITTAJAT, 'wb')
        pickle.dump(valittajat, tiedosto)
        tiedosto.close()
        return True
        
    except IOError:
        return False
            
def lisaaOsoite(osoitteet, uusi_osoite):
    '''
    Lisätään osoite sanakirjaan.
    
    Lisää osoiteolion (uusi_osoite) sanakirjaan (osoitteet). 
    Sanakirjan avaimeksi määritetään osoiteolion sisältämä y-tunnus.
    uusi_osoite.get_ytunnus() = "uusi_osoite"-olion ytunnus merkkijono
    
    :param osoitteet: osoitteet sanakirjassa.
    :param uusi_osoite: lisättävä olio
    '''    

    osoitteet[uusi_osoite.get_ytunnus()] = uusi_osoite
    #sanakirja[avain.hae_ytunnus()] = lisattava olio
    
def lisaaValittaja(valittajat, uusi_valittaja):
    valittajat.append(uusi_valittaja)
    
def haeOsoite(osoitteet, ytunnus):
    '''
    Haetaan osoiteolio sanakirjasta.
    
    Etsii y-tunnuksen (ytunnus) perusteella 
    osoitetiedot sisältävän olion sanakirjasta (osoitteet) 
    ja palauttaa sen.
    
    :param osoitteet: osoitteet sanakirjassa.
    :param numero: ytunnus.
    
    :return osoite-olio, jossa etsityn yrityksen tiedot.
    '''
    if ytunnus in osoitteet:
        osoite = osoitteet[ytunnus]
    else:
        osoite = None
        
    return osoite

def valittajaListaStr(valittajalista):
    valittajatMerkkijono = ''
    valittajalista.sort()
    for alkio in valittajalista:
        valittajatMerkkijono += alkio + '\n'
    return valittajatMerkkijono

def haeOsoiteStr(osoite):
    '''
    Haetaan osoiteolio sanakirjasta muotoiltuna merkkijonona.
    
    Palauttaa yhden osoite-olion (osoite) tiedot
    ruudulle tulostamiseen sopivana merkkijonona (osoitetiedot).
    Pilkkoo tarvittaessa tietoalkiot sopivan pituisiksi
    ja lisää niiden väliin tyhjiä merkkejä, jotta allekaiset
    osoitetietojen alkiot asettuvat ruudulle sarakkeittain.
    
    :param osoite: osoite-olio.
    
    :return osoitetiedot: merkkijono, jossa osoite-olion tiedot muotoiltuna.
    
    '''
    osoite = osoite
    #print(osoite)
    osoitetiedot = ''
    
    '''ytunnus'''
    ytunnus = osoite.get_ytunnus()
    osoitetiedot += lisaaTyhjiaTekstiin(ytunnus, 9, 2) 
    
    '''nimi'''
    nimi = osoite.get_nimi()
    osoitetiedot += lisaaTyhjiaTekstiin(nimi, 18, 3)
        
    '''valittaja'''
    valittaja = osoite.get_valittaja()
    osoitetiedot += lisaaTyhjiaTekstiin(valittaja, 18, 3)
        
    '''ovt'''
    ovt = osoite.get_ovt()
    osoitetiedot += lisaaTyhjiaTekstiin(ovt, 13, 2)
        
    '''ovt2'''
    ovt2 = osoite.get_ovt2()
    osoitetiedot += lisaaTyhjiaTekstiin(ovt2, 5, 6)
        
    '''iban'''
    iban = osoite.get_iban()
    osoitetiedot += lisaaTyhjiaTekstiin(iban, 18, 3)
        
    '''voimassa'''
    alkupvm = dateToString(osoite.get_alkupvm())
    erapvm = dateToString(osoite.get_erapvm())
        
    alkupvm = lisaaTyhjiaTekstiin(alkupvm, 8, 0)
    erapvm = lisaaTyhjiaTekstiin(erapvm, 8, 0)
        
    voimassa = alkupvm + ' - ' + erapvm
        
    osoitetiedot += voimassa
        
            
    osoitetiedot +='\n' #lisää rivivaihto
    
    return osoitetiedot
        
def poistaOsoite(osoitteet, ytunnus): 
    '''
    Poistetaan osoite sanakirjasta ytunnuksen perusteella. 
    
    Poistaa y-tunnuksen (ytunnus) mukaisen osoitetieto-olion
    sanakirjasta (osoitteet).
    
    :param osoitteet: osoitteet sanakirjassa.
    :param ytunnus: poistettavan yrityksen Y-tunnus.
    
    :return: totuusarvo onnistuiko tallennus vai ei.
    '''
    if ytunnus in osoitteet: 
        del osoitteet[ytunnus]
        return True
    else:
        return False
    
def poistaValittaja(valittajat, poistettava): 
    '''
    Poistetaan valittaja listasta.
    
    Poistaa maksuvälittäjän (poistettava) listalta (valittajat).
    
    :param osoitteet: osoitteet sanakirjassa.
    :param ytunnus: poistettavan yrityksen Y-tunnus.
    
    :return: totuusarvo onnistuiko tallennus vai ei.
    '''
    if poistettava in valittajat: 
        valittajat.remove(poistettava)
        return True
    else:
        return False
    
def haeOsoitteet(osoitteet):
    '''
    Palauttaa kaikkien yritysten tiedot merkkijonona. 
    
    Luo merkkijonon joka sisältää kaikki sanakirjan (osoitteet)
    sisältämät osoitetiedot. Merkkijono on ruudulle tulostamiseen
    sopivaksi muotoiltu haeOsoiteStr-metodin avulla.
    Jokainen osoitetieto on omalla rivillään
    ja alkiot on aseteltu sarakkeittain.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return: merkkijono, jossa kaikkien yrityksen tiedot omilla riveillään. 
    '''
    osoitetiedot = '' #luodaan tyhjä str-muuttuja
    for avain in osoitteet: 
        '''
        käydään läpi kaikki sanakirjan oliot, haetaan olion tiedot,
        lisätään oikea määrä tyhjiä
        '''
        #haetaan sanakirjasta olio muuttujaan "osoite"
        osoite = osoitteet[avain]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def haeOsoitteetABC(osoitteet):
    '''
    Järjestetään osoitteet nimen mukaan aakkosjärjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen nimen perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono jossa kaikkien yrityksen tiedot omilla riveillään
            nimen mukaan aakkosjärjestyksessä
    
    Sanakirjaa ei voi lajitella suoraan, joten se muutetaan järjestetyksi
    listaksi. Listan alkiot ovat avain-arvo pareja tuple muodossa.
    
    Koodin selitys:
    Sanakirja järjestetyksi listaksi:
    tuodaan sanakirja (param osoitteet)
    sanakirjan lajittelemiseksi luodaan järjestetty lista sanakirjan arvoista.
    Listan alkiot ovat tupleja, jotka sisältävät parin:
    (sanakirjan avain, avainta vastaava arvo) eli tässä:
    (y-tunnus, osoiteolio).
    
    Merkkijonon luominen:
    osoitetiedot = ''
    for item in lista:
        osoite = item[1] #tuplen jälkimmäinen elemetti eli osoiteolio
        osoitetiedot += haeOsoiteStr(osoite) 
        #lisää tulostusmuokatun osoitetiedot merkkijonoon
    
    return osoitetiedot
    '''
    
    def getkey(tuplessaAvainJaOlio): #param: tuple (ytunnus, osoiteolio)
    #getkey-kutsussa ei näy välittävä argumentti, sorted()-komento luo sen
    #automaattisesti
        olio = tuplessaAvainJaOlio[1] #poimitaan tuplesta olio
        return olio.get_nimi() #palautetaan olion nimen haku käsky
    #luodaan järjestetty lista:
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    #lajitellutOsoitteetLista = järjestetty lista jossa tupleja
    #tuplessa: (ytunnus, osoiteolio)
    #HUOM: luotava tietorakenne muistuttaa siis sanakirjaa
    #osoitteet.items() = sanakirjan (osoitteet) arvot
    #key määrittää minkä mukaan sanakirjasta luotava lista järjestetään
    #tässä nimen mukaan, joten key:ksi asetaan getkey-metodilla olio.get_nimi()
    
    #luodaan osoitetiedoista merkkijono:
    osoitetiedot = ''
    #käydään luotu järjestetty lista läpi for-silmukassa
    for item in lajitellutOsoitteetLista:
        osoite = item[1] #item = tuple, item[1] = osoiteolio
        #lisätään merkkijonoon haeOsoiteStr-metodin muotoilema
        #yhden osoitetiedon sisältävä merkkijono
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def haeOsoitteetYTUNNUS(osoitteet):
    '''
    Järjestetään osoitteet Y-tunnuksen mukaan numerojärjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen Y-tunnuksen perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono, jossa kaikkien yrityksen tiedot omilla riveillään
            Y-tunnuksen mukaan järjestettynä.
    '''
    
    '''
    ks. koodin selitys metodista haeOsoitteetABC
    '''
    def getkey(tupleAvainOlio):
        olio = tupleAvainOlio[1]
        return olio.get_ytunnus()
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    osoitetiedot = ''
    for item in lajitellutOsoitteetLista:
        osoite = item[1]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def haeOsoitteetVALITTAJA(osoitteet):
    '''
    Järjestetään osoitteet maksuvälittäjän mukaan aakkosjärjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen maksuvälittäjän perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono jossa kaikkien yrityksen tiedot omilla riveillään
            maksuvälittäjän mukaan aakkosjärjestyksessä
    '''
    def getkey(tupleAvainOlio):
        olio = tupleAvainOlio[1]
        return olio.get_valittaja()
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    osoitetiedot = ''
    for item in lajitellutOsoitteetLista:
        osoite = item[1]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def haeOsoitteetOVT(osoitteet):
    '''
    Järjestetään osoitteet OVT-tunnuksen mukaan järjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen OVT-tunnuksen perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono jossa kaikkien yrityksen tiedot omilla riveillään
            OVT-tunnuksen mukaan järjestettynä
    '''
    def getkey(tupleAvainOlio):
        olio = tupleAvainOlio[1]
        return olio.get_ovt()
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    osoitetiedot = ''
    for item in lajitellutOsoitteetLista:
        osoite = item[1]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def haeOsoitteetIBAN(osoitteet):
    '''
    Järjestetään osoitteet IBAN-tilinumeron mukaan järjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen IBAN-tilinumeron perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono jossa kaikkien yrityksen tiedot omilla riveillään
            IBAN-tilinumeron mukaan järjestettynä
    '''
    def getkey(tupleAvainOlio):
        olio = tupleAvainOlio[1]
        return olio.get_iban()
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    osoitetiedot = ''
    for item in lajitellutOsoitteetLista:
        osoite = item[1]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot


def haeOsoitteetERAPVM(osoitteet):
    '''
    Järjestetään osoitteet voimassaolon päättymispäivän mukaan järjestykseen.
    
    Järjestetään sanakirjan (osoitteet) verkkolaskuosoitetiedot
    yrityksen voimassaolon päättymispäivän perusteella ja muodostetaan niistä ruudulle
    tulostettava merkkijono.
    :param osoitteet: osoitteet sanakirjassa
    
    :return merkkijono jossa kaikkien yrityksen tiedot omilla riveillään
            voimassaolon päättymispäivän mukaan järjestettynä
    '''
    def getkey(tupleAvainOlio):
        olio = tupleAvainOlio[1]
        return olio.get_erapvm()
    lajitellutOsoitteetLista = sorted(osoitteet.items(), key=getkey)
    osoitetiedot = ''
    for item in lajitellutOsoitteetLista:
        osoite = item[1]
        osoitetiedot += haeOsoiteStr(osoite)
    return osoitetiedot

def tarkistaMuotoilut(osoiteOlio):
    '''
    Tarkista käyttäjän syöttämien tietojen muoto
    
    Metodi tarkistaa ovatko osoiteolioksi koostetut käyttäjän syöttämät
    verkkolaskuosoitetiedot oikeassa muodossa.
    
    :param osoiteOlio: osoitetieto oliona
    
    :return boolean: True jos kaikki muotoilut ok
    '''
    ytunnus = osoiteOlio.get_ytunnus()
    nimi = osoiteOlio.get_nimi()
    valittaja = osoiteOlio.get_valittaja()
    ovt = osoiteOlio.get_ovt()
    ovt2 = osoiteOlio.get_ovt2()
    iban = osoiteOlio.get_iban()
    alkupvm = dateToString(osoiteOlio.get_alkupvm())
    erapvm = dateToString(osoiteOlio.get_erapvm())
    
    #muuttuja johon listataan virheet
    virheet = ''
    
    
    '''
    if-elif toistosilmukassa tutkitaan täyttävätkö syötteet muotoiluehdot.
    Jokainen if vastaa yhtä syötettä.
    '''
    
    #ytunnus
    if len(ytunnus) != 9 or\
        ytunnus[7] != '-' or\
        not ytunnus[:7].isdigit() or\
        not ytunnus[8].isdigit():
        virheet += 'Y-tunnus (1234567-9)\n'    
    #nimi, (ei tarkistusta)
    #valittaja, (ei tarkistusta)
    #ovt
    if len(ovt) != 12 or\
        ovt[:4] != '0037' or\
        not ovt.isdigit():
        virheet += 'OVT-tunnus (003712345679)\n'
    #ovt2
    if len(ovt2) > 5 or\
        not ovt2.isdigit():
        virheet += 'OVT-lisätunnus (12345)\n'
    #iban
    if len(iban) != 18 or\
        not iban[:2].isalpha() or\
        not iban[2:].isdigit():
        virheet += 'IBAN (2 kirjainta + 16 numeroa)\n'
    #alkupvm
    if len(alkupvm) != 8 or\
        not alkupvm[:2].isdigit() or\
        not alkupvm[2] == '.' or\
        not alkupvm[3:5].isdigit() or\
        not alkupvm[5] == '.' or\
        not alkupvm[6:].isdigit():
        virheet += 'Voimassa alk: (01.02.15)\n'
    #erapvm
    if len(erapvm) != 8 or\
        not alkupvm[:2].isdigit() or\
        not alkupvm[2] == '.' or\
        not alkupvm[3:5].isdigit() or\
        not alkupvm[5] == '.' or\
        not alkupvm[6:].isdigit():
        virheet += 'Voimassa asti: (01.02.15)\n'
    return virheet

def lisaaTyhjiaTekstiin(teksti, pituus, rako):
    '''
    Metodi muokkaa merkkijonoa sopivan pituiseksi ruudulle tulostettavaksi.
    
    Metodi katkaisee ruudulle mahtumattoman merkkijonon (teksti)
    sopivan pituiseksi (pituus). Lopuksi merkkijonon perään
    lisätään tyhjiä merkkejä kunnes sen pituus on 
    (pituus)+(rako).
    
    :param teksti: merkkijono, esim. ytunnus, nimi...
    :param pituus: merkkijonon suurin sallittu merkkimäärä, 
                    yli menevät jätetään pois palautettavasta merkkijonosta
    :param rako: merkkijonon perään lisättävien tyhjien merkkien määrä
    
    :return merkkijono, jonka pituus on säädetty sopivaksi
    '''
    #teksti on esim. ytunnus, nimi...
    #pituus on teksti max pituus
    #rako on haluttu tyhjien määrä perään
    stopvalue = int(pituus + 1)
    kokopituus = int(pituus + rako)
    
    if len(teksti) > pituus:
        teksti = teksti[:stopvalue]
    while len(teksti) < kokopituus:
        teksti+=' '
    return teksti

    '''pseudona pätkimis algoritmi'''
        
    '''
    def lisaaTyhjiaTekstiin  
        hae nimi str-muuttujaan oliosta
        jos nimi on pidempi kuin 9
            käytä nimestä vain 9 ensimmäistä
        kunnes nimi on 11 merkkiä pitkä
            lisää nimeen tyhjä merkki perään
    '''
    
def strToDate(pvmStr):
    '''
    Muuntaa merkkijonon päivämääräksi
    
    Metodi käyttää datetime-metodia joka muuttaa metodikutsussa
    määritellyn muotoisen merkkijonon (pvmStr) datetime-muotoon.
    Tässä muodoksi on määritelty "dd.mm.yy".
    
    :param pvmStr: dd.mm.yy muotoinen päivämäärän sisältävä merkkijono
    
    :return parametrinä annettu päivämäärä datetime-muodossa
    '''
    return datetime.strptime(pvmStr, '%d.%m.%y')

def dateToString(pvmDate):
    '''
    Muuntaa date-muuttujan merkkijonoksi.
    
    Metodi käyttää datetime-metodia joka muuttaa date-muotoisen
    päivämäärän (pvmDate) metodikutsussa määritellyn muotoiseksi
    merkkijonoksi.
    Tässä muodoksi on määritelty "dd.mm.yy".
    
    :param pvmDate: päivämäärä datetime-formaatissa
    
    :return dd.mm.yy muotoinen päivämäärän sisältävä merkkijono
    '''
    return (pvmDate.strftime("%d.%m.%y"))

