"""
def linearsearch(list, searchValue):
    
    Perfrom a linear search
    :param list: The list
    :param searchValue: The searchvalue
    :return: Index of searchValue in list. If it not exist it returns -1
    

    for index, obj in enumerate(list):
        if obj == searchValue:
            return index 

    else:
        return -1 

    tallista = [123, 23, 54, 84, 92, 0 ,72, 2, 3, 12, 167]

    search = int(input("Ange ett tal att söka efter: "))

    index = linearsearch(tallista, search)

    if index == -1:
        print("Objektet finns inte i listan")
    else:
        print("hittades på plats ", index + 1)
"""
def binearSearch(list, searchValue):
    """

    Perfrom a linear search
    :param list: The list
    :param searchValue: The searchvalue
    :return: Boolean value. True - exist, Flase - Doesn't exist
    """

    first = 0
    last = len(list) -1 
    found = False

    while first <=last and not found:
        midpoint = (first + last) // 2

        if list[midpoint] == searchValue:
            return True

        else:
            if searchValue < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

tallista = [123, 23, 54, 84, 92, 0 ,72, 2, 3, 12, 167]
tallista.sort()
if binearSearch(tallista, 23):
    print("Hittad! ")
else:
    print("inte hittad! ")