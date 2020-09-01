'''
for tal in range (1, 151):
    if tal % 13 == 0 and tal % 11 == 0 and tal % 7 == 0 and tal % 5 == 0 and tal % 3 == 0:
        print ("FizzBuzzFuzzDizzDuzz")
    
    elif tal % 3 == 0 and tal % 5 == 0:
        print ("FizzBuzz")
    elif tal % 3 == 0 and tal % 7 == 0:
        print ("FizzFuzz")
    
    
    elif tal % 3 == 0:
        print ("Fizz")
    elif tal % 5 == 0 and tal % 7 == 0:
        print ("BuzzFuzz")    
    elif tal % 5 == 0:
        print ("Buzz")
    elif tal % 7 == 0:
       print("Fuzz")
    else:
        print(tal)
'''

for tal in range (1, 10000001):
    output = ""


    if tal % 3 == 0:
        output += "Fizz"

    if tal % 5 == 0:
        output += "Buzz"

    if tal % 7 == 0:
        output += "Fuzz"

    if tal % 11 == 0:
        output += "Bizz"

    if tal % 13 == 0:
        output += "Mizz"

    if output == "":
        print (tal)

    else:
        print (output)
