"""
Name: Henrik Nguyen
Date: 19-11-05
Info:Burr program
<Insert information about file>
"""

burr = int(input("A burrtalet: "))

for tal in range (2, 100):
        
    if tal % burr == 0:
        print("burr")

    #str(burr) kollar ifall det finns något liknande i str(tal)
    elif str(burr) in str(tal):
        print("burr")

    else:
        print(tal)





