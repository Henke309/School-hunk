
from abc import ABCMeta, abstractmethod

class djurpensionat ():
    idcounter = 100

    def __init__(self, namn, ras, vikt):
        self.djur = []
        self.namn = namn
        self.setdjurid()
        self.ras = ras
        self.vikt = vikt

    @property
    def djurid(self):
        return self.__djurid

    def setdjurid (self):
        self.__djurid = djurpensionat.idcounter
        djurpensionat.idcounter += 1

    @propert
    def namn(self):
        return self.__namn.title()

    @setter
    def namn(self, value):
        self.__namn = value
        
    @property
    def vikt (self):
        return self.__vikt

    @setter 
    def vikt (self):
        if not self.vikt.isdigit():
            pass
        else:
            pass




    def adddjur(self, namn, id, ras, vikt):
        self.djur.append(namn, id, ras, vikt )

    @abstractmethod
    def info(self):
        return "Namn " + self.namn +\
            "\nId-nr: " + str(self.djurid) +\
                "\nRas: " + self.ras +\
                    "\nVikt: " + self.vikt

class personal ():
    pass

class vårdnadshavare ():
    pass

class guest ():
    pass