rAns = 7

guess = int(input("Gissa på ett tal mellan 1-10: "))

if guess == rAns:   
    print ("Sant boi")

elif rAns -1 == guess or rAns + 1 == guess:
    print ("sooo close mate")

else:
    print ("fel bror")