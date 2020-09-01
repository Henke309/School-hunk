
"""
Name: Henrik Nguyen
Date: 19-11-05
Info:
<Insert information about file>
"""

import random


print("======================")
print("Nu kastast 2 tärningar")

while True:
    dice = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    if dice == dice2:
        print("Par ")
        print("")
        break

    else:
        print("Ej par")