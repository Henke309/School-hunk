"""
Name: Henrik Nguyen
Date: 2019-12-03
Info: Bubbelsortering
"""

def bubblesort(tallist):
    for passnum in range(len(tallist) -1, 0, -1 ): #[9,8,7,6,5,4,3,2,1]
        for i in range(passnum):
            if tallist[i] > tallist[i+1]:
                temp = tallist[i]
                tallist[i] = tallist[i+1]
                tallist[i+1] = temp 

aList =[3, 5, 2, 4, 1]

bubblesort(aList)

print(aList)