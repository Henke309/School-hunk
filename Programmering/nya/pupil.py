class Pupil:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name (self):
        return self.__name.title()

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age (self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age should be above 0!")

p1 = Pupil("Hunke B", 33)
print(p1.name)
p1.name = "Hunke H"
print(p1.name)
try:
    p1.age = -17
except ValueError as e:
    print("an error occured:", str(e))