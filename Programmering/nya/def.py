"""
Name: Henrik Nguyen
Date: 19-11-19
Info:
<Insert information about file>
"""

def info():
    print("Skapat av Henrik nguyen \xa9")

def cube(tal):
    """
    :param tal: talet
    :return: kuben på param tal
    """
    cube = tal ** 3

    return cube

def cubeagain(tal):
    print("Kuben är", tal**3)

info()


print(cube(5))
print(cube(25))
print(cube(35))
print(cube(45))
print(cube(55))