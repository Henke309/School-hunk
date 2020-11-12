
from abc import ABCMeta, abstractmethod

class djur ():
    idcounter = 100

    def __init__(self, namn, ras, vikt, hem):
        self.hem = hem
        self.namn = namn
        self.setdjurid()
        self.ras = ras
        self.vikt = vikt
        self.vaccinerad = "nej"

    @property
    def djurid(self):
        return self.__djurid

    def setdjurid (self):
        self.__djurid = djur.idcounter
        djur.idcounter += 1

    @property
    def namn(self):
        return self.__namn.title()

    @namn.setter
    def namn(self, value):
        self.__namn = value
        
    @property
    def vikt (self):
        return self.__vikt

    @vikt.setter 
    def vikt (self, value):
        if not value.isdigit():
            raise SyntaxError("Skriv med siffor mongo...")
        else:
            if not value.strip():
                raise SyntaxError("Ha inga mellanslag...")
            
            else:
                self.__vikt = value

    @property
    def ras (self):
        return self.__ras.title()

    @ras.setter
    def ras (self, value):
        self.__ras = value 

    @property
    def vaccinerad (self):
        return self.__vaccinerad.title()
    
    @vaccinerad.setter
    def vaccinerad (self, value):
        self.__vaccinerad = value

    @property
    def hem (self):
        return self.__hem.title()

    @hem.setter
    def hem (self,value):
        self.__hem = value


    def info(self):
        return "Namn " + self.namn +\
            "\nId-nr: " + str(self.djurid) +\
                "\nRas: " + self.ras +\
                    "\nVikt: " + self.vikt

class katt (djur):
    def __init__(self, namn, ras, vikt, hem):
        djur.__init__(self, namn, ras, vikt)
        self.kastrerad = "nej"

class hund (djur):
    def __init__(self, namn, ras, vikt, hem):
        djur.__init__(self, namn, ras, vikt)
        self.chippad = "nej"