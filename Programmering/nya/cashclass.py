class Cashregister():
    def __init__(self):
        self.kvitto = [] 

    def add(self, price):
        self.kvitto.append(price)

    def getValue(self):
        return sum(self.kvitto)

    def getCount(self):
        return len(self.kvitto)

    def clear(self):
        self.kvitto.clear()



c1 = Cashregister()
c1.add(3.45)
c1.add(4)

print(c1.getValue())
print(c1.getCount())
c1.clear()
print(c1.getCount())