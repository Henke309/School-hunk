class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def toFahrenheit(self):
        return self.temperature * 1,8 + 32

    @property
    def temperature(self):
        return self.__temprature 

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("That cold man...")
        
        else:
            self.__temperature = value

c = Celsius

print(c.temperature)
print(c.toFahrenheit)