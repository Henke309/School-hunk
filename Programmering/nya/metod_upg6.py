def age(x):
    if x >= 18:
        return True
    else:
        return False 

x = int(input("skriv in din ålder: "))
print(age(x))