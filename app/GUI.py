'''
Created on 11.2.2015

@author: juhamo
'''
'''
tuodaan tkinter moduulit
'''
from tkinter import *
import tkinter as tkinter
import tkinter.scrolledtext as tkst
import tkinter.messagebox

'''
tuodaan verkkolasku-olio ja ohjelman rakenne -moduulit
'''
from Verkkolaskuosoite_olio import *
from Verkkolaskuosoite_rakenne import *

'''
Verkkolaskuosoiterekisterihallintaohjelman
graafisen käyttöliittymän luokka
'''

class verkkoLaskuOsoiteGUI:



    def __init__(self, osoitteet):
        '''
        Ohjelman pääikkunan alustaja.
        
        Ohjelman pääikkuna sisältää seuraavat toiminnot:
        -Etsi osoite
        -Lisää osoite
        -Muokkaa osoite
        -Poista osoite
        -Lisätoiminnot
        
        -Tekstikentässä näytetään osoitetietoja sarakkeittain
            kukin osoite omalla rivillään.
        -Osoitetiedot voi järjestää ylärivin otsikkopainikkeista
            mm. nimen mukaan aakkosjärjestykseen.
            
        -Ohje-painike
        -Ohjelman lopetuspainike
        
        param: osoitteet, kaikki verkkolaskuosoitteet sanakirjassa
        '''
        #sanakirja muuttujaan
        self.osoitteet = osoitteet

        #luodaan pääikkuna
        self.ikkuna = tkinter.Tk()
        
        #luodaan master-frame
        self.master = tkinter.Frame()

        #Master-framen sisään 3 framea
        #ylärivi ja alaosa kahteen osaan
        self.toprow = tkinter.Frame(self.master)
        self.bottom = tkinter.Frame(self.master)
        self.left = tkinter.Frame(self.bottom)
        self.right = tkinter.Frame(self.bottom)

        #ks. framien sijoittelu lopusta
        
        #pääikkunan otsikko
        self.ikkuna.title("Verkkolaskuosoitteisto")

        '''Ylärivin komponentit:'''
        
        #käytetty Buttoneita yhteinäisen ulkoasun vuoksi
        
        
        '''OTSIKKO'''
        self.label_otsikko = tkinter.Button(self.toprow, \
                                            text = 'Verkkolaskuosoitteet  ', \
                                            #font = Arial, \
                                            relief = GROOVE, \
                                            ).grid(row=0, column=0, sticky=W)

        '''Y-TUNNUS'''
        self.label_ytunnus = tkinter.Button(self.toprow, \
                                           text = 'Y-tunnus', \
                                            width = 12, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            command = self.textWindowYTUNNUS
                                            ).grid(row=0, column=1)

        '''NIMI'''
        self.label_nimi = tkinter.Button(self.toprow, \
                                            text = 'Yrityksen nimi', \
                                            width = 22, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            command = self.textWindowNIMI
                                            ).grid(row=0, column=2)
        
        '''MAKSUVÄLITTÄJÄ'''
        self.label_valittaja = tkinter.Button(self.toprow, \
                                            text = 'Maksuvälittäjä', \
                                            width = 22, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            command = self.textWindowVALITTAJA, \
                                            ).grid(row=0, column=3)
        
        '''OVT-TUNNUS''' 
        self.label_ovt = tkinter.Button(self.toprow, \
                                            text = 'OVT-tunnus', \
                                            width = 16, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            #state = DISABLED, \
                                            command = self.textWindowOVT, \
                                            ).grid(row=0, column=4)

        '''OVT-LISÄTUNNUS'''        
        self.label_ovt2 = tkinter.Button(self.toprow, \
                                            text = 'OVT-lisätunnus', \
                                            width = 12, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            state = DISABLED, \
                                            ).grid(row=0, column=5)
        
        '''IBAN TILINUMERO'''
        self.label_iban = tkinter.Button(self.toprow, \
                                            text = 'IBAN', \
                                            width = 22, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            #state = DISABLED, \
                                            command = self.textWindowIBAN, \
                                            ).grid(row=0, column=6)
        
        '''VOIMASSAOLO'''
        self.label_erapvm = tkinter.Button(self.toprow, \
                                            text = 'Voimassaoloaika', \
                                            width = 20, \
                                            anchor = W, \
                                            relief = GROOVE, \
                                            #state = DISABLED, \
                                            command = self.textWindowErapvm, \
                                            ).grid(row=0, column=7, sticky=E)
        
        '''LEFT FRAME'''
        '''Vasemmanreunan komponentit'''

        '''
        PÄÄIKKUNAN
        
        Entry-kenttiin kirjoitettavat tekstit tallennetaan seuraaviin 
        StringVar-muuttujiin:
        '''
        
        self.etsiUserEntry = tkinter.StringVar()
        self.lisaaUserEntry = tkinter.StringVar()
        self.muokkaaUserEntry = tkinter.StringVar()
        self.poistaUserEntry = tkinter.StringVar()
        self.extraUserEntry = tkinter.StringVar()
        
            
        '''Etsi-toiminto'''
        
        self.label_etsi = tkinter.Label(self.left, \
                                            text = 'Etsi')                                    
        self.label_etsi.grid(row=0, column=0, sticky=NW)
        
        self.entry_etsi = tkinter.Entry(self.left, \
                                            text = self.etsiUserEntry, \
                                            foreground = 'Grey', \
                                            width = 15)
        self.entry_etsi.grid(row=1, column=0, sticky=NW)
        
        self.button_etsi = tkinter.Button(self.left, \
                                            command = self.etsiYksi, \
                                            text = '>', \
                                            width = 2)
        self.button_etsi.grid(row=1, column=1, sticky=NW)
                       
        self.etsiUserEntry.set('ytunnus') 
        #asettaa entry-ikkunan "oletusarvon"
        self.tyhjennaKlikatessa(self.entry_etsi, self.etsiUserEntry, 'ytunnus')
        #tyhjentää entryn klikatessa jos siinä lukee 'ytunnus'
        #ja asettaa tekstin väriksi mustan
        self.entry_etsi.bind("<Return>", self.etsiYksiEvent)
        #käynnistää etsi_buttonin toiminnon entryssä enteriä painettaessa
        

            
        '''Lisää-toiminto'''
        
        self.label_lisaa = tkinter.Label(self.left, \
                                            text = 'Lisää', \
                                            ).grid(row=2, column=0, sticky=W)
        self.entry_lisaa = tkinter.Entry(self.left, \
                                            text = self.lisaaUserEntry, \
                                            foreground = 'Grey', \
                                            width = 15)
        self.entry_lisaa.grid(row=3, column=0, sticky=W)
        
        self.button_lisaa = tkinter.Button(self.left, \
                                            text = '>', \
                                            width = 2, \
                                            command = self.lisaaRun, \
                                            ).grid(row=3, \
                                                   column=1, \
                                                   sticky=W)
                                            
        self.lisaaUserEntry.set('ytunnus') 
        #asettaa entry-ikkunan "oletusarvon"
        
        self.tyhjennaKlikatessa(self.entry_lisaa, self.lisaaUserEntry, 'ytunnus')
        #tyhjentää entryn klikatessa jos siinä lukee 'ytunnus'
        #ja asettaa tekstin väriksi mustan
        
        self.entry_lisaa.bind("<Return>", self.toplevelLisaaEvent)
        #käynnistää lisää_buttonin toiminnon entryssä enteriä painettaessa
        
        
        
        '''Muokkaa-toiminto'''
        
        self.label_muokkaa = tkinter.Label(self.left, \
                                            text = 'Muokkaa', \
                                           ).grid(row=4, \
                                                  column=0, \
                                                  sticky=W)
        self.entry_muokkaa = tkinter.Entry(self.left, \
                                            width = 15, \
                                            text = self.muokkaaUserEntry, \
                                            foreground = 'Grey')
        self.entry_muokkaa.grid(row=5, column=0, sticky=W)
        
        self.button_muokkaa = tkinter.Button(self.left, \
                                            command = self.muokkaaRun, \
                                            width = 2, \
                                            text = '>').grid(row=5, \
                                                             column=1, \
                                                             sticky=W)
                                            
        self.muokkaaUserEntry.set('ytunnus') 
        #asettaa entry-ikkunan "oletusarvon"
        self.tyhjennaKlikatessa(self.entry_muokkaa, self.muokkaaUserEntry, 'ytunnus')
        #tyhjentää entryn klikatessa jos siinä lukee 'ytunnus'
        #ja asettaa tekstin väriksi mustan
        self.entry_muokkaa.bind("<Return>", self.toplevelMuokkaaEvent)
                
        '''Poista-toiminto'''
        
        self.label_poista = tkinter.Label(self.left, \
                                            text = 'Poista', \
                                            ).grid(row=6, \
                                                   column=0, \
                                                   sticky=W)
        self.entry_poista = tkinter.Entry(self.left, \
                                            width = 15, \
                                            foreground = 'Grey', \
                                            text = self.poistaUserEntry)
        self.entry_poista.grid(row=7, column=0, sticky=W)
        self.button_poista = tkinter.Button(self.left, \
                                            command = self.poistaOsoiteButton, \
                                            width = 2, \
                                            text = '>').grid(row=7, \
                                                             column=1, \
                                                             sticky=W)
                                            
        self.poistaUserEntry.set('ytunnus') 
        #asettaa entry-ikkunan "oletusarvon"
        self.tyhjennaKlikatessa(self.entry_poista, self.poistaUserEntry, 'ytunnus')
        #tyhjentää entryn klikatessa jos siinä lukee 'ytunnus'
        #ja asettaa tekstin väriksi mustan
        self.entry_poista.bind("<Return>", self.poistaOsoiteButtonEvent)
                
        '''Lisätoiminnot'''
        
        self.label_extra = tkinter.Label(self.left, \
                                            text = 'Lisätoiminnot'
                                            ).grid(row=8, column=0, sticky=W)
        self.entry_extra = tkinter.Entry(self.left, \
                                            width = 15, \
                                            foreground = 'Grey', \
                                            text = self.extraUserEntry)
        self.entry_extra.grid(row=9, column=0, sticky=W)
        
        self.extraUserEntry.set('salasana') 
        #asettaa entry-ikkunan "oletusarvon"
        self.tyhjennaKlikatessa(self.entry_extra, self.extraUserEntry, 'salasana')
        #tyhjentää entryn klikatessa jos siinä lukee 'salasana'
        #ja asettaa tekstin väriksi mustan
        self.entry_extra.bind("<Return>", self.lisatoiminnotEvent)      
        
        self.button_extra = tkinter.Button(self.left, \
                                           command = self.lisatoiminnot, \
                                           width = 2, \
                                            text = '>').grid(row=9, \
                                                            column=1, \
                                                            sticky=W)

        '''Alaopainikkeet'''
        
        #tyhjiä välejä
        self.label_extra = tkinter.Label(self.left, \
                                            text = '\n\n', \
                                            ).grid(row=10, \
                                                   column=0, \
                                                   sticky=W, \
                                                   rowspan=3)
        #ohjelman lopetuspainike
        self.button_lopeta = tkinter.Button(self.left, \
                                            text = 'Lopeta', \
                                            command = self.lopetaOhjelma
                                            ).grid(row=14, \
                                                   padx=5, \
                                                   sticky=W)
        #ohjepainike
        self.button_ohje = tkinter.Button(self.left, \
                            text = 'Ohje', \
                            command = self.ohje)
        self.button_ohje.grid(row=14, column=0, sticky=E)
        #Oikean reunan komponentit
        
        #TEKSTIKENTTA
        
        "scrollbarin sisältävä tekstikenttäkomponetti"
        self.tekstiKentta = tkst.ScrolledText(self.right, \
                                  height = 20, \
                                  width = 120, \
                                  bd = 3, \
                                  )
        self.tekstiKentta.grid(row=0, column=0)

        '''Framien sijoittelu gridiin'''
        self.toprow.grid(row=0,column=0, sticky = W)
        self.bottom.grid(row=1,column=0)
        self.left.grid(row=0, column=0, sticky = N+W+S+E, padx=3)
        self.right.grid(row=0, column=1)
        self.master.grid()
       
        #päivitetään tekstikenttä ohjelman käynnistyessä
        self.textWindowNIMI()
        #ikkuna-loop käyntiin
        tkinter.mainloop()
        

        
        '''
        end of pääikkuna
        '''
    '''
    Entry-kenttien tyhjentäjä metodit
    
    Tyhjentävä ko. entry-kentän ja asettavat tekstin värin mustaksi.
    Näitä kutsutaan entryyn klikattaessa.

    Kehittämismahdollisuus:
    
    if self.lisaaUserEntry == 'ytunnus':
        delete
        aseta mustaksi
    else
        ei tyhjennetä (ei tehdä mitään)
        
        self.lisaaUserEntry = tkinter.StringVar()
        self.muokkaaUserEntry = tkinter.StringVar()
        self.poistaUserEntry = tkinter.StringVar()
        self.extraUserEntry = tkinter.StringVar()
    '''  
    
    def tyhjennaKlikatessa(self, entryWidget, entrynSisalto, oletusStr):
        '''
        Tyhjentää entryn sitä klikattaessa
        
        Jos entryssä on oletusarvo, esim. teksti 'ytunnus'
        metodi poimii hiiren klikkauksen ja kutsuu entrynTyhjennys-metodia
        välittäen sille tiedon mitä entryä (entryWidget) klikattiin.
        '''
        if entrynSisalto.get() == oletusStr:
            entryWidget.bind("<Button-1>", lambda widgetti, \
                             mitaKlikattiin=entryWidget: \
                             self.entrynTyhjennys(widgetti, mitaKlikattiin))

    def entrynTyhjennys(self, event, entryWidget):
        '''
        Tyhjennä entry.
        
        Tyhjentää entryn (entryWidget) ja asettaa sen tekstin värin mustaksi.
        Parametreissa event, koska kutsutaan bindilla.
        '''
        entryWidget.delete(0, END)
        entryWidget.config(foreground = 'Black')
        # jos kyseessä lisätoimintowidget niin muutetaan merkit tähdiksi
        if entryWidget == self.entry_extra:
            entryWidget.config(show = '*')
    
  

    '''
    Vasemman reunan toiminto painikkeiden metodit
    
    1. Etsi (etsiYksi)
    2. Lisää (toplevelLisaa)
    3. Muokkaa (toplevelMuokkaa)
    4. Poista (poistaOsoiteButton)
    5. Lopeta (lopetaOhjelma)
    '''
        
    '''1. Etsi-painike'''    

    def etsiYksi(self):
        '''
        Etsi-toiminto
        
        Hakee käyttäjän entry-kenttään syöttämän Y-tunnuksen mukaisen
        osoitetiedon sanakirjata. Muodostaa osoitetiedosta tulostettavan
        merkkijonon ja näyttää sen pääikkunan tekstikentässä yksistään.
        '''
        #entrystä muotoiluksi osoitetiedoksi
        self.haku = str(self.etsiUserEntry.get())
        #print(str(self.haku) + 'etsiYksi')
        self.haettuOsoiteOlio = haeOsoite(self.osoitteet, self.haku) 
        #haeOsoite(sanakirja, avain)
        #print(str(self.haettuOsoiteOlio) + 'etsiYksi')
        self.haettuOsoiteStr = haeOsoiteStr(self.haettuOsoiteOlio)
        ''' tulostaminen tekstikenttään '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, self.haettuOsoiteStr)
        #print('tulostettu 1')
 
    def etsiYksiEvent(self, event):
        '''
        Etsi-toiminto, enter-painikkeella
        
        Käynnistää etsi toiminnon, jos käyttäjä painaa enteriä buttonin
        klikkaamisen sijaan.
        '''
        self.etsiYksi()

    '''2. Lisää-painike'''
    def lisaaRun(self):
        '''
        Lisää ikkunan käynnistäjä
        
        Tarkistetaan ettei järjestelmässä ole jo olemassa
        verkkolaskuosoitetietoa annetulla y-tunnuksella.
        
        Käynnistää "Lisää osoite"-ikkunan tai
        ilmoittaa että Y-tunnuksella on jo tallennettu tieto
        järjestelmässä.
        '''
        if self.lisaaUserEntry.get() in self.osoitteet:
            "annetaan virheilmoitus"
            tkinter.messagebox.showwarning(parent = self.ikkuna, \
                                title='Virhe!', \
                                message='Y-tunnus on jo järjestelmässä')
        
        else:
            "käynnistetään ikkuna"
            self.toplevelLisaa()
        
    def toplevelLisaa(self):
        '''
        Lisää osoite -toiminto
        
        Luo popup-ikkunan jossa käyttäjä voi syöttää 
        verkkolaskuosoitetiedon järjestelmään.
        '''
        
        self.lisaa = Toplevel()
        self.lisaa.title("Lisää yrityksen tiedot")
        
        self.valittajaLista = avaaValittajaLista()
        
        '''
        LISAA TopLevel-ikkunan
        
        Entry-kenttiin kirjoitettavat tekstit tallennetaan seuraaviin 
        StringVar-muuttujiin:
        '''
        
        self.ytunnusLisaaUserEntry = tkinter.StringVar()
        self.nimiLisaaUserEntry = tkinter.StringVar()
        self.valittajaLisaaUserEntry = tkinter.StringVar()
        self.ovtLisaaUserEntry = tkinter.StringVar()
        self.ovt2LisaaUserEntry = tkinter.StringVar()
        self.ibanLisaaUserEntry = tkinter.StringVar()
        self.alkupvmLisaaUserEntry = tkinter.StringVar()
        self.loppupvmLisaaUserEntry = tkinter.StringVar()
        
        self.valittajaLisaaUserEntry.set('Maksuvälittäjä')
        
        '''Entry-kentät ja niiden Label tunnisteet'''
        
        lisaaLabelYtunnus = tkinter.Label(self.lisaa, \
                                        text = 'Y-tunnus', \
                                        anchor = W, \
                                        ).grid(row = 0, column = 0, sticky=W)
        lisaaEntryYtunnus = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.ytunnusLisaaUserEntry, \
                                        #valmisarvo = str(self.lisaaUserEntry)
                                        ).grid(row = 0, column = 1)
                                           
        self.ytunnusLisaaUserEntry.set(self.lisaaUserEntry.get())                                     
        
        lisaaLabelNimi = tkinter.Label(self.lisaa, \
                                        text = 'Nimi', \
                                        ).grid(row = 1, column = 0, sticky=W)
        lisaaEntryNimi = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.nimiLisaaUserEntry, \
                                        ).grid(row = 1, column = 1)

        lisaaLabelValittaja = tkinter.Label(self.lisaa, \
                                        text = 'Maksuvälittaja', \
                                        ).grid(row = 2, column = 0, sticky=W)
        lisaaEntryValittaja = OptionMenu(self.lisaa, \
                                         self.valittajaLisaaUserEntry, \
                                         *self.valittajaLista)
        lisaaEntryValittaja.config(width = 24, \
                                   bg="white", \
                                   relief = SUNKEN, \
                                   bd=1)
        '''
        lisaaEntryValittaja = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.valittajaLisaaUserEntry, \
                                        ).grid(row = 2, column = 1)
        '''
        lisaaEntryValittaja.grid(row = 2, column = 1)
        lisaaLabelOVT = tkinter.Label(self.lisaa, \
                                        text = 'OVT-tunnus', \
                                        ).grid(row = 3, column = 0, sticky=W)
        lisaaEntryOVT = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.ovtLisaaUserEntry, \
                                        ).grid(row = 3, column = 1)
        
        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.ovtLisaaUserEntry.set('0037' + self.lisaaUserEntry.get().replace('-', ''))                                
        
        lisaaLabelOVT2 = tkinter.Label(self.lisaa, \
                                        text = 'OVT-lisätunnus', \
                                        ).grid(row = 4, column = 0, sticky=W)
        lisaaEntryOVT2 = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.ovt2LisaaUserEntry, \
                                        ).grid(row = 4, column = 1)

        lisaaLabelIBAN = tkinter.Label(self.lisaa, \
                                        text = 'IBAN', \
                                        ).grid(row = 5, column = 0, sticky=W)
        lisaaEntryIBAN = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.ibanLisaaUserEntry, \
                                        ).grid(row = 5, column = 1)

        lisaaLabelAlkuPvm = tkinter.Label(self.lisaa, \
                                        text = 'Voimassa alk:', \
                                        ).grid(row = 6, column = 0, sticky=W)
        lisaaEntryAlkuPvm = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.alkupvmLisaaUserEntry, \
                                        ).grid(row = 6, column = 1)

        lisaaLabelLoppuPvm = tkinter.Label(self.lisaa, \
                                        text = 'Voimassa asti:', \
                                        ).grid(row = 7, column = 0, sticky=W)
        lisaaEntryLoppuPvm = tkinter.Entry(self.lisaa, \
                                        width = 30, \
                                        text = self.loppupvmLisaaUserEntry, \
                                        ).grid(row = 7, column = 1)

        '''Lopetuspainikkeet'''

        lisaaButtonPeruuta = tkinter.Button(self.lisaa, \
                                        text='Peruuta', \
                                        command=self.lisaa.destroy, \
                                        width = 15, \
                                        ).grid(row = 8, column = 0)
   
        lisaaButtonLopeta = tkinter.Button(self.lisaa, \
                                        text='Lopeta ja tallenna', \
                                        command=self.lopetaTallennaLisaa, \
                                        width = 25, \
                                        ).grid(row = 8, column = 1)

    def toplevelLisaaEvent(self, event):
        '''
        Lisää osoite -toiminto, enter-painikkeella
        
        Käynnistää Lisää osoite -toiminnon, jos käyttäjä painaa enteriä buttonin
        klikkaamisen sijaan.
        '''
        self.lisaaRun()
        
    '''3. Muokkaa-painike'''    
    def muokkaaRun(self):
        '''
        Muokkaa osoitetta -ikkunan käynnistäjä.
        
        Tarkistetaan että järjestelmässä löytyy
        verkkolaskuosoitetieto annetulla y-tunnuksella, jotta
        sitä voidaan muokata.
        
        Käynnistää "Muokkaa osoite"-ikkunan tai
        ilmoittaa että annetulla Y-tunnuksella ei löydy
        osoitetta.
        '''
        #tarkistetaan että annettu y-tunnus on olemassa
        if self.muokkaaUserEntry.get() not in self.osoitteet:
            "annetaan virheilmoitus"
            tkinter.messagebox.showwarning(parent = self.ikkuna, \
                                           title='Virhe!', \
                                       message='Y-tunnusta ei löydy')
        
        else:
            "käynnistetään ikkuna"
            self.toplevelMuokkaa()
                                                    
    def toplevelMuokkaa(self):
        '''
        Muokkaa osoitetta -toiminto
        
        Luo popup-ikkunan jossa käyttäjä voi muokata 
        järjestelmässä olevaa verkkolaskuosoitetietoa.
        '''
        self.muokkaa = Toplevel()
        self.muokkaa.title("Muokkaa yrityksen tietoja")
        
        '''
        MUOKKAA TopLevel-ikkunan
        
        Entry-kenttiin kirjoitettavat tekstit tallennetaan seuraaviin 
        StringVar-muuttujiin:
        '''
        
        self.valittajaLista = avaaValittajaLista()
        
        self.ytunnusMuokkaaUserEntry = tkinter.StringVar()
        self.nimiMuokkaaUserEntry = tkinter.StringVar()
        self.valittajaMuokkaaUserEntry = tkinter.StringVar()
        self.ovtMuokkaaUserEntry = tkinter.StringVar()
        self.ovt2MuokkaaUserEntry = tkinter.StringVar()
        self.ibanMuokkaaUserEntry = tkinter.StringVar()
        self.alkupvmMuokkaaUserEntry = tkinter.StringVar()
        self.loppupvmMuokkaaUserEntry = tkinter.StringVar()
            
        '''Entry-kentät ja niiden Label tunnisteet'''
        
        '''haetaan syötetun y-tunnuksen tiedot sisältävä olio'''
        
        self.muokattavaOsoite = haeOsoite(self.osoitteet, \
                                          self.muokkaaUserEntry.get())
        
        '''rivi1: Label YTUNNUS, entry'''
        
        muokkaaLabelYtunnus = tkinter.Label(self.muokkaa, \
                                        text = 'Y-tunnus', \
                                        anchor = W, \
                                        ).grid(row = 0, column = 0, sticky=W)
        muokkaaEntryYtunnus = tkinter.Entry(self.muokkaa, \
                                        width = 30, \
                                        text = self.ytunnusMuokkaaUserEntry, \
                                        ).grid(row = 0, column = 1)                               
        
        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''
        self.ytunnusMuokkaaUserEntry.set(self.muokattavaOsoite.get_ytunnus())
        
        '''rivi2: Label NIMI, entry'''
        
        muokkaaLabelNimi = tkinter.Label(self.muokkaa, \
                                        text = 'Nimi', \
                                        ).grid(row = 1, column = 0, sticky=W)
        muokkaaEntryNimi = tkinter.Entry(self.muokkaa, \
                                        width = 30, \
                                        text = self.nimiMuokkaaUserEntry, \
                                        ).grid(row = 1, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.nimiMuokkaaUserEntry.set(self.muokattavaOsoite.get_nimi())
        
        '''rivi3: Label Maksuvälittäjä, entry'''

        muokkaaLabelValittaja = tkinter.Label(self.muokkaa, \
                                            text = 'Maksuvälittaja', \
                                            ).grid(row = 2, column = 0, sticky=W)
        muokkaaEntryValittaja = OptionMenu(self.muokkaa, \
                                           self.valittajaMuokkaaUserEntry, \
                                           *self.valittajaLista)
        muokkaaEntryValittaja.config(width = 24, \
                                     bg="white", \
                                     relief = SUNKEN, \
                                     bd=1)
        muokkaaEntryValittaja.grid(row = 2, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.valittajaMuokkaaUserEntry.set(self.muokattavaOsoite.get_valittaja())
        
        '''rivi4: Label OVT-tunnus, entry'''
        
        muokkaaLabelOVT = tkinter.Label(self.muokkaa, \
                                            text = 'OVT-tunnus', \
                                            ).grid(row = 3, column = 0, sticky=W)
        muokkaaEntryOVT = tkinter.Entry(self.muokkaa, \
                                            width = 30, \
                                            text = self.ovtMuokkaaUserEntry, \
                                            ).grid(row = 3, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.ovtMuokkaaUserEntry.set(self.muokattavaOsoite.get_ovt())

        '''rivi5: Label OVT-lisatunnus, entry'''

        muokkaaLabelOVT2 = tkinter.Label(self.muokkaa, \
                                            text = 'OVT-lisätunnus', \
                                            ).grid(row = 4, column = 0, sticky=W)
        muokkaaEntryOVT2 = tkinter.Entry(self.muokkaa, \
                                            width = 30, \
                                            text = self.ovt2MuokkaaUserEntry, \
                                            ).grid(row = 4, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.ovt2MuokkaaUserEntry.set(self.muokattavaOsoite.get_ovt2())
        
        '''rivi6: Label IBAN, entry'''
    
        muokkaaLabelIBAN = tkinter.Label(self.muokkaa, \
                                    text = 'IBAN', \
                                    ).grid(row = 5, column = 0, sticky=W)
        muokkaaEntryIBAN = tkinter.Entry(self.muokkaa, \
                                    width = 30, \
                                    text = self.ibanMuokkaaUserEntry, \
                                    ).grid(row = 5, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.ibanMuokkaaUserEntry.set(self.muokattavaOsoite.get_iban())
        
        '''rivi7: Label Voimassa alk., entry'''
        
        muokkaaLabelAlkuPvm = tkinter.Label(self.muokkaa, \
                                    text = 'Voimassa alk:', \
                                    ).grid(row = 6, column = 0, sticky=W)
        muokkaaEntryAlkuPvm = tkinter.Entry(self.muokkaa, \
                                    width = 30, \
                                    text = self.alkupvmMuokkaaUserEntry, \
                                    ).grid(row = 6, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.alkupvmMuokkaaUserEntry.set(dateToString(\
                                      self.muokattavaOsoite.get_alkupvm()))
        
        '''rivi8: Label Voimassa asti:, entry'''
        
        muokkaaLabelLoppuPvm = tkinter.Label(self.muokkaa, \
                                    text = 'Voimassa asti:', \
                                    ).grid(row = 7, column = 0, sticky=W)
        muokkaaEntryLoppuPvm = tkinter.Entry(self.muokkaa, \
                                    width = 30, \
                                    text = self.loppupvmMuokkaaUserEntry, \
                                    ).grid(row = 7, column = 1)

        '''Haetaan entryyn valmiiksi syötetyn tunnuksen mukainen tieto'''                                            
        self.loppupvmMuokkaaUserEntry.set(dateToString(\
                                        self.muokattavaOsoite.get_erapvm()))
        
        '''Lopetuspainikkeet'''

        muokkaaButtonPeruuta = tkinter.Button(self.muokkaa, \
                                    text='Peruuta', \
                                    command=self.muokkaa.destroy, \
                                    width = 15, \
                                    ).grid(row = 8, column = 0)
   
        muokkaaButtonLopeta = tkinter.Button(self.muokkaa, \
                                    text='Lopeta ja tallenna', \
                                    command=self.lopetaTallennaMuokkaa, \
                                    width = 25, \
                                    ).grid(row = 8, column = 1)
                                            
        '''Toplevel muokkaa paattyy'''
    def toplevelMuokkaaEvent(self, event):
        '''
        Muokkaa osoitetta -toiminto, enter-painikkeella
        
        Käynnistää Muokkaa osoitetta -toiminnon, jos käyttäjä painaa enteriä buttonin
        klikkaamisen sijaan.
        '''
        self.muokkaaRun()
        
    '''4. Poista-painike'''
        
    def poistaOsoiteButton(self):
        '''
        Poista osoite -toiminto
        
        Varmistaa käyttäjältä popup-ikkunalla, että haluaako
        hän poistaa syöttämänsä Y-tunnuksen verkkolaskuosoitetiedon
        järjestelmästä.
        '''
        poistettavaOsoite = haeOsoite(self.osoitteet, \
                                      self.poistaUserEntry.get())
        poistettavanYtunnus = poistettavaOsoite.get_ytunnus()
        poistettavanNimi = poistettavaOsoite.get_nimi()
        
        varmistusVastaus = tkinter.messagebox.askquestion(\
                    parent = self.ikkuna, \
                    title='Vahvista poistaminen', \
                    message='Haluatko varmasti poistaa yrityksen tiedot?\n'\
                    +poistettavanYtunnus+'\n'\
                    +poistettavanNimi)
        if varmistusVastaus == 'yes':
            poistaOsoite(self.osoitteet, poistettavanYtunnus)
            self.textWindowNIMI()
            
    def poistaOsoiteButtonEvent(self, event):                
        self.poistaOsoiteButton()
        
    '''5. Lisätoiminnot-painike'''
    
    def lisatoiminnot(self):
        '''
        Lisätoiminto-ikkunan käynnistäjä
        
        Tarkastaa oliko käyttäjän syöttämä salasana oikea.
        Avaa lisätoiminto-ikkunan, jos oli oikein.
        Muutoin kertoo virheestä.
        '''
        #haetaan salasana entrystä
        salasana = self.extraUserEntry.get()
        #tarkastetaan salasana
        if salasana == 'yllapito':
            #kutsutaan metodiin kirjoitettua topleveliä
            self.toplevelExtra()
        #jos oli väärä sanasana niin kerrotaan siitä popupilla    
        else:  
            tkinter.messagebox.showwarning(parent = self.ikkuna, \
                                    title='Virhe!', \
                                    message='Väärä salasana\n(vihje: admin)')
            
    def lisatoiminnotEvent(self, event):
        '''
        Lisätoiminto-ikkunan käynnistäjä, enter-painikkeella
        
        Käynnistää Muokkaa osoitetta -toiminnon, jos käyttäjä painaa enteriä buttonin
        klikkaamisen sijaan.
        '''
        self.lisatoiminnot()
    
    def toplevelExtra(self):
        '''
        Lisätoiminnot-ikkuna
        
        Luo popup-ikkunan jossa ylläpitokäyttäjä voi hallita
        maksuvälittäjälistaa sekä tarvittaessa tyhjentää kaikki
        osoitetiedot järjestelmästä
        '''
        #luodaan toplevel
        self.extraTop = Toplevel()
        self.extraTop.title('Lisätoiminnot')
        
        self.ylaFrame = tkinter.Frame(self.extraTop)
        self.keskiFrame = tkinter.Frame(self.extraTop)
        self.alaFrame = tkinter.Frame(self.extraTop)
        
        '''tallennetaan entryt tekstimuuttujiin'''
        self.extraLisaa = tkinter.StringVar()
        self.extraPoista = tkinter.StringVar()
        
        self.valittajaLista = avaaValittajaLista()
        
        
        self.lisaaValittajaLabel = tkinter.Button(master = self.ylaFrame, \
                                    relief = GROOVE, \
                                    state = DISABLED, \
                                    text='Lisää välittäjä', \
                                    width = 15, \
                                    anchor=W)
        self.lisaaValittajaEntry = tkinter.Entry(master = self.ylaFrame, \
                                            text=self.extraLisaa, width = 25)
        self.lisaaValittajaButton = tkinter.Button(master = self.ylaFrame, \
                                            text='>', \
                                            width = 2, \
                                            command=self.lisaaValittajaButton)
        self.poistaValittajaLabel = tkinter.Button(master = self.ylaFrame, \
                                            relief = GROOVE, \
                                            state = DISABLED, \
                                            text='Poista välittäjä', \
                                            width = 15, \
                                            anchor=W)
        self.poistaValittajaEntry = tkinter.Entry(master = self.ylaFrame, \
                                            text=self.extraPoista, width = 25)
        self.poistaValittajaButton = tkinter.Button(master = self.ylaFrame, \
                                            text='>', \
                                            width = 2, \
                                            command=self.poistaValittajaButton)
        
        self.lisaaValittajaLabel.grid(row=0, column=0, sticky=W)
        self.lisaaValittajaEntry.grid(row=0, column=1, sticky=W)
        self.lisaaValittajaButton.grid(row=0, column=2, sticky=W)
        self.poistaValittajaLabel.grid(row=1, column=0, sticky=W)
        self.poistaValittajaEntry.grid(row=1, column=1, sticky=W)
        self.poistaValittajaButton.grid(row=1, column=2, sticky=W)
        
        self.extraTekstiKentta = tkst.ScrolledText(self.keskiFrame,
                                    relief = GROOVE, \
                                    pady = 5, \
                                    width = 33, height = 20, bd = 3)
        self.extraTekstiKentta.grid(row=2)
        
        self.textValittajat()
        
        self.extraTyhja1 = tkinter.Label(text = '').grid(row=3)
        
        self.extraPoistaKaikki = tkinter.Button(self.keskiFrame, \
                                    text='Poista kaikki OSOITTEET', \
                                    width=42, \
                                    command = self.poistaKaikkiOsoitteet, \
                                    ).grid(row=4)
        
        self.extraTyhja2 = tkinter.Label(text = '').grid(row=5)
        
        self.extraPeruuta = tkinter.Button(master = self.alaFrame, \
                                    text='Peruuta', \
                                    width = 20, \
                                    command=self.peruutaExtraButton)
        self.extraTallenna = tkinter.Button(master = self.alaFrame, \
                                    text='Lopeta', \
                                    width = 20, \
                                    command=self.lopetaExtraButton)
        
        self.extraPeruuta.grid(row=6, column=0, sticky=W)
        self.extraTallenna.grid(row=6, column=1, sticky=W)
      
        self.ylaFrame.grid()
        self.keskiFrame.grid()
        self.alaFrame.grid()
        
    def lisaaValittajaButton(self):
        '''
        Lisää maksuvälittäjä-button
        
        Hakee ylläpitokäyttäjän entryyn kirjoittaman maksuvälittäjän
        ja lisää sen järjestelmään, jonka jälkeen se on valittavissa
        verkkolaskuosoitetta lisättäessä.
        '''
        lisaaValittaja(self.valittajaLista, self.extraLisaa.get())
        self.textValittajat()
        
    def poistaValittajaButton(self):
        '''
        Poista maksuvälittäjä-button
        
        Poistaa ylläpitokäyttäjän syöttämän maksuvälittäjän
        järjestelmästä.
        '''
        poistaValittaja(self.valittajaLista, self.extraPoista.get())
        self.textValittajat()
        
    def textValittajat(self):
        '''
        Maksuvälittäjät näyttävän tekstikentän päivitys
        
        Tyhjentää tekstikentän, jossa maksuvälittäjä lista näkyy
        ja päivittää siihen nykyisen listan.
        '''
        self.extraTekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.extraTekstiKentta.insert(tkinter.INSERT, \
                                      valittajaListaStr(self.valittajaLista))

    def peruutaExtraButton(self):
        '''
        Peruuta-button, lisätoiminnot
        
        Sulkee lisätoimintoikkunan talletamatta muutoksia
        '''
        return self.extraTop.destroy()
                           
    def lopetaExtraButton(self):
        '''
        Lopeta-button, lisätoiminnot
        
        Sulkee lisätoimintoikkunan ja tallentaa maksuvälittäjälistan
        järjestelmään.
        '''
        tallennaValittajat(self.valittajaLista)
        return self.extraTop.destroy()
                                       
    def poistaKaikkiOsoitteet(self):
        '''
        Poista kaikki osoitteet -toiminto
        
        Tyhjentää kaikki verkkolaskuosoitetiedot järjestelmästä.
        '''
        vastaus = tkinter.messagebox.askquestion(parent = self.extraTop, \
                                title='Vahvista poistaminen', \
                                message='Haluatko varmasti poistaa\n' + \
                                'KAIKKI osoitetiedot järjestelmästä?')
        if vastaus == 'yes':
            self.osoitteet = {}
        print('kaikki poistettu')
                                      
    '''6. Lopeta-painike'''
    
    def lopetaOhjelma(self):
        '''
        Ohjelman käytön lopetuspainike
        
        Tallentaa sanakirjatietorakenteen ja sulkee ohjelman.
        '''
        tallennaOsoitteet(self.osoitteet)
        self.ikkuna.destroy()
    
    def ohje(self):
        '''
        Ohje-ikkuna
       
        Ohje ikkunan joka käynnistyy, kun käyttäjä klikkaa pääikkunan ohjepainiketta
        '''
        tkinter.messagebox.showinfo(parent = self.ikkuna, \
                            title='Ohje!', \
                            message='Ohjeet:\n' \
                            'www.verkkolaskuosoitteistoohje.com')
    
    '''
    GUI metodit
    
    Toplevel-ikkunoiden painikkeet:
    -Lisää-toplevelin lopetuspainike (lopetaTallennaLisaa)
    -Muokkaa-toplevelin lopetuspainike (lopetaTallennaMuokkaa)
    
    Tekstinkentän päivitys metodit:
    -Nimen mukaan aakkosellinen (textWindowNIMI)
    -Y-tunnuksen mukaan nouseva (textWindowYTUNNUS)
    -Maksuvälittäjän mukaan aakkosellinen (textWindowVALITTAJA)
    '''                                                                                    

    '''Lisää-toplevelin lopetuspainike'''    
    
    def lopetaTallennaLisaa(self):
        '''
        Lisää toiminnon lopetuspainike
        
        Tarkistaa, että käyttäjän syöttämät tiedot ovat oikeassa muodossa.
        Lisää käyttäjän syöttämän verkkolaskuosoitteen järjestelmään.
        '''
        #luodaan olio käyttäjän syöttämistä tiedoista
        uusi_osoite_olio = osoite(self.ytunnusLisaaUserEntry.get(), \
                            self.nimiLisaaUserEntry.get(), \
                            self.valittajaLisaaUserEntry.get(), \
                            self.ovtLisaaUserEntry.get(), \
                            self.ovt2LisaaUserEntry.get(), \
                            self.ibanLisaaUserEntry.get(), \
                            strToDate(self.alkupvmLisaaUserEntry.get()), \
                            strToDate(self.loppupvmLisaaUserEntry.get()))
        
        #tarkistetaan käyttäjän antamien tietojen muotoilut
        virheetMuotoilussa = tarkistaMuotoilut(uusi_osoite_olio)
        
        #jos tarkistus menee läpi, tallennetaan syötetyt tiedot
        if virheetMuotoilussa == '':   
            lisaaOsoite(self.osoitteet, uusi_osoite_olio)
            #päivitetään tekstikenttä
            self.textWindowNIMI()
            #palautetaan ikkunan sulkemiskomento
            self.lisaa.destroy()
        
        #jos tarkistus ei mene läpi niin annetaan virheilmoitus popup-ikkunassa
        else:
            tkinter.messagebox.showwarning(parent = self.lisaa, \
                    title='Virhe!', \
                    message='Seuraavat tiedot eivät ole oikeassa muodossa: \n'\
                    + virheetMuotoilussa)
    
    def lopetaTallennaMuokkaa(self):
        '''
        Muokkaa osoitetta -toiminnon lopetuspainike
        
        '''
        #luodaan olio
        muokattu_osoite_olio = osoite(self.ytunnusMuokkaaUserEntry.get(), \
                            self.nimiMuokkaaUserEntry.get(), \
                            self.valittajaMuokkaaUserEntry.get(), \
                            self.ovtMuokkaaUserEntry.get(), \
                            self.ovt2MuokkaaUserEntry.get(), \
                            self.ibanMuokkaaUserEntry.get(), \
                            strToDate(self.alkupvmMuokkaaUserEntry.get()), \
                            strToDate(self.loppupvmMuokkaaUserEntry.get()))
        
        #tarkistetaan käyttäjän antamien tietojen muotoilut
        virheetMuotoilussa = tarkistaMuotoilut(muokattu_osoite_olio)
        
        #jos tarkistus menee läpi, tallennetaan syötetyt tiedot
        if virheetMuotoilussa == '':   
            lisaaOsoite(self.osoitteet, muokattu_osoite_olio)
            #päivitetään tekstikenttä
            self.textWindowNIMI()
            #palautetaan ikkunan sulkemiskomento
            self.muokkaa.destroy()
        
        #jos tarkistus ei mene läpi niin annetaan virheilmoitus popup-ikkunassa
        else:
            tkinter.messagebox.showwarning(parent = self.muokkaa, \
                    title='Virhe!', \
                    message='Seuraavat tiedot eivät ole oikeassa muodossa: \n'\
                    + virheetMuotoilussa)
    
    '''
    turhia metodeja?
    def lisaaValittaja(self):
        
        lisaaValittaja(self.valittajaLista, self.extraLisaa.get())
        #tallenna
        
    def poistaValittaja(self):
        poistaValittaja(self.valittajaLista, self.extraPoista.get())
        #tallenna 
    '''
            
    '''
    Tekstikentän päivitys metodit
    '''
    
    '''
    turha metodi?
    def textWindowNoOrder(self):
    '''
    
    #Päivitä tekstikenttä
    '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteet(self.osoitteet))
        print('päivitetty')
    '''
    def textWindowNIMI(self):
        '''
        Tekstikentän päivitys nimen mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        nimen mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetABC(self.osoitteet))
        
    def textWindowYTUNNUS(self):
        '''
        Tekstikentän päivitys Y-tunnuksen mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        Y-tunnuksen mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetYTUNNUS(self.osoitteet))

    def textWindowVALITTAJA(self):
        '''
        Tekstikentän päivitys maksuvälittäjän mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        maksuvälittäjän mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetVALITTAJA(self.osoitteet))

    def textWindowOVT(self):
        '''
        Tekstikentän päivitys OVT-tunnuksen mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        OVT-tunnuksen mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetOVT(self.osoitteet))
 
    def textWindowIBAN(self):
        '''
        Tekstikentän päivitys IBAN-tilinumeron mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        IBAN-tilinumeron mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetIBAN(self.osoitteet))    
  
    def textWindowErapvm(self):
        '''
        Tekstikentän päivitys viimeisen voimassaolopäivän mukaan
        
        Tyhjentää pääikkunan tekstikentän ja päivittää siihen
        viimeisen voimassaolopäivän mukaan järjestetyt verkkolaskuosoitetiedot
        '''
        self.tekstiKentta.delete("1.0", END) 
        #index=("line.column", tekstin loppu) eli koko teksti
        self.tekstiKentta.insert(tkinter.INSERT, \
                                 haeOsoitteetERAPVM(self.osoitteet))

def main():
    
    osoitteet = avaaOsoitteet() #luodaan tai avataan sanakirja

    verkkoLaskuOsoiteGUI(osoitteet) #käynnistetään verkkoLaskuGUI (välitettään sanakirja)
    #poistin tästä muuttuja = 
if __name__ == '__main__':
    main()