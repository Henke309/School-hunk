def prim(tal):
    """
    räkna upp alla primtal upp till ett specifikt tal
    :param tal: Talet som räknas upp till
    """
    primtal = []

    for x in range(2, tal+1):
        check = False
        for y in range(2, x):
            if x % y == 0:
                check = True

        if not check:
            primtal.append(x)
    
    print(primtal)

def primefactorization():
    primtal = ""

    min = 2
    max = tal 

    while min < max:
        if min % max == 0:
            primtal += "{}*".format(min)
            max / min 
        else:
            min += 1

    primtal += "{}".format(max)

    if primtal == str(tal):
        print("Talet är ett primtal")

    else:
        print(primtal)

    primefactorization()