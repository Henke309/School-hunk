class Elev:
    def __init__(self, name, group, ssn):
        self.name = name
        self.group = group
        self.ssn = ssn

    def getInfo(self):
        text = "Namn: " + self.name + "\nKlass" + "\nPersonnummer: " + self.ssn

        return text


elever= []

elever.append = ("Adam Andersson", "TE17", "001122-6666")
elever.append = ("Berit Bengtsson", "TE18", "950101-1234")
elever.append = ("Ceasar Claesson", "Te17", "990101-1010")

change = input("Ange vem soom skall byta namn: ")
newName = input("Ange det nya namnet")


for elev in elever:
    if elev.name == change:
        elev.name == newName
        break
    
else:
    print("Hittade ingen elev med detta namn")

for elev in elever:
    print(elev.getInfo())




"""
print("== Från metoden getInfo() på eleven ==")
print(elev1.getInfo())

print("== Hämtar elevens namn via egenskapen name "")
print(elev1.name)
"""