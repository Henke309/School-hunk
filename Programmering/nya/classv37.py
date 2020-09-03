class Cashregister():
    def __init__(Self,name , price):
        self.name = name
        self.price = price 

    @property
    def name(self):
        return self.name.title()

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError ("nej")
    

