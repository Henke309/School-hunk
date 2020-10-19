from abc import ABCMeta, abstractmethod

class account():
    idcounter = 420
    interestrate = 1.01
    def __init__(self, namn, cash):
        self.konto = []
        self.namn = namn
        self.cash = cash
        self.setbankid()
    
    def setbankid(self):
        self.bankid = account.idcounter
        account.idcounter += 1

    def addkonto(self, namn, cash, bankid):
        self.konto.append(namn, cash, bankid) 

    @abstractmethod
    def info(self):
        return "namn: " + self.namn +\
            "\nPengar: " + self.cash +\
                "\nbankid: "+ str(self.bankid)

    def irate(self):
        self.irate = accrate
        accrate = account.deposit * interestrate




test1 = account("henke", "10921398kr")
test2 = account("david", "0.99kr")

print(test1.info())
print(test2.info())

    