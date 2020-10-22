class Tally:

    amountTally = 0

    def __init__(self):
        self.__value = 0
        Tally.amountTally += 1

    def count(self):
        self.__value += 1

    def getValue(self):
        return self.__value

    def reset(self):
        self.__value = 0


    @staticmethod
    def getTallys():
        return Tally.amountTally


print(Tally.amountTally)

t1 = Tally()
t2 = Tally()
t3 = Tally()
print(Tally.amountTally)