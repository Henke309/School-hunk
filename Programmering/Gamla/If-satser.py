'''
#uppgift 1
svar = input("Är det fint väder? ")


if svar.lower() == "ja":
    print ("Vi går på picknick! ")

elif svar.lower() == "nej":
    print ("Vi stannar inne och programmerar! ")

else: 
    print ("Jag förstår inte vad du menar boii... ")
'''
'''
#uppgift 2

'''
'''
#uppgift 3
x = int(input("Ey va ligger bensin priset per liter nuförtiden bror? "))

if 0 < x <= 9:  
    print ("Damn, det var billigt MANNEN!!! ")

elif 10 < x <= 15:
    print ("Tanka full tank ffs xD ")

elif 16 < x <= 19:
    print ("Tanka ba 10 liter bror ")

elif x > 20:
    print ("Nu säljer du bilen ffs!!! ")
'''
'''
#uppgift 4
tal = int(input("Skriv in ett tal: "))
if tal % 2 == 0:
    print ("Talet är jämnt")
else:
    print ("Talet är udda")
'''
'''
#uppgift 5
Karlskoga = int(input("Temp i Karlskoga BROR!! "))
Karlstad = int(input("Temp Karlstad BROR!! "))

Örebro = int(input("Temp Örebro BROR!! "))

if Karlskoga < Karlstad and Karlskoga < Örebro:
    print ("Det är kallast i Karlskoga")
elif Karlstad < Karlskoga and Karlstad < Örebro:
    print ("Det är kallast i Karlstad")
elif Örebro < Karlskoga and Örebro < Karlstad:
    print ("Det är kallast i Örebro")
else:
    print ("DET ÄR LIKA KALLT ÖVERALLT!!!")
'''
'''
#uppgift 6
from math import pi, degrees

svar = input("Vill du få reda på area, grader eller omkrets?: ")
if svar == "area":
    radie = int(input("Ange radien: "))
    print (radie * radie * pi)

if svar == "grader":
    radie = int(input("Ange radien: "))
    print (degrees(radie))

if svar == "omkrets"
    radie = int(input("Ange radien: "))
    print (2 * pi * radie)
'''
'''
#uppgift 7
svar = int(input("Ange ditt körkort resultat: "))

if 0 <= svar <= 53:
    print ("Du har blivit underkänd... ")

elif 54 <= svar <= 63:
    print ("Du har blivit godkänd! ")

elif 64 <= svar <= 65:
    print ("Du har blivit godkänd med god marginal!!! ")

else:
    print ("Ogiltig inmatning")
'''
'''
#uppgift 8
from math import sqrt
print ("andragradsekvations program")
p = int(input("Ange P: "))
q = int(input("Ange Q: "))

if (p/2)**2 - q < 0:
    print ("Det finns inga lösningar.")

elif (p/2)**2 - q == 0:
    print ("Det finns bara en lösning. ")
    svar = -p/2
    print (svar)

else:
    print ("Det finns 2 lösningar. ")
    svar = -p/2 + sqrt ((p/2)**2 -q)
    svar2 = -p/2 - sqrt ((p/2)**2 -q)
    print (svar)
    print (svar2)
'''