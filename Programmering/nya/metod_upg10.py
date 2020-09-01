def ränta(pengar, räntesats):
    räntekostnad = pengar * räntesats/100
    return räntekostnad

print("*"*51)
print("Räntskit".center(51))

money = int(input("Ange lånbeloppet: "))
interest = float(input("Ange räntan "))

print(ränta(money, interest))

