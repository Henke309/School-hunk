"""
Name: Henrik Nguyen
Date: 2019-11-12
Info:
<Insert information about file>
"""

tal = []

while True:
    try:
        talet = int(input("Talet: "))
    except:
        print("Felaktig inmatning")
    else:
        if talet == 0:
            break
        else:
            tal.append(talet)

for t in tal:
    print(t)