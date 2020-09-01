"""
Name: Henrik Nguyen
Date: 01-10-2019
Info:
<Datastrukturer>
"""
'''
#uppgift 1 

tal = []

for i in range (5):
    t = int(input("Skriv in 5 tal: "))

    tal.append(t)

tal.sort()

print(tal[2])

summa = 0

for t in tal:
    summa += t

print(summa/5)
'''
'''
#uppgift 2

temp = []
while True:
    t = input("Tempen bror: ")
    

    if t.lower() == "avsluta":
        break
    else:
        temp.append(int(t))


print(sum(temp)/len(temp))
print (temp)
'''
