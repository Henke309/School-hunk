"""
Name: Henrik Nguyen
Date: --
Info:
<Insert information about file>
"""

from math import sqrt

p = int(input("Koefficienten p: "))
q = int(input("Koefficienten q: "))

if (p/2)**2 - q < 0:
    print ("Ekvationen saknar lösningar.")

elif (p/2)**2 - q == 0:
    svar = -p/2
    print ("Det finns en lösning.", svar)

else:
    svar = -p/2 + sqrt ((p/2)**2 - q)
    svar2 = -p/2 - sqrt ((p/2)**2 - q)
    print ("Det finns 2 lösningar. ", svar, "och ", svar2)