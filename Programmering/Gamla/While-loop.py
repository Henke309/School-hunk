'''
namn = input("Ange ett namn: ")

while namn.lower() != "avsluta":
    print("Coolt namn bror, namnet innehåller", len(namn), "antal tecken!")

    namn = input("Ange ett namn: ")
else:
    print("Du har valt att avsluta programmet! REEEEEEEEE!!!!")
'''
'''
namn = "Henrik"
print("Jag heter", namn)
print("Jag heter " + namn)
print("Jag heter {n}. Jag är {a} år gammal".format(n=namn, a=17) )
'''
'''
#uppgift 1a
i = 1
while i < 16:
    print (i)
    i += 1
'''
'''
#uppgift 1b
i = 20
while i < 31:
    print (i)
    i += 1
'''
'''
#uppgift 1c
i = 10
while i > -11:
    print (i)
    i -= 1
'''
'''
#uppgift 2a
i = 1
sum = 0
while i < 51:
   sum = sum + i 
   i += 1
   print(sum)
'''
'''
#uppgift 2b
n = int(input("skriv in ett tal: "))
i = 1
sum = 0
while i < n:
   sum = sum + i 
   i += 1
   print(sum, end=" ")
'''
'''
#uppgift 3 a
i = 1
tal = int(input("Skriv in ett tal mellan 1-10: "))
sum = 0
while i < 11:
    
    sum = tal * i
    print (sum, end=" ")
    i+= 1
'''
'''
#uppgift 3 b
i = 1 
tal = int(input("Skriv in ett tal mellan 1-10: "))
multi = int(input("Hur mycket ska den gångra sig själv? "))
sum = 0
while i < multi:

    sum = tal * i
    print (sum, end=" ")
    i+= 1
'''
'''
#uppgift 3c

tal = int(input("Skriv in ett tal mellan 1-10"))

while not 1 <= tal <= 10:
    print("Du är ju dålig... LÄS UPPGIFTEN IGEN!!!! ")
    tal = int(input("Skriv in ett tal mellan 1-10: "))
    
else:
    print("Done!")
'''
'''
#uppgift 4
i = 1
while i < 21:
    print (i, end=" ")
    print(i ** 2, end=" ")
    print(i ** 3, end=" ")
    print()
    i += 1
'''
'''
#uppgift 5
x = 1 #räknar rader
while x < 6:
    i = 1
    while i < 10:
        print (i, end=" ")
        i += 1
    print ()
    x += 1
'''
'''
#uppgift 6
i = 1

tal = int(input("Skriv in ett högt tal, vi kör fizzbuzz: "))
while i < tal:
    if i % 3==0 and i % 5==0:
        print ("FizzBuzz ")
    elif i % 5==0:
        print ("Buzz ")
    elif i % 3==0:
        print ("Fizz ")
    else:
        print (i)
    i += 1
'''

