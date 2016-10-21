'''
Created on 14.1.2015

@author: Juha-Pekka Moilanen
'''

class osoite():
    '''
    Verkkolaskuosoiteluokka
    
    Yksi olio sisältää yhden yrityksen verkkolaskutiedot.
    
    n=numero, k=kirjain, (merkkejä) (näkyviin merkkejä / merkkejä)
    
    type(ytunnus) = str        nnnnnnn-n     (9)
    type(nimi) = str           kk..kk        (18 / +)
    type(valittaja) = str      kk...kk       (18 / +)
    type(ovt) = int            0037nn..nn    (12)
    type(ovt2) = int           nnnnn         (max 5)
    type(iban) = str           KKnnn..nn     (18)
    type(alkupvm) = date       nn.nn.nn      (8)
    type(erapvm) = date        nn.nn.nn      (8)
    
    '''


    def __init__(self, ytunnus, nimi, valittaja, \
                 ovt, ovt2, iban, alkupvm, erapvm):
        self.__ytunnus = ytunnus
        self.__nimi = nimi
        self.__valittaja = valittaja
        self.__ovt = ovt
        self.__ovt2 = ovt2
        self.__iban = iban
        self.__alkupvm = alkupvm
        self.__erapvm = erapvm
        
    def set_ytunnus(self, ytunnus):
        self.__ytunnus = ytunnus
    def set_nimi(self, nimi):
        self.__nimi = nimi
    def set_valittaja(self, valittaja):
        self.valittaja = valittaja
    def set_ovt(self, ovt):
        self.__ovt = ovt
    def set_ovt2(self, ovt2):
        self.__ovt2 = ovt2
    def set_iban(self, iban):
        self.__iban = iban
    def set_alkupvm(self, alkupvm):
        self.__alkupvm = alkupvm
    def set_erapvm(self, erapvm):
        self.__erapvm = erapvm
        
    def get_ytunnus(self):
        return self.__ytunnus
    def get_nimi(self):
        return self.__nimi
    def get_valittaja(self):
        return self.__valittaja
    def get_ovt(self):
        return self.__ovt
    def get_ovt2(self):
        return self.__ovt2
    def get_iban(self):
        return self.__iban
    def get_alkupvm(self):
        return self.__alkupvm
    def get_erapvm(self):
        return self.__erapvm
    
    def __str__(self):
        return self.__ytunnus+'\t'+self.__nimi+'\t'+self.__valittaja+'\t'+\
        self.__ovt+'\t'+self.__ovt2+'\t'+self.__iban+'\t'+\
        str(self.__alkupvm)+'\t'+str(self.__erapvm)
        '''
        return  'Y-tunnus: '+self.__ytunnus+'\t'+\
                'Yrityksen nimi: '+self.__nimi+'\t'+\
                'Maksuvälittäjä: '+self.__valittaja+'\t'+\
                'OVT-tunnus: '+self.__ovt+'\t'+\
                'OVT-lisätunnus: '+self.__ovt2+'\t'+\
                'IBAN: '+self.__iban+'\t'+\
                'Alkupvm: '+self.__alkupvm+'\t'+\
                'Loppupvm: '+self.__erapvm
        '''
        
    